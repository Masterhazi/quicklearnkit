
# Visualization

QuickLearnKit provides **teaching-friendly wrappers** around **seaborn + matplotlib**.  

These wrappers are designed to:

- Reduce repetitive plotting boilerplate  
- Optionally display numeric values directly on plots  
- Return a `matplotlib.Axes` object for full customization  
- Automatically display plots by default (ideal for notebooks)  

---

## Common Parameters

All plotting functions share a consistent interface:

| Parameter     | Description |
|---------------|-------------|
| `data`        | pandas DataFrame used for plotting |
| `x`           | Column name for x-axis |
| `y`           | Column name for y-axis (if applicable) |
| `title`       | Optional plot title |
| `show_values` | `"yes"` or `"no"` to display numeric values |
| `fmt`         | Format string for value labels (e.g., `{:.2f}`) |
| `show`        | If `False`, returns Axes without displaying |

**Why it matters:**  
Students can quickly learn plotting concepts without memorizing seaborn/matplotlib boilerplate, while instructors can demonstrate clarity by showing values directly on charts.

---

## bar_plot

```python
bar_plot(data, x, y, title=None, show_values="no", fmt="{:.1f}", show=True)
```

### Example

```python
from quicklearnkit import bar_plot
import seaborn as sns

df = sns.load_dataset("tips")

bar_plot(df, x="day", y="total_bill", show_values="yes")
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

Displays mean values when `show_values="yes"`.

```python
box_plot(data, x=None, y=None, title=None, show_values="no", fmt="{:.2f}", show=True)
```

---

## hist_plot

Displays bin counts when `show_values="yes"`.

```python
hist_plot(data, x, bins=10, title=None, show_values="no", fmt="{:.0f}", show=True)
```

---

## Customization Example

Because all functions return a `matplotlib.Axes` object, you can customize further:

```python
ax = bar_plot(df, x="day", y="total_bill", show_values="yes", show=False)

ax.set_xlabel("Day of Week")
ax.set_ylabel("Average Bill")
ax.set_ylim(0, 40)

import matplotlib.pyplot as plt
plt.show()
```

**Why it matters:**  
Learners get the simplicity of QuickLearnKit wrappers, but advanced users retain full matplotlib control for professional-quality plots.

---

## Design Intent

Visualization wrappers are designed to:

- Help students **see numeric values clearly**  
- Reduce repetitive plotting code  
- Maintain compatibility with standard matplotlib workflows  
- Simplify — but never restrict — customization  

---

✨ **In short:** QuickLearnKit visualization tools make plots **teaching-ready out of the box**. They balance simplicity for beginners with flexibility for advanced users, ensuring clarity without sacrificing control.

