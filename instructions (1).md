# Wine Quality Prediction – ML Project Instructions

## Objective
Predict whether a wine is of **good quality** or **bad quality** based on its chemical properties.
The target variable is `quality`, which is binary:
- `1` → Good Quality (quality >= 7)
- `0` → Bad Quality (quality < 7)

## Dataset Context
The dataset contains physicochemical tests (e.g., acidity, sugar, pH, alcohol) of red wines.
Each row represents one wine sample with its measured properties.
The data was collected from laboratory tests and expert wine quality scores.

### Columns & Explanations
- **fixed acidity** → Concentration of non-volatile acids (like tartaric acid). High values may affect taste balance.
- **volatile acidity** → Amount of acetic acid (vinegar-like). Higher levels usually lower wine quality. (Your plot showed wines with higher volatile acidity had lower quality).
- **citric acid** → Adds freshness and flavor. Moderate levels are linked with better quality. (Your plot showed higher citric acid = higher quality).
- **residual sugar** → Sugar left after fermentation. Small amounts are normal; high values make wine sweet.
- **chlorides** → Salt concentration in wine. High chlorides negatively affect taste.
- **free sulfur dioxide** → SO₂ in free form; helps prevent microbial growth but too much harms flavor.
- **total sulfur dioxide** → Total SO₂ content; excessive levels are undesirable.
- **density** → Related to sugar/alcohol content. High density = usually sweeter, low alcohol.
- **pH** → Acidity level of wine (lower pH = more acidic).
- **sulphates** → Additive for preservation and flavor. Positively correlated with quality.
- **alcohol** → % alcohol content. Higher alcohol generally improves perceived quality.
- **quality (target)** → Expert score converted into binary (Good vs Bad).

## Observations from Data Exploration
- Wines with **higher volatile acidity** tend to have **lower quality**.
- Wines with **higher citric acid** tend to have **better quality**.
- Alcohol content and sulphates show a **positive correlation** with quality.

## Desired Output
The model should predict a probability or class label (0 = bad, 1 = good).

The final output should be a CSV with one column:
- `PredictedQuality` (values 0 or 1)