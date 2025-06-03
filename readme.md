
# QuickLearnkit

QuickLearnkit is a lightweight machine learning wrapper designed to simplify model imports and streamline workflows. No more deep module navigation—import models effortlessly and start building!

## Installation

Install QuickLearnkit using pip:

```bash
pip install quicklearn
```

## Quick Model Imports

QuickLearnkit provides seamless access to essential machine learning models with minimal syntax. Simply import and initialize models without the usual clutter.

### **Example Usage**
```python
from quicklearnkit import LinearRegressionmodel, RandomForestRegressionmodel, XGBoostRegressionmodel
from quicklearnkit import KNeighborsClassifiermodel, GradientBoostingClassifiermodel

# Initialize models directly
lr_model = LinearRegressionmodel()
rf_model = RandomForestRegressionmodel()
xgb_model = XGBoostRegressionmodel()

# Initialize classifiers
knn_classifier = KNeighborsClassifiermodel()
gb_classifier = GradientBoostingClassifiermodel()
```

## **Supported Models**
QuickLearnkit offers easy access to commonly used supervised learning models:

### **Regression Models**
- Linear Regression (`LinearRegressionmodel()`)
- K-Nearest Neighbors Regression (`KNNRegressionmodel()`)
- Decision Tree Regression (`DecisionTreeRegressionmodel()`)
- Random Forest Regression (`RandomForestRegressionmodel()`)
- Gradient Boosting Regression (`GradientBoostingRegressionmodel()`)
- AdaBoost Regression (`AdaBoostRegressionmodel()`)
- XGBoost Regression (`XGBoostRegressionmodel()`)
- ElasticNet Regression (`ElasticNetRegressionmodel()`)

### **Classification Models**
- Logistic Regression (`LogisticRegressionmodel()`)
- K-Nearest Neighbors Classifier (`KNeighborsClassifiermodel()`)
- Decision Tree Classifier (`DecisionTreeClassifiermodel()`)
- Random Forest Classifier (`RandomForestClassifiermodel()`)
- AdaBoost Classifier (`AdaBoostClassifiermodel()`)
- Gradient Boosting Classifier (`GradientBoostingClassifiermodel()`)
- XGBoost Classifier (`XGBClassifiermodel()`)
- Support Vector Classifier (`SVClassifiermodel()`)

## **Randomized Data Generation**
Generate random arrays with specific characteristics:
```python
from quicklearn import create_random

random_data = create_random(mean=0, std_dev=1, size=100)
print(random_data)
```

## **Contribute**
Want to improve QuickLearnkit? Fork the repository, suggest enhancements, and be a part of making machine learning more accessible.

## **License**
This project is licensed under the MIT License.

---

QuickLearnkit makes machine learning imports effortless—so you can focus on building models, not writing complex import statements! 🚀



