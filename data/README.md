# Dataset guide

The project uses `heart_statlog_cleveland_hungary_final.csv`, with 1,190 rows, 11 input features, and one binary target.

## Source

The reference paper describes a combined dataset from Cleveland, Hungarian, Switzerland, Long Beach VA, and Statlog (Heart), obtained through IEEE DataPort. See the [reference paper](https://doi.org/10.1016/j.datak.2024.102339), the [IEEE DataPort dataset page](https://ieee-dataport.org/open-access/heart-disease-dataset-comprehensive), and the [Kaggle distribution](https://www.kaggle.com/datasets/sid321axn/heart-statlog-cleveland-hungary-final). The repository does not record which distribution was used to download this CSV.

## Feature definitions

| Column | Meaning and encoding |
| --- | --- |
| `age` | Age in years |
| `sex` | 0 = female, 1 = male |
| `chest pain type` | 1 = typical angina, 2 = atypical angina, 3 = non-anginal pain, 4 = asymptomatic |
| `resting bp s` | Resting blood pressure in mmHg |
| `cholesterol` | Serum cholesterol in mg/dL |
| `fasting blood sugar` | 1 if fasting blood sugar exceeds 120 mg/dL, otherwise 0 |
| `resting ecg` | 0 = normal, 1 = ST-T wave abnormality, 2 = left ventricular hypertrophy |
| `max heart rate` | Maximum heart rate achieved, in beats per minute |
| `exercise angina` | 0 = no exercise-induced angina, 1 = yes |
| `oldpeak` | Exercise-induced ST depression relative to rest |
| `ST slope` | 1 = upsloping, 2 = flat, 3 = downsloping |
| `target` | 0 = no disease, 1 = disease |

Keep the original column names when running the notebook.

## Cleaning and evaluation

- Remove 272 duplicate rows before splitting, leaving 918 records.
- Convert zero values in cholesterol (172 records), resting blood pressure (1), and ST slope (1) to missing values. Counts refer to the deduplicated data.
- Fit imputation and other learned preprocessing on training folds only. Apply BorderlineSMOTE only to training folds.
- Reserve 46 records for testing. Split the remaining 872 into 610 training and 262 validation records.

The original data contains 629 positive and 561 negative records. After duplicate removal, these counts are 508 and 410. The final test set contains 25 positive and 21 negative records.

The label describes disease status in this dataset. It is not a measured probability of a future cardiac event. These observations are not a representative estimate of disease prevalence in the general population.
