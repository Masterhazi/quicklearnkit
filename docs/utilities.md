
# Utilities

QuickLearnKit provides **structured utility functions** that simplify common data science operations while remaining transparent and customizable. These utilities are designed to reduce boilerplate, improve clarity, and keep workflows reproducible without hiding the mechanics of machine learning.

---

## Sampler

The `Sampler` class enables controlled random sampling from:

- Python lists  
- NumPy arrays  
- pandas DataFrames  

### Initialization

```python
Sampler(data, n=1, random_state=None, replace=False, axis=0, stateful=False)
```

### Parameters

| Parameter      | Description                                |
|----------------|--------------------------------------------|
| `data`         | Dataset to sample from                     |
| `n`            | Number of samples                          |
| `random_state` | Seed for reproducibility                   |
| `replace`      | Whether to sample with replacement         |
| `axis`         | For DataFrames: `0` = rows, `1` = columns  |
| `stateful`     | If `True`, RNG state advances across calls |

### Example

```python
from quicklearnkit import Sampler
import seaborn as sns

df = sns.load_dataset("tips")

sampler = Sampler(df, n=3, random_state=42)
sample = sampler.sample()
```

**Why it matters:**  
Instead of writing repetitive sampling logic, learners can focus on *what* they’re sampling and *why*, while instructors can demonstrate reproducibility and randomness control.

---

## Train–Test Split

Split datasets into training and testing sets with support for:

- Shuffling  
- Stratification  
- NumPy arrays  
- pandas DataFrames  

### Function Signature

```python
train_test_split(data, test_size=0.25, shuffle=True, stratify=None, random_state=None)
```

### Example

```python
from quicklearnkit import train_test_split

train, test = train_test_split(df, test_size=0.3, random_state=42)
```

**Why it matters:**  
This mirrors scikit-learn’s functionality but keeps syntax simple and consistent across QuickLearnKit utilities, making it easier for beginners to grasp dataset partitioning.

---

## ProbabilisticImputer

A **group-aware, probabilistic categorical imputer**.  
It learns probability distributions from observed data and fills missing values by sampling from those distributions.

### Initialization

```python
ProbabilisticImputer(group_col, target_col, random_state=None, stateful=False)
```

### Methods

| Method              | Description                      |
|---------------------|----------------------------------|
| `fit(df)`           | Learns probability distributions |
| `transform(df)`     | Imputes missing values           |
| `fit_transform(df)` | Fit and transform in one step    |

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

df_imputed = imputer.fit_transform(df)
```

**Why it matters:**  
Instead of defaulting to naive imputation (like filling with mode or mean), this approach preserves **distributional realism** and respects **group-level differences** (e.g., imputing cabin decks by passenger class).

---

## Random Data Generation

Generate synthetic numerical data for experimentation and demonstrations:

```python
from quicklearnkit import create_random

random_data = create_random(mean=0, std_dev=1, size=100)
```

**Why it matters:**  
Perfect for teaching statistical concepts, testing workflows, or demonstrating algorithms without needing a real dataset.

---

## Design Intent

QuickLearnKit utilities are designed to:

- **Reduce repetitive boilerplate** so learners can focus on concepts.  
- **Improve teaching clarity** with explicit, readable functions.  
- **Maintain reproducibility** through controlled randomness.  
- **Avoid hiding ML mechanics** — utilities are transparent, not “black boxes.”  
- **Stay simple and explicit**, making them ideal for classrooms, tutorials, and rapid prototyping.  

