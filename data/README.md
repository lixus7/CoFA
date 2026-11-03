# Data layout

Each dataset has its own folder, `data/<dataset>/`, with these arrays (T steps, N sensors, 3 quantities in the order flow, occupancy, speed):

| File | Shape and type | Content |
|---|---|---|
| `labels.npy` | T×N×3, float64 | Raw values, finite everywhere (invalid entries hold 0). Occupancy is a fraction; speed is in mph. |
| `valid.npy` | T×N×3, bool | Target-validity mask. |
| `causal.npy` | T×N×3, float32 | Causal forward fill of the valid values, with zeros before the first valid value. |
| `adj.npy` | N×N, float32 | Road-graph adjacency, used only by D²STGNN. |

PeMS04 and PeMS08 use their three-quantity releases. Dataset sizes, splits and congestion thresholds are in `../configs/datasets.json`.
