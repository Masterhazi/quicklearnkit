

# Model Imports

QuickLearnKit makes importing machine learning models **fast, intuitive, and teaching-friendly**.  

Instead of long, nested imports like:

```python
from sklearn.ensemble import RandomForestClassifier
```

You can simply write:

```python
from quicklearnkit import RandomForestClassifiermodel
```

This keeps beginner workflows simple while still exposing the **full power of scikit-learn, XGBoost, and other libraries** once the model is instantiated.

---

## Example Usage

```python
from quicklearnkit import (
    LinearRegressionmodel,
    RandomForestRegressionmodel,
    XGBoostRegressionmodel,
    KNeighborsClassifiermodel,
    GradientBoostingClassifiermodel
)

# Regression models
lr_model = LinearRegressionmodel()
rf_model = RandomForestRegressionmodel()
xgb_model = XGBoostRegressionmodel()

# Classification models
knn_classifier = KNeighborsClassifiermodel()
gb_classifier = GradientBoostingClassifiermodel()
```

All imports return **properly initialized model instances**, ready for fitting and prediction.

---

## Supported Models

### 🔢 Regression
- `LinearRegressionmodel()`  
- `KNNRegressionmodel()`  
- `DecisionTreeRegressionmodel()`  
- `RandomForestRegressionmodel()`  
- `GradientBoostingRegressionmodel()`  
- `AdaBoostRegressionmodel()`  
- `XGBoostRegressionmodel()`  
- `ElasticNetRegressionmodel()`  

### 🎯 Classification
- `LogisticRegressionmodel()`  
- `KNeighborsClassifiermodel()`  
- `DecisionTreeClassifiermodel()`  
- `RandomForestClassifiermodel()`  
- `AdaBoostClassifiermodel()`  
- `GradientBoostingClassifiermodel()`  
- `XGBClassifiermodel()`  
- `SVClassifiermodel()`  

---

## Why This Exists

Model imports are intentionally simplified to:

- **Reduce friction for students** — no need to memorize deep module paths.  
- **Encourage focus on concepts** — learners spend time on modeling ideas, not syntax.  
- **Support experimentation** — quick setup for trying multiple models side by side.  
- **Preserve advanced control** — once imported, models behave exactly like their native implementations, allowing full parameter tuning and customization.  

---

✨ **In short:** QuickLearnKit bridges the gap between *teaching simplicity* and *professional flexibility*. It’s ideal for classrooms, tutorials, and rapid prototyping, while still being robust enough for serious experimentation.


