# Tooltip & Popover

Tooltips and Popovers provide small overlays of content on hover, click, or focus. They are essential for providing extra context without cluttering the UI.

!!! tip "Bootstrap Reference"
    [Bootstrap 5 Tooltips](https://getbootstrap.com/docs/5.3/components/tooltips/) & [Bootstrap 5 Popovers](https://getbootstrap.com/docs/5.3/components/popovers/)

---

## Quick Start (Tooltip)

```python
from faststrap import Tooltip, Button

Tooltip(
    Button("Hover Me", variant="secondary"),
    title="I am a tooltip!"
)
```

<div class="result" markdown>
![Screenshot: Mouse hovering over button shows a small black bubble above](../../assets/images/tooltip-basic.png)
</div>

---

## Quick Start (Popover)

Popovers are similar to tooltips but can contain a title and more complex content (usually triggered by click).

```python
from faststrap import Popover, Button

Popover(
    Button("Click Me", variant="primary"),
    title="Rich Details",
    content="This is more detailed information inside a popover."
)
```

<div class="result" markdown>
![Screenshot: Clicked button shows a larger card with title and content](../../assets/images/popover-basic.png)
</div>

---

## Visual Examples & Use Cases

### 1. Positioning
Use the `placement` argument to control where the overlay appears.

!!! note "Code & Output"
    ```python
    Tooltip(Button("Top"), title="On top", placement="top")
    Tooltip(Button("Right"), title="On right", placement="right")
    Tooltip(Button("Bottom"), title="On bottom", placement="bottom")
    Tooltip(Button("Left"), title="On left", placement="left")
    ```

### 2. Activation Triggers
Tooltips usually trigger on `hover`, but you can change this to `focus` or `click`.

```python
# Only shows when the input field is focused (tabbed into)
Tooltip(Input(placeholder="Type..."), title="Help text", trigger="focus")
```

---

## Practical Functionality

### 1. Automatic Initialization
In standard Bootstrap, you must manually run JavaScript to enable tooltips. **FastStrap handles this for you** automatically using a global initialization script that targets any element with `data-bs-toggle="tooltip"` or `"popover"`.

---

## Parameter Reference

### Tooltip
| Param | Type | Description |
| :--- | :--- | :--- |
| `title` | `str` | The text content of the tooltip. |
| `placement` | `str` | `top`, `bottom`, `left`, `right`, `auto`. |
| `trigger` | `str` | `hover`, `focus`, `click`, `manual`. |
| `animation` | `bool` | Default `True`. Enables CSS fade. |

### Popover
| Param | Type | Description |
| :--- | :--- | :--- |
| `title` | `str` | The header of the popover. |
| `content` | `str` | The body text of the popover. |
| `placement` | `str` | Same as tooltip. |
| `trigger` | `str` | Default is `click`. |
| `dismissible` | `bool` | If `True`, closes when the user clicks anywhere else. |

::: faststrap.components.feedback.overlays.Tooltip
    options:
        heading_level: 4

::: faststrap.components.feedback.overlays.Popover
    options:
        heading_level: 4
