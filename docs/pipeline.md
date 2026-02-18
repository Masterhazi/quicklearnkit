Here’s a cleaned, polished, and slightly expanded version of your **Pipeline (Notebook → Script Bridge)** section. I’ve tightened the language, added context, and emphasized the teaching/structuring benefits so it feels more like a guide than raw documentation:

---

# Pipeline (Notebook → Script Bridge)

QuickLearnKit includes a **Pipeline system** that helps transition from interactive notebook experimentation to clean, structured Python scripts.  

It is **not** a workflow scheduler or DAG engine.  
It is a **disciplined bridge** between experimentation and scripting.

---

## Why Pipeline Exists

Notebooks are great for exploration, but they often lead to:

- Multiple trial cells  
- Reordered or duplicated logic  
- Debug code mixed with final code  
- Hard-to-reproduce workflows  

The Pipeline system solves this by letting you:

- Explicitly commit only the functions you want  
- Attach metadata for validation  
- Register required imports  
- Compile a clean `.py` file  

---

## Basic Usage

### 1. Create a Pipeline

```python
from quicklearnkit import Pipeline

pipe = Pipeline()
```

Each `Pipeline()` instance is independent.

---

### 2. Manual Commit

Commit functions explicitly for full control:

```python
def preprocess(X):
    return X

def train(X):
    return "model"

pipe.commit(preprocess, outputs=["X_scaled"], stage="Preprocessing")
pipe.commit(train, inputs=["X_scaled"], outputs=["model"], stage="Training")
```

#### Commit Parameters

| Parameter | Description                        |
|-----------|------------------------------------|
| `func`    | Top-level function to include      |
| `inputs`  | Expected input variable names      |
| `outputs` | Output variable names produced     |
| `stage`   | Optional grouping label            |
| `mode`    | `"functions"` for semi-auto commit |

---

### 3. Semi-Automatic Commit

Capture all top-level user-defined functions:

```python
pipe.commit(mode="functions")
```

Semi-auto mode:

- Detects user-defined functions  
- Skips built-ins and nested functions  
- Avoids duplicates  
- Allows later metadata updates  

You can override metadata later:

```python
pipe.commit(train, inputs=["X_scaled"], outputs=["model"])
```

---

### 4. Register Imports

Pipeline does **not** scrape notebook imports automatically.  
You must explicitly register them:

```python
pipe.add_import("""
import pandas as pd
import numpy as np
""")
```

Imports are:

- Validated  
- Deduplicated  
- Inserted at the top of the compiled file  

---

### 5. Dependency Validation

If `inputs` and `outputs` metadata are provided, QuickLearnKit can validate logical consistency:

```python
pipe.compile("pipeline.py", validate=True)
```

Checks include:

- Missing inputs  
- Duplicate outputs  
- Incorrect dependency flow  

#### Strict Mode

```python
pipe.compile("pipeline.py", validate="strict")
```

Strict mode raises errors instead of warnings.

---

### 6. Compile to Script

Generate a clean Python script:

```python
pipe.compile("pipeline.py")
```

The generated file includes:

- Registered imports  
- Stage-based grouping comments  
- Ordered function definitions  
- Entry execution block  

**Example structure:**

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
    print("Pipeline ready.")
```

---

### 7. Reset Pipeline

Clear committed state:

```python
pipe.reset()
```

This resets:

- Committed functions  
- Metadata  
- Imports  
- Compile lock  

---

## Guard Rails

To ensure clean compilation, Pipeline prevents committing:

- Lambda functions  
- Built-in functions  
- Class methods  
- Nested functions  
- Non-user-defined callables  

Only **top-level Python functions** can be committed.

---

## Design Philosophy

Pipeline is designed to:

- Encourage structured thinking  
- Preserve developer control  
- Avoid hidden magic  
- Prevent automatic code mutation  
- Keep compilation deterministic  

It bridges:

**Notebook experimentation → Clean, reproducible scripts**

---

✨ **In short:** 

```text
                                            ┌─────────────────────┐
                                            │   Jupyter Notebook  │
                                            │  (Exploration,      │
                                            │   trial cells,      │
                                            │   messy imports)    │
                                            └─────────┬───────────┘
                                                      │
                                                      ▼
                                            ┌─────────────────────┐
                                            │   QuickLearnKit     │
                                            │      Pipeline       │
                                            │  • Commit functions │
                                            │  • Register imports │
                                            │  • Validate deps    │
                                            │  • Structure stages │
                                            └─────────┬───────────┘
                                                      │
                                                      ▼
                                            ┌─────────────────────┐
                                            │   Clean Script      │
                                            │   (pipeline.py)     │
                                            │  • Ordered logic    │
                                            │  • Grouped stages   │
                                            │  • Reproducible run │
                                            └─────────────────────┘
```



