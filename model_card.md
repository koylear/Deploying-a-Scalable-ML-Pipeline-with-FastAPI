# Model Card

## Model Details
Random Forest Classifier and FastAPI were used
Contact - Kjersten Oylear, koylear@wgu.edu

## Intended Use
Model predicts salary category based on demographic data.

## Training Data
Source: publicly available census data. Training data consists of 80% of the dataset.

## Evaluation Data
Source: publicly available census data. Evaulation data consists of 20% of the dataset.

## Metrics
Precision - accuracy of positive predictions
Recall - proportion of positives correctly identified
F1 - harmonic mean of Precision and Recall
First run metrics - Precision: 0.7389 | Recall: 0.6359 | F1: 0.6835

## Ethical Considerations
Dataset reflects historical data, which may include biases related to race, gender, or socioeconomic status.

## Caveats and Recommendations
Model may not correctly apply to other populations or time periods, and may not perform well on datasets with missing values. Model could be enhanced with hyperparameter tuning and more diverse datasets.