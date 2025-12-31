# Checkbox, Radio & Switch

These components allow users to select one or more options from a list. FastStrap provides `Checkbox` for multiple select, `Radio` for single select, and `Switch` for toggles.

!!! tip "Bootstrap Reference"
    [Bootstrap 5 Checks & Radios](https://getbootstrap.com/docs/5.3/forms/checks-radios/)

---

## Quick Start

```python
from faststrap import Checkbox, Radio, Switch

# Basic variants
Checkbox("subscribe", label="Subscribe to newsletter")
Radio("plan", value="monthly", label="Monthly Plan")
Switch("notifications", label="Enable Notifications")
```

<div class="result" markdown>
![Screenshot: Basic Checkbox, Radio, and Switch](../assets/images/checks-basic.png){ width=300 }
</div>

---

## Visual Examples & Use Cases

### 1. Grouping Radios
Radios share a `name` attribute to ensure only one can be selected at a time.

!!! note "Code & Output"
    ```python
    from faststrap import Div
    
    Div(
        Radio("shipping", value="standard", label="Standard Shipping (Free)", checked=True),
        Radio("shipping", value="express", label="Express Shipping ($10)"),
        Radio("shipping", value="overnight", label="Overnight ($25)")
    )
    ```
    <div class="result" markdown>
    ![Screenshot: List of 3 radio options](../assets/images/radios-group.png)
    </div>

### 2. Inline Layout
By default, checks stack vertically. Use `inline=True` to place them side-by-side.

!!! note "Code & Output"
    ```python
    Div(
        Checkbox("tag", value="python", label="Python", inline=True),
        Checkbox("tag", value="javascript", label="JavaScript", inline=True),
        Checkbox("tag", value="rust", label="Rust", inline=True)
    )
    ```
    <div class="result" markdown>
    ![Screenshot: Checkboxes arranged horizontally](../assets/images/checks-inline.png)
    </div>

### 3. Switches 
A `Switch` is simply a checkbox with a toggle slider appearance. It has the same API as `Checkbox`.

!!! note "Code & Output"
    ```python
    Switch("wifi", label="Wi-Fi", checked=True)
    Switch("bluetooth", label="Bluetooth")
    Switch("airplane", label="Airplane Mode", disabled=True)
    ```
    <div class="result" markdown>
    ![Screenshot: Toggle switches](../assets/images/switches.png)
    </div>

### 4. Button Style (Toggle Buttons) 
You can make checkboxes and radios look like push buttons using `btn_style=True`.

!!! note "Code & Output"
    ```python
    # Radio group looking like segmented control
    Div(
        Radio(
            "view", value="list", label="List View", 
            btn_style=True, variant="outline-primary", checked=True
        ),
        Radio(
            "view", value="grid", label="Grid View", 
            btn_style=True, variant="outline-primary"
        ),
        cls="btn-group"
    )
    ```
    <div class="result" markdown>
    ![Screenshot: Segmented button control](../assets/images/checks-buttons.png)
    </div>

---

## Parameter Reference (Common)

| FastStrap Param | Type | Bootstrap Class | Description |
| :--- | :--- | :--- | :--- |
| `name` | `str` | `name="..."` | Name for form submission. Radios with same name act as a group. |
| `value` | `str` | `value="..."` | Value submitted when checked. |
| `label` | `str` | `<label>` | Text displayed next to the control. |
| `checked` | `bool` | `checked` | Detailed initial state. |
| `inline` | `bool` | `.form-check-inline` | Displays control inline. |
| `reverse` | `bool` | `.form-check-reverse` | Puts label on left, input on right. |
| `switch` | `bool` | `.form-switch` | (Checkbox only) Renders as toggle switch. |
| `btn_style` | `bool` | `.btn-check` | Renders as a button instead of a native input. |

::: faststrap.components.forms.checks.Checkbox
    options:
        show_source: false
        heading_level: 4

::: faststrap.components.forms.checks.Radio
    options:
        show_source: false
        heading_level: 4
