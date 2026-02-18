# QuickLearnKit

QuickLearnKit is a **learning-first machine learning utilities library** designed to make common ML and data science workflows simple, readable, and beginner-friendly — without blocking advanced users from full customization.

The philosophy is:

> **Remove mechanical friction so students can focus on concepts, not syntax.**

QuickLearnKit provides:

* Easy model imports
* Random sampling utilities
* Train–test splitting
* Probabilistic, group-aware imputation
* Teaching-friendly plotting with optional value labels

---

## Installation

```bash
pip install quicklearnkit
```

---

## Quick Start

```python
from quicklearnkit import (
    Sampler,
    train_test_split,
    ProbabilisticImputer,
    bar_plot
)

import seaborn as sns

# Load example dataset
df = sns.load_dataset("titanic")

# Sample data
sampler = Sampler(df, n=5, random_state=42)
print(sampler.sample())

# Split data
train, test = train_test_split(df, test_size=0.25)

# Impute missing values
imputer = ProbabilisticImputer("pclass", "deck", random_state=42)
df_imputed = imputer.fit_transform(df)

# Plot
bar_plot(df, x="class", y="fare", show_values="yes")
```

---

# Model Imports

QuickLearnKit allows you to import commonly used machine learning models without navigating deep module paths.

### Example

```python
from quicklearnkit import (
    LinearRegressionmodel,
    RandomForestRegressionmodel,
    XGBoostRegressionmodel,
    KNeighborsClassifiermodel,
    GradientBoostingClassifiermodel
)

lr_model = LinearRegressionmodel()
rf_model = RandomForestRegressionmodel()
xgb_model = XGBoostRegressionmodel()

knn_classifier = KNeighborsClassifiermodel()
gb_classifier = GradientBoostingClassifiermodel()
```

---

## Supported Models

### Regression Models

* `LinearRegressionmodel()`
* `KNNRegressionmodel()`
* `DecisionTreeRegressionmodel()`
* `RandomForestRegressionmodel()`
* `GradientBoostingRegressionmodel()`
* `AdaBoostRegressionmodel()`
* `XGBoostRegressionmodel()`
* `ElasticNetRegressionmodel()`

### Classification Models

* `LogisticRegressionmodel()`
* `KNeighborsClassifiermodel()`
* `DecisionTreeClassifiermodel()`
* `RandomForestClassifiermodel()`
* `AdaBoostClassifiermodel()`
* `GradientBoostingClassifiermodel()`
* `XGBClassifiermodel()`
* `SVClassifiermodel()`

---

# Utilities

## 1. Sampler

The `Sampler` class allows you to randomly select elements from:

* Python lists
* NumPy arrays
* pandas DataFrames

It supports both **stateless** (reproducible) and **stateful** (streaming/simulation) modes.

### Initialization

```python
Sampler(data, n=1, random_state=None, replace=False, axis=0, stateful=False)
```

### Parameters Explained

| Parameter      | Type                                  | Description                                                                                      |
| -------------- | ------------------------------------- | ------------------------------------------------------------------------------------------------ |
| `data`         | list, numpy.ndarray, pandas.DataFrame | The dataset to sample from                                                                       |
| `n`            | int                                   | Number of samples to return                                                                      |
| `random_state` | int or None                           | Seed for reproducibility. Same seed = same result                                                |
| `replace`      | bool                                  | If `True`, sampling is done **with replacement** (duplicates allowed). If `False`, no duplicates |
| `axis`         | int                                   | Only applies to DataFrames. `0` = sample rows, `1` = sample columns                              |
| `stateful`     | bool                                  | If `True`, RNG state continues across calls. If `False`, sampling is reproducible on every call  |

### Example

```python
from quicklearnkit import Sampler
import seaborn as sns

df = sns.load_dataset("tips")

sampler = Sampler(df, n=3, random_state=42, replace=False)

sample1 = sampler.sample()
sample2 = sampler.sample()  # Same output if stateful=False
```

---

## 2. Train–Test Split

Split datasets into training and testing sets with support for:

* Shuffling
* Stratification
* NumPy arrays
* pandas DataFrames

### Function

```python
train_test_split(data, test_size=0.25, shuffle=True, stratify=None, random_state=None)
```

### Parameters Explained

| Parameter      | Type                           | Description                                                |
| -------------- | ------------------------------ | ---------------------------------------------------------- |
| `data`         | array-like or pandas.DataFrame | Dataset to split                                           |
| `test_size`    | float                          | Proportion of data to use as test set (e.g., `0.25` = 25%) |
| `shuffle`      | bool                           | If `True`, data is shuffled before splitting               |
| `stratify`     | array-like or str              | Column or labels to preserve class distribution in splits  |
| `random_state` | int or None                    | Seed for reproducibility                                   |

