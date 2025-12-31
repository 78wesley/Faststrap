# Badge

Small, circular or pill-shaped indicators for status, counts, or labels. Badges scale to match the size of the immediate parent element by using relative font sizing and `em` units.

!!! tip "Bootstrap Reference"
    [Bootstrap 5 Badges](https://getbootstrap.com/docs/5.3/components/badge/)

---

## Quick Start

```python
from faststrap import Badge

# A simple primary badge
Badge("New", variant="primary")
```

<div class="result" markdown>
![Screenshot: A small blue 'New' badge](../../assets/images/badge-basic.png){ width=100 }
</div>

---

## Visual Examples & Use Cases

### 1. Variants
Like buttons, badges use semantic variants for meaning.

!!! note "Code & Output"
    ```python
    Badge("Success", variant="success")
    Badge("Danger", variant="danger")
    Badge("Warning", variant="warning", pill=True) # Rounded pill shape
    Badge("Light", variant="light", cls="text-dark") # Light needs dark text
    ```
    <div class="result" markdown>
    ![Screenshot: Badges in Green, Red, Yellow (Pill), and White](../../assets/images/badge-variants.png)
    </div>

### 2. Contextual Badges
Badges are often placed inside other components like Buttons or Headings.

!!! note "Code & Output"
    ```python
    from faststrap import Button, H1

    # Notification count in a button
    Button(
        "Notifications ", 
        Badge("99+", variant="light", pill=True), 
        variant="primary"
    )

    # Status in a heading
    H1("Documentation ", Badge("Beta", variant="info"))
    ```
    <div class="result" markdown>
    ![Screenshot: Button with '99+' badge and H1 with 'Beta' badge](../../assets/images/badge-contextual.png)
    </div>

---

## Practical Functionality

### 1. Indicators (Dot Style)
You can create "status dots" by using a Badge with no text and specific width/height.

```python
# A small 'Online' green dot
Badge(variant="success", rounded=True, style={"width": "10px", "height": "10px", "padding": "0"})
```

---

## Advanced Customization

### 1. CSS Variables
Customize standard badge colors.

| CSS Variable | Description | Default |
| :--- | :--- | :--- |
| `--bs-badge-padding-x` | Horizontal padding. | `.65em` |
| `--bs-badge-padding-y` | Vertical padding. | `.35em` |
| `--bs-badge-font-size` | Text size. | `.75em` |
| `--bs-badge-font-weight` | Boldness. | `700` |
| `--bs-badge-border-radius` | Corner roundness. | `var(--bs-border-radius)` |

---

## Parameter Reference

| FastStrap Param | Type | Bootstrap Class | Description |
| :--- | :--- | :--- | :--- |
| `variant` | `str` | `.text-bg-{variant}` | Color theme. |
| `pill` | `bool` | `.rounded-pill` | Fully rounded edges. |
| `rounded` | `bool` | `.rounded-circle` | Perfect circle (if width=height). |

::: faststrap.components.display.badge.Badge
    options:
        show_source: true
        heading_level: 4
