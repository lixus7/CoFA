# CoFA

Code for *Beyond Individual Forecasts: Cross-Quantity Collaboration for Traffic Prediction* (submitted to ICDE 2027).

CoFA forecasts flow, occupancy and speed in two stages. One forecaster per quantity (DecoupleST) produces a multi-step forecast. A sensor-level collaboration module then corrects each forecast from the recent histories and forecasts of all three quantities at that sensor. The module is fitted to out-of-fold forecasts while the forecasters stay fixed.

Two deployments are reported:

- **K12 (CoFA):** the module corrects each of the twelve fold forecasters per quantity, and the corrected forecasts are averaged.
- **FINAL (CoFA-FINAL):** the module corrects one forecaster per quantity, refit on the training split. It has lower latency.

## Layout

| Path | Content |
|---|---|
| `run.py` | Command-line entry for every stage |
| `cofa/decouplest.py` | DecoupleST forecaster |
| `cofa/module.py` | Collaboration module; `mode='self'` is the target-only control |
| `cofa/train.py` | Forecaster training (200 epochs at most, patience 30) |
| `cofa/fold_inputs.py`, `cofa/prepare.py` | Twelve-fold partitions and fold-local causal inputs |
| `cofa/banks.py` | Assembles out-of-fold, fold and final forecasts into one bank |
| `cofa/dual_adapter.py`, `cofa/train_adapter.py`, `cofa/selection.py` | Module training, per-deployment checkpoint selection, and evaluation |
| `cofa/evaluation.py` | Metrics with validity masks, traffic states and forecast leads |
| `cofa/models.py`, `cofa/external_models.py` | DecoupleST MISO, RAGC and baseline wrappers |
| `configs/` | Dataset settings and baseline source commits |
| `data/` | Data layout, checksums and provenance; the arrays themselves are in the `data-v1` release |
| `results/main/` | Results behind the main comparison, further baselines, early fusion and deployment tables |
| `results/ragc_extension/` | Complete results of the exploratory extension on RAGC (Section V-E of the paper) |
| `tests/smoke_cpu.py` | End-to-end check on synthetic data |

## Setup

Python 3.11 with the packages in `requirements.txt`. See `third_party/README.md` for the baselines.

The aligned PeMS03 and PeMS07 arrays are in the [`data-v1` release](https://github.com/lixus7/CoFA/releases/tag/data-v1). `data/README.md` describes how to download them, how to build PeMS04 and PeMS08, and how the arrays were made.

## Running

```bash
python run.py prepare --dataset pems08
python run.py pipeline --dataset pems08 --seed 2024
```

`pipeline` runs the 39 forecaster fits (12 folds and one final fit, per quantity), the bank, the cross-quantity module and the target-only control, one after another. Results go to `results/<task id>/`. To schedule the steps yourself:

```bash
python run.py forecaster --dataset pems08 --seed 2024 --quantity flow --fold 3
python run.py forecaster --dataset pems08 --seed 2024 --quantity flow
python run.py bank --dataset pems08 --seed 2024
python run.py module --dataset pems08 --seed 2024 --arm v1_cross
python run.py evaluate --dataset pems08 --seed 2024 --arm v1_cross
```

Baselines and controls:

```bash
python run.py forecaster --dataset pems08 --seed 2024 --quantity speed --architecture decouplest_miso
python run.py forecaster --dataset pems08 --seed 2024 --quantity speed --architecture ragc
python run.py baseline --dataset pems08 --seed 2024 --architecture staeformer --variant miso_speed
```

The paper uses seeds 2024, 2025 and 2026. Each `evaluate` run writes the K12, FINAL and TRANSFER predictions and metrics for the validation and test splits.

To check that the code runs without the data (a few minutes on CPU):

```bash
python tests/smoke_cpu.py
```

## Provenance

This is the code of the PeMS03 and PeMS07 runs, with cluster scheduling and internal bookkeeping removed. PeMS04 and PeMS08 were run with an earlier revision, before fold-local input filling was added for the missing records in PeMS03 and PeMS07. Device selection was generalized so that the code also runs on CPU; the reported results were produced on GPUs.

## License

The code and the result tables are under the [MIT License](LICENSE). The license does not cover the data, whose sources are listed in `data/README.md`, or the baseline code, which is not redistributed here.