### Example

```python
from quicklearnkit import train_test_split

train, test = train_test_split(df, test_size=0.3, shuffle=True, random_state=42)
```

---

## 3. ProbabilisticImputer

A **group-aware, probabilistic categorical imputer**. It learns probability distributions from observed data and fills missing values by sampling from those distributions.

This allows:

* Realistic missing data handling
* Teaching probability-based imputation
* Reproducible preprocessing

### Initialization

```python
ProbabilisticImputer(group_col, target_col, random_state=None, stateful=False)
```

### Parameters Explained

| Parameter      | Type        | Description                                                                                            |
| -------------- | ----------- | ------------------------------------------------------------------------------------------------------ |
| `group_col`    | str         | Column used to group data (e.g., class, category)                                                      |
| `target_col`   | str         | Column where missing values will be imputed                                                            |
| `random_state` | int or None | Seed for reproducibility                                                                               |
| `stateful`     | bool        | If `True`, RNG state advances across calls (useful for simulation). If `False`, output is reproducible |

### Methods

| Method              | Description                                        |
| ------------------- | -------------------------------------------------- |
| `fit(df)`           | Learns probability distributions from known values |
| `transform(df)`     | Imputes missing values using learned distributions |
| `fit_transform(df)` | Fit and transform in one step                      |

### Example

```python
from quicklearnkit import ProbabilisticImputer
import seaborn as sns

df = sns.load_dataset("titanic")

imputer = ProbabilisticImputer(
    group_col="pclass",
    target_col="deck",
    random_state=42
)

imputed_df = imputer.fit_transform(df)
```

---

# Plotting (Teaching-Friendly Visualization)

QuickLearnKit provides wrappers around **seaborn + matplotlib** that allow students to display values on plots using a simple switch:

```python
show_values="yes"
```

All plotting functions:

* Return a **matplotlib Axes object**
* Allow full customization (labels, limits, grids, styles)
* Automatically display the plot by default

---

## Common Parameters (All Plot Functions)

| Parameter     | Type             | Description                                                                      |
| ------------- | ---------------- | -------------------------------------------------------------------------------- |
| `data`        | pandas.DataFrame | Dataset used for plotting                                                        |
| `x`           | str              | Column for x-axis                                                                |
| `y`           | str              | Column for y-axis (if applicable)                                                |
| `title`       | str or None      | Plot title                                                                       |
| `show_values` | str              | "yes" or "no" — whether to display numeric values                                |
| `fmt`         | str              | Format string for value labels (e.g. `{:.2f}`)                                   |
| `show`        | bool             | If `True`, displays plot immediately. If `False`, returns Axes for customization |

---

## bar_plot

```python
bar_plot(data, x, y, title=None, show_values="no", fmt="{:.1f}", show=True)
```

### Example

```python
from quicklearnkit import bar_plot
import seaborn as sns

_df = sns.load_dataset("tips")

ax = bar_plot(
    _df,
    x="day",
    y="total_bill",
    show_values="yes",
    show=False
)

ax.set_xlabel("Day of Week")
ax.set_ylabel("Average Bill")
ax.set_ylim(0, 40)

import matplotlib.pyplot as plt
plt.show()
```

---

## line_plot

```python
line_plot(data, x, y, title=None, show_values="no", fmt="{:.2f}", show=True)
```

---

## scatter_plot

```python
scatter_plot(data, x, y, title=None, show_values="no", fmt="{:.2f}", show=True)
```

---

## count_plot

```python
count_plot(data, x, title=None, show_values="no", show=True)
```

---

## box_plot

Displays **mean values** when `show_values="yes"`.

```python
box_plot(data, x=None, y=None, title=None, show_values="no", fmt="{:.2f}", show=True)
```

---

## hist_plot

Displays **bin counts** when `show_values="yes"`.

```python
hist_plot(data, x, bins=10, title=None, show_values="no", fmt="{:.0f}", show=True)
```

---

# Random Data Generation

Generate random numerical arrays for experiments and demonstrations.

```python
from quicklearnkit import create_random

random_data = create_random(mean=0, std_dev=1, size=100)
```

---

# Pipeline (Notebook → Script Bridge)

QuickLearnKit now includes a **Pipeline system** that helps you move from interactive notebook experimentation to clean, structured Python scripts.

The goal is to make transitioning from:

> 🧪 Exploration in notebooks → 🧾 Reproducible `.py` pipelines

simple, explicit, and disciplined.

---

## Creating a Pipeline

```python
from quicklearnkit import Pipeline

pipe = Pipeline()
```

