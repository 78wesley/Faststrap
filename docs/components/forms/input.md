# Input

The `Input` component allows users to enter text, numbers, passwords, emails, and more. It wraps the standard HTML `<input>` element with comprehensive Bootstrap styling, validation states, and floating labels.

!!! tip "Bootstrap Reference"
    [Bootstrap 5 Form Controls Documentation](https://getbootstrap.com/docs/5.3/forms/form-control/)

---

## Quick Start

```python
from faststrap import Input

# A simple text input
Input(placeholder="Enter your name", label="Full Name")
```

<div class="result" markdown>
![Screenshot: Basic Input with Label](../assets/images/input-basic.png){ width=300 }
</div>

---

## Visual Examples & Use Cases

### 1. Types & Labels
FastStrap supports all HTML5 input types. Adding a `label` argument automatically creates a properly accessible `<label>` associated with the input.

!!! note "Code & Output"
    ```python
    Input(type="email", label="Email Address", placeholder="name@example.com")
    Input(type="password", label="Password")
    Input(type="color", label="Choose Color", value="#563d7c")
    ```
    <div class="result" markdown>
    ![Screenshot: Email input, Password input, Color picker](../assets/images/input-types.png)
    </div>

### 2. Sizing
Match inputs to buttons or other components using `size`.

!!! note "Code & Output"
    ```python
    Input(placeholder="Large Input", size="lg")
    Input(placeholder="Default Input")
    Input(placeholder="Small Input", size="sm")
    ```
    <div class="result" markdown>
    ![Screenshot: Large, Default, and Small inputs](../assets/images/input-sizes.png)
    </div>

### 3. Utility Text and Disabled State
Add flexible helper text below the input using `help_text`. Use `disabled` or `readonly` to restrict interaction.

!!! note "Code & Output"
    ```python
    Input(
        label="Username", 
        help_text="Must be 8-20 characters long.",
        disabled=True,
        value="jdoe_archived"
    )
    ```
    <div class="result" markdown>
    ![Screenshot: Disabled input with help text below it](../assets/images/input-disabled.png)
    </div>

---

## Practical Functionality

### 1. Validation States
Communicate success or error states vividly. This is critical for form feedback.

```python
# Valid state (Green border + checkmark)
Input("valid_user", class="is-valid", value="Correct!")

# Invalid state (Red border + warning icon)
Input("invalid_csv", class="is-invalid", value="Invalid data")
```

### 2. Floating Labels
Bootstrap's modern "Floating Label" pattern moves the label *inside* the input, floating up when the user types.

```python
from faststrap import FloatingLabel

FloatingLabel(
    Input("email", placeholder="name@example.com"),
    label="Email Address"
)
```
<div class="result" markdown>
![Animation: Label floating up when input is focused](../assets/videos/input-floating.gif)
</div>

### 3. HTMX Integration
Trigger server requests on user input (e.g., live search).

```python
Input(
    type="search",
    placeholder="Search users...",
    hx_get="/search_users",
    hx_trigger="keyup changed delay:500ms", # Wait 500ms after typing stops
    hx_target="#search-results"
)
```

---

## Advanced Customization

### 1. CSS Variables
Customize standard form colors and spacing.

| CSS Variable | Description |
| :--- | :--- |
| `--bs-body-bg` | Background color of input. |
| `--bs-body-color` | Text color. |
| `--bs-border-color` | Default border color. |
| `--bs-focus-ring-color` | Glow color when focused. |

### 2. Input Groups
Combine inputs with text or buttons using `InputGroup`.

```python
from faststrap import InputGroup, InputGroupText

InputGroup(
    InputGroupText("@"),
    Input(placeholder="Username"),
    InputGroupText(".com")
)
```

---

## Parameter Reference

| FastStrap Param | Type | Bootstrap / HTML Attribute | Description |
| :--- | :--- | :--- | :--- |
| `type` | `str` | `type="..."` | HTML5 Input type (`text`, `password`, `email`, `number`, `date`, etc.). Default `text`. |
| `label` | `str` | `<label>` | Text for the associated label element. |
| `placeholder` | `str` | `placeholder="..."` | Ghost text shown when empty. |
| `value` | `Any` | `value="..."` | Initial value of the input. |
| `help_text` | `str` | `.form-text` | Helper text displayed below the input. |
| `size` | `str` | `.form-control-{size}` | Size: `sm` or `lg`. |
| `disabled` | `bool` | `disabled` | Disables interaction. |
| `readonly` | `bool` | `readonly` | Value is visible but not editable. |
| `required` | `bool` | `required` | analyzing browser validation. |

::: faststrap.components.forms.input.Input
    options:
        show_source: true
        heading_level: 4
