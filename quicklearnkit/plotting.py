import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


# ---------------- INTERNAL HELPER ---------------- #

def _add_value_labels(ax, fmt="{:.2f}", offset=(0, 3)):
    """
    Attach value labels to bars, line points, and scatter points.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Axes object containing the plot
    fmt : str
        Format string for values
    offset : tuple
        (x, y) pixel offset for annotations
    """
    # Bars (barplot, countplot, hist bars)
    for container in ax.containers:
        ax.bar_label(container, fmt=fmt, padding=3)

    # Lines / scatter points
    for line in ax.lines:
        x_data = line.get_xdata()
        y_data = line.get_ydata()

        for x, y in zip(x_data, y_data):
            if y is None or (isinstance(y, float) and np.isnan(y)):
                continue

            ax.annotate(
                fmt.format(y),
                (x, y),
                textcoords="offset points",
                xytext=offset,
                ha="center"
            )


def _show_flag(val):
    return str(val).lower() in ("yes", "y", "true", "1")


# ---------------- PUBLIC API ---------------- #

def bar_plot(
    data,
    x,
    y,
    title=None,
    show_values="no",
    fmt="{:.1f}",
    show=True
):
    """
    Draw a bar plot with optional value labels.

    Returns matplotlib Axes for further customization.
    """
    ax = sns.barplot(data=data, x=x, y=y)

    if title:
        ax.set_title(title)

    if _show_flag(show_values):
        _add_value_labels(ax, fmt=fmt)

    if show:
        plt.show()

    return ax


def line_plot(
    data,
    x,
    y,
    title=None,
    show_values="no",
    fmt="{:.2f}",
    show=True
):
    """
    Draw a line plot with optional value labels.

    Returns matplotlib Axes for further customization.
    """
    ax = sns.lineplot(data=data, x=x, y=y, marker="o")

    if title:
        ax.set_title(title)

    if _show_flag(show_values):
        _add_value_labels(ax, fmt=fmt)

    if show:
        plt.show()

    return ax


def scatter_plot(
    data,
    x,
    y,
    title=None,
    show_values="no",
    fmt="{:.2f}",
    show=True
):
    """
    Draw a scatter plot with optional value labels.

    Returns matplotlib Axes for further customization.
    """
    ax = sns.scatterplot(data=data, x=x, y=y)

    if title:
        ax.set_title(title)

    if _show_flag(show_values):
        _add_value_labels(ax, fmt=fmt)

    if show:
        plt.show()

    return ax


def count_plot(
    data,
    x,
    title=None,
    show_values="no",
    show=True
):
    """
    Draw a count plot with optional value labels.

    Returns matplotlib Axes for further customization.
    """
    ax = sns.countplot(data=data, x=x)

    if title:
        ax.set_title(title)

    if _show_flag(show_values):
        for container in ax.containers:
            ax.bar_label(container, padding=3)

    if show:
        plt.show()

    return ax


def box_plot(
    data,
    x=None,
    y=None,
    title=None,
    show_values="no",
    fmt="{:.2f}",
    show=True
):
    """
    Draw a box plot. If show_values is enabled, display mean value(s).

    Returns matplotlib Axes for further customization.
    """
    ax = sns.boxplot(data=data, x=x, y=y)

    if title:
        ax.set_title(title)

    if _show_flag(show_values):
        # Compute mean(s)
        if y:
            if x:
                means = data.groupby(x)[y].mean()
            else:
                means = [data[y].mean()]
        else:
            means = [data.mean(numeric_only=True).values[0]]

        for i, mean_val in enumerate(means):
            ax.annotate(
                f"Mean: {fmt.format(mean_val)}",
                (i, mean_val),
                textcoords="offset points",
                xytext=(0, 10),
                ha="center",
                color="red"
            )

    if show:
        plt.show()

    return ax


def hist_plot(
    data,
    x,
    bins=10,
    title=None,
    show_values="no",
    fmt="{:.0f}",
    show=True
):
    """
    Draw a histogram. If show_values is enabled, display bin counts.

    Returns matplotlib Axes for further customization.
    """
    ax = sns.histplot(data=data, x=x, bins=bins)

    if title:
        ax.set_title(title)

    if _show_flag(show_values):
        for patch in ax.patches:
            height = patch.get_height()
            if height > 0:
                ax.annotate(
                    fmt.format(height),
                    (patch.get_x() + patch.get_width() / 2, height),
                    ha="center",
                    va="bottom",
                    xytext=(0, 3),
                    textcoords="offset points"
                )

    if show:
        plt.show()

    return ax