Each `Pipeline()` instance is isolated and independent.

---

## 1. Manual Commit

Commit top-level functions explicitly:

```python
def preprocess(X):
    return X

def train(X):
    return "model"

pipe.commit(preprocess, outputs=["X_scaled"], stage="Preprocessing")
pipe.commit(train, inputs=["X_scaled"], outputs=["model"], stage="Training")
```

### Parameters Explained

| Parameter | Type        | Description                                      |
| --------- | ----------- | ------------------------------------------------ |
| `func`    | Callable    | Top-level function to include in the pipeline    |
| `inputs`  | list of str | Expected input variable names (for validation)   |
| `outputs` | list of str | Output variable names produced by the function   |
| `stage`   | str         | Optional grouping label for script organization  |
| `mode`    | str         | `"functions"` enables semi-automatic commit mode |

---

## 2. Semi-Automatic Commit

Capture all user-defined top-level functions in the current notebook:

```python
pipe.commit(mode="functions")
```

Semi-auto mode:

* Detects user-defined functions
* Skips built-in functions
* Skips private functions (`_helper`)
* Skips nested functions
* Avoids duplicates

Metadata can later be updated:

```python
pipe.commit(train, inputs=["X_scaled"], outputs=["model"])
```

---

## 3. Pipeline Summary

Inspect committed functions and metadata:

```python
pipe.summary()
```

Example output:

```
[QuickLearn] 📦 Pipeline Summary

1. preprocess
   Stage: Preprocessing
   Inputs: []
   Outputs: ['X_scaled']

2. train
   Stage: Training
   Inputs: ['X_scaled']
   Outputs: ['model']
```

---

## 4. Register Imports

QuickLearnKit does **not** automatically capture notebook imports.
Imports must be registered explicitly to be included in the compiled script.

### Multiline string:

```python
pipe.add_import("""
import pandas as pd
import numpy as np
from quicklearnkit import RandomForestClassifiermodel
""")
```

### List format:

```python
pipe.add_import([
    "import pandas as pd",
    "import numpy as np"
])
```

Imports are:

* Validated
* Deduplicated
* Inserted at the top of the generated script

---

## 5. Dependency Validation

If `inputs` and `outputs` metadata are provided, QuickLearnKit can validate logical ordering.

```python
pipe.compile("pipeline.py", validate=True)
```

Validation checks:

* Missing inputs
* Duplicate outputs
* Incorrect dependency flow

### Strict Mode

```python
pipe.compile("pipeline.py", validate="strict")
```

Strict mode raises an error instead of warning.

---

## 6. Compile to Script

Generate a clean Python script:

```python
pipe.compile("pipeline.py")
```

Generated file includes:

* Registered imports
* Stage-based comment grouping
* Ordered function definitions
* A clean execution block

Example structure:

```python
import pandas as pd

# ==============================
# Preprocessing
# ==============================

def preprocess(X):
    return X

# ==============================
# Training
# ==============================

def train(X):
    return "model"

if __name__ == '__main__':
    print('Pipeline ready.')
```

---

## 7. Reset Pipeline

Clear committed functions and imports:

```python
pipe.reset()
```

This resets:

* Committed functions
* Metadata
* Imports
* Compile lock

---

## Guard Rails

To ensure clean compilation, QuickLearnKit prevents committing:

* Lambda functions
* Built-in functions
* Class methods
* Nested functions
* Non-user-defined callables

Only top-level Python functions can be committed.

---

## Example: Full Hybrid Workflow

```python
from quicklearnkit import Pipeline

pipe = Pipeline()

pipe.add_import("""
import pandas as pd
from quicklearnkit import RandomForestClassifiermodel
""")

def preprocess(X):
    return X

def train(X):
    model = RandomForestClassifiermodel()
    return model

pipe.commit(preprocess, outputs=["X_clean"], stage="Preprocessing")
pipe.commit(train, inputs=["X_clean"], outputs=["model"], stage="Training")

pipe.compile("ml_pipeline.py", validate=True)
```

---

This extends QuickLearnKit from a learning utility library into a structured bridge between experimentation and scripting — while keeping full control in the developer’s hands.

---

If you’d like next, we can:

* Add a **Table of Contents** (recommended now that it's growing)
* Split README into sections for docs hosting
* Or prepare a clean `CHANGELOG.md` for this release

# Contributing

Want to improve QuickLearnKit?

1. Fork the repository
2. Create a feature branch
3. Add tests and documentation
4. Submit a pull request

---

# License

MIT License

---

QuickLearnKit helps you move from *learning* to *building* faster — without sacrificing clarity or control. 🚀
