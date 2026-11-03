# Baseline code

The baseline models are not redistributed here. `cofa/external_models.py` and `cofa/models.py` load them from this folder. The repositories and commits used in the paper are in `../configs/baseline_sources.json`.

| Module expected here | Source |
|---|---|
| `staeformer_core.py` (class `STAEformer`) | XDZhelheim/STAEformer |
| `himnet_core.py` (class `HimNet`) | XDZhelheim/HimNet |
| `d2stgnn/` (class `D2STGNN`) | BasicTS (D²STGNN architecture) |
| `ragc_upstream/` (`models/RAGC.py`) | wkq-wukaiqi/RAGC |

Constructor arguments are in `cofa/external_models.py` and `cofa/models.py`. For PeMS03 and PeMS07, HimNet's teacher forcing uses the model's own previous prediction at positions whose future label is invalid.
