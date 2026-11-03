# Complete results: the collaboration module on RAGC

Complete results of the exploratory extension in Section V-E of the paper, in which the CoFA module uses RAGC (Wu et al., ICDE 2026) as its host forecaster.

**Status.** We decided to run this extension after inspecting the main test results and a test of the CoFA module applied to RAGC's forecasts without refitting. The training recipe and reporting rules were fixed before the runs. These are development results on previously examined benchmarks, not a preregistered or independent confirmation. All 24 evaluations (4 datasets, 3 seeds, cross and target-only modules) are reported.

## Files

| File | Content |
|---|---|
| `summary_test.csv` | Test metrics for every module, deployment, dataset and quantity (72 rows). |
| `comparisons_test.csv` | Paired test MAE comparisons for the K12 and FINAL rows (240 rows). |
| `per_seed.csv` | MAE, RMSE and selected epoch per seed, for validation and test, with and without zero targets (576 rows). |

## Definitions

- **Module:** `cross` reads all three quantities at the sensor; `target_only` reads copies of the target quantity.
- **Deployments:**
  - `K12` corrects each of the twelve RAGC fold forecasters per quantity and averages the corrected forecasts.
  - `FINAL` corrects the single RAGC fit of the paper's main table.
  - `TRANSFER` applies the K12-selected checkpoint to that single fit.
- **Units:** flow in vehicles per five minutes, occupancy as a fraction, speed in mph.
- **Means and SDs:** mean and sample SD of three seed-level scores (seeds 2024, 2025, 2026).
- **Gain:** `100 (1 - candidate MAE / reference MAE)`, so positive values favor the candidate.
- **Intervals:** 95% day-block intervals with 10,000 resamples. They are per-cell, omit training randomness, and are not corrected for multiple comparisons.
- **Lowest against 11 baselines:** below all eleven baseline configurations of the main table. These counts do not measure how much fold averaging or the module contributes.

## Limits

- `TRANSFER` values come from run records, with no day-block analysis, so `comparisons_test.csv` does not include them.
- RAGC's 12-fold mean without the module is not included yet, so the K12 rows cannot be split into fold averaging and module here. No baseline in the main table is given a fold average.
- The inference latency of these deployments was not measured.
