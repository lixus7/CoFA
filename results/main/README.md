# Results of the main comparison

Results behind Table II (main comparison), Table III (further baselines), Table IV (early fusion) and Table V (deployments) of the paper. Every cell of these tables was recomputed from these files and matched the paper.

**Status.** All four benchmarks, including their test splits, were used during development, and K12 was chosen as CoFA's reported deployment after test results were seen (Sections I, IV-E and VI of the paper). These are development results, not an independent confirmation.

## Files

| File | Content |
|---|---|
| `main_table_test.csv` | Test metrics for the 17 rows of Table II on every dataset and quantity (204 rows). The two CoFA on RAGC rows come from `../ragc_extension/`. |
| `per_seed.csv` | MAE and RMSE per seed for validation and test, with and without zero targets, for 19 configurations (11 baselines, DecoupleST SISO and its 12-fold mean, and the K12, FINAL and TRANSFER deployments of the cross and target-only modules, 2,736 rows). |
| `comparisons_test.csv` | Paired test MAE comparisons, 12 pairs on 12 cells (144 rows). |
| `further_baselines_test.csv` | Test metrics for every trained form of the 17 further baselines on PeMS04 and PeMS08 (276 rows). |
| `further_baselines_per_seed.csv` | MAE and RMSE per seed for those forms, for validation and test, with and without zero targets (3,312 rows). |

## Definitions

- **Variants:** SISO (1→1) predicts a quantity from its own history; MISO (3→1) predicts it from all three quantities, one model per quantity; MIMO (3→3) predicts all three with one model.
- **Deployments:**
  - `K12` corrects each of the twelve fold forecasters per quantity and averages the corrected forecasts. K12 + Cross is CoFA.
  - `FINAL` corrects one forecaster per quantity, refit on the training split. FINAL + Cross is CoFA-FINAL.
  - `TRANSFER` applies the K12-selected checkpoint to that single forecaster.
- **Modules:** `Cross` reads all three quantities at the sensor; `Self` is the target-only control.
- **Units:** flow in vehicles per five minutes, occupancy as a fraction (the paper shows percent), speed in mph.
- **Means and SDs:** mean and sample SD of three seed-level scores (seeds 2024, 2025, 2026).
- **Targets:** `all valid` is the primary metric and keeps valid zeros; `valid, excluding zero` drops zero targets.
- **Ranked:** the eleven baselines, CoFA and CoFA on RAGC (K12). `lowest_*_of_13_ranked` marks the bold cells of Table II.
- **Lowest against 11 baselines:** below all eleven baselines, given for the rows that are not baselines. These counts do not measure how much fold averaging or the module contributes.
- **Gain:** `100 (1 - candidate MAE / reference MAE)`, so positive values favor the candidate.
- **Intervals:** 95% day-block intervals with 10,000 resamples. They are per-cell, omit training randomness, and are not corrected for multiple comparisons.

## Limits

- The further baselines ran on PeMS04 and PeMS08 only. `lowest_mae_of_model` marks the form shown in Table III: the lowest test MAE among a model's trained forms, a descriptive minimum that favors the baseline, not a validation-selected configuration.
- The best baseline in `comparisons_test.csv` is the configuration with the lowest test MAE in that cell, also chosen on test.
- The other analyses in the paper (traffic states, forecast leads, seed ensembles, latency and training cost) are not included here.
