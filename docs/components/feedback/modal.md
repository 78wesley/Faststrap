# Modal

Modals are "dialogs" that appear in front of the application content. They provide critical information, require user confirmation, or host complex forms.

!!! tip "Bootstrap Reference"
    [Bootstrap 5 Modals](https://getbootstrap.com/docs/5.3/components/modal/)

---

## Quick Start

Modals require a **Trigger** (usually a Button) and a **Modal Definition**.

```python
from faststrap import Modal, Button, Div

# 1. The Trigger
trigger = Button("Launch Modal", data_bs_toggle="modal", data_bs_target="#myModal")

# 2. The Modal
modal = Modal(
    "Hello! This is a modal dialog.", 
    title="Example Modal", 
    id="myModal",
    footer=Button("Save", variant="primary")
)
```

<div class="result" markdown>
![Video: Click button -> Modal fades in front of blurry background](../../assets/videos/modal-demo.gif)
</div>

---

## Visual Examples & Use Cases

### 1. Sizing
Specify the viewport width using `size`.

!!! note "Code & Output"
    ```python
    Modal(..., size="sm") # Small
    Modal(..., size="lg") # Large
    Modal(..., size="xl") # Extra Large
    Modal(..., size="fullscreen") # Full screen
    ```

### 2. Centered & Scrollable
Handle long content or improve ergonomics by centering the dialog.

!!! note "Code & Output"
    ```python
    Modal(
        "Lots of long text here...", 
        centered=True, 
        scrollable=True,
        title="Vertically Centered"
    )
    ```

### 3. Static Backdrop
Prevents closing the modal when clicking the shaded background. Useful for high-stakes forms or "must-read" alerts.

```python
Modal(..., backdrop="static")
```

---

## Practical Functionality

### 1. ConfirmDialog (Preset)
FastStrap provides a specialized `ConfirmDialog` for standard "Are you sure?" scenarios. It simplifies the API by pre-configuring the "Yes/No" buttons.

```python
from faststrap import ConfirmDialog

ConfirmDialog(
    "Delete this post? This cannot be undone.",
    title="Confirm Deletion",
    id="confirmDelete",
    confirm_text="Yes, Delete It",
    confirm_variant="danger",
    hx_delete="/post/1", # Action on confirm
    hx_target="#post-1"
)
```

### 2. Real-time Loading
You can put HTMX content inside a modal body to load data only when opened.

```python
Modal(
    Div(hx_get="/api/user_details", hx_trigger="intersect once"), # Loads when modal opens
    title="User Profile",
    id="profileModal"
)
```

---

## Parameter Reference

| FastStrap Param | Type | Bootstrap Attribute | Description |
| :--- | :--- | :--- | :--- |
| `title` | `str` | `.modal-title` | Text for the top header. |
| `footer` | `Any` | `.modal-footer` | Elements to put in bottom row. |
| `size` | `str` | `.modal-{size}` | `sm`, `lg`, `xl`, `fullscreen`. |
| `centered` | `bool` | `.modal-dialog-centered` | Vertically centers the dialog. |
| `scrollable` | `bool` | `.modal-dialog-scrollable` | Makes body scrollable independently. |
| `backdrop` | `str` | `data-bs-backdrop` | `static` prevents click-to-close. |
| `keyboard` | `bool` | `data-bs-keyboard` | If `False`, Escape key won't close it. |

::: faststrap.components.feedback.modal.Modal
    options:
        show_source: false
        heading_level: 4
