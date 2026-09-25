# Experiment results

## Reported results

`reported_test_metrics.csv` contains the rounded results already reported in the notebook and thesis. It is a historical reference, not a new training run.

## New runs

Run the notebook from the beginning through **Export experiment results**. Each execution creates `runs/<UTC timestamp>/` with these files.

| File | Contents |
| --- | --- |
| `test_metrics.csv` | Numeric test metrics for the five final models |
| `test_confidence_intervals.csv` | Test metrics with 95% confidence intervals |
| `validation_metrics.csv` | Validation comparison of tuning methods |
| `hyperparameters.json` | Best parameters and CV recall for both searches, plus the selected method |
| `split_rows.csv` | Train, validation, and test membership using zero-based original CSV row positions, excluding the header |
| `test_predictions.csv` | Test labels, probabilities, and predictions for each model |
| `statistical_comparisons.csv` | Paired comparisons and adjusted p-values |
| `ablation_cv.csv` | Cross-validation results of the four CatBoost configurations |
| `ablation_test.csv` | Test results of those configurations |
| `run_metadata.json` | Data SHA-256, seeds, split sizes, threshold, bootstrap count, Python and package versions |

Compare dataset hashes and split membership before comparing metrics. The test selection uses seed 786, while model training, validation splitting, and cross-validation use `SEED = 2025`. A fixed seed helps reproduce a run but does not replace matching data and software versions.

The export uses results already computed by the notebook. It does not retrain models or overwrite previous run directories. Rerun from the beginning after changing data or training settings to avoid exporting stale variables.
