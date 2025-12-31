# Stat Card

Stat cards are used on dashboards and reports to highlight key metrics. They typically include a title, a value, an optional icon, and a trend indicator (up/down).

---

## Quick Start

```python
from faststrap import StatCard

StatCard(
    label="Total Revenue",
    value="$45,231.89",
    icon="currency-dollar",
    trend="+20.1%",
    trend_variant="success"
)
```

<div class="result" markdown>
![Screenshot: Card with dollar icon, revenue number, and green trend text](../../assets/images/stat-card-basic.png)
</div>

---

## Visual Examples & Use Cases

### 1. Negative Trends
Use `trend_variant="danger"` for decreases in metrics.

!!! note "Code & Output"
    ```python
    StatCard(
        label="Active Users",
        value="1,234",
        trend="-5%",
        trend_label="from last month",
        trend_variant="danger",
        icon="people"
    )
    ```

### 2. Branding (Variants)
Apply color to the icon or card borders using the `variant` argument.

!!! note "Code & Output"
    ```python
    StatCard(..., variant="primary", bg_variant="soft-primary")
    ```

---

## Parameter Reference

| FastStrap Param | Type | Description |
| :--- | :--- | :--- |
| `label` | `str` | Title of the metric (e.g. "Total Sales"). |
| `value` | `str | int` | The main display number or value. |
| `icon` | `str` | Bootstrap icon name. |
| `trend` | `str` | Percentage or text indicating change (e.g. "+12%"). |
| `trend_label` | `str` | Context for the trend (e.g. "since yesterday"). |
| `trend_variant` | `str` | Color of trend text: `success`, `danger`, `warning`. |
| `variant` | `str` | Color theme for the icon/label. |

::: faststrap.components.display.stat_card.StatCard
    options:
        show_source: true
        heading_level: 4
