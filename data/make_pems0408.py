#!/usr/bin/env python3
"""Build data/<dataset>/ for PeMS04 or PeMS08 from the ASTGCN release (see README.md in this folder).

Usage: python data/make_pems0408.py --npz pems08.npz --distance distance.csv --out data/pems08
"""
import argparse
import csv
from pathlib import Path

import numpy as np

q = argparse.ArgumentParser(description=__doc__)
q.add_argument('--npz', required=True)
q.add_argument('--distance', required=True)
q.add_argument('--out', required=True)
a = q.parse_args()
with np.load(a.npz) as z:
    labels = z['data'].astype(np.float64)
valid = np.isfinite(labels)
assert valid.all(), 'expected every entry of the release to be finite'
adj = np.zeros((labels.shape[1], labels.shape[1]), np.float32)
with open(a.distance, newline='') as f:
    for row in csv.DictReader(f):
        adj[int(row['from']), int(row['to'])] = adj[int(row['to']), int(row['from'])] = 1
out = Path(a.out)
out.mkdir(parents=True, exist_ok=True)
np.save(out/'labels.npy', labels)
np.save(out/'valid.npy', valid)
np.save(out/'causal.npy', labels.astype(np.float32))
np.save(out/'adj.npy', adj)
print(out, labels.shape, 'edges', int(adj.sum()/2))
