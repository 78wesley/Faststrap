# Alert

Alerts provide contextual feedback messages for typical user actions with a handful of available and flexible alert messages.

!!! tip "Bootstrap Reference"
    [Bootstrap 5 Alerts](https://getbootstrap.com/docs/5.3/components/alerts/)

---

## Quick Start

```python
from faststrap import Alert

# A simple success alert
Alert("Your profile has been updated!", variant="success")
```

<div class="result" markdown>
![Screenshot: Green success alert](../../assets/images/alert-basic.png){ width=500 }
</div>

---

## Visual Examples & Use Cases

### 1. Dismissible Alerts
Allow users to close the alert. This is handled automatically by Bootstrap's JS via FastStrap's `dismissible=True`.

!!! note "Code & Output"
    ```python
    Alert(
        "Important: Your session expires in 5 minutes.", 
        variant="warning", 
        dismissible=True
    )
    ```
    <div class="result" markdown>
    ![Screenshot: Warning alert with a 'X' close button](../../assets/images/alert-dismissible.png)
    </div>

### 2. Rich Content
Alerts can contain headings, links, and multiple paragraphs.

!!! note "Code & Output"
    ```python
    from fasthtml.common import H4, P, Hr, A

    Alert(
        H4("Well done!", cls="alert-heading"),
        P("Aww yeah, you successfully read this important alert message."),
        Hr(),
        P("Whenever you need to, be sure to use margin utilities to keep things nice and tidy."),
        variant="success"
    )
    ```
    <div class="result" markdown>
    ![Screenshot: Large success alert with heading and paragraphs](../../assets/images/alert-rich.png)
    </div>

### 3. Icons
Adding icons to alerts significantly improves user recognition of message status.

!!! note "Code & Output"
    ```python
    Alert(
        " An error occurred while saving.", 
        variant="danger", 
        icon="exclamation-triangle-fill"
    )
    ```
    <div class="result" markdown>
    ![Screenshot: Red danger alert with an exclamation icon](../../assets/images/alert-icon.png)
    </div>

---

## Practical Functionality

### 1. HTMX Integration (Auto-remove)
Commonly used for temporary notifications that should disappear after an HTMX update.

```python
# Alert is removed from DOM after being seen (requires custom JS or HTMX trick)
Alert(
    "Saved!", 
    variant="success", 
    hx_get="/clear_notification", 
    hx_trigger="load delay:3s" # Disappears after 3 seconds
)
```

---

## Advanced Customization

### 1. CSS Variables

| CSS Variable | Description |
| :--- | :--- |
| `--bs-alert-bg` | Background color. |
| `--bs-alert-color` | Text color. |
| `--bs-alert-border-color` | Border color. |
| `--bs-alert-padding-x` | Padding. |
| `--bs-alert-link-color` | Color for `<A>` tags inside. |

---

## Parameter Reference

| FastStrap Param | Type | Bootstrap Class | Description |
| :--- | :--- | :--- | :--- |
| `variant` | `str` | `.alert-{variant}` | Color theme. |
| `dismissible` | `bool` | `.alert-dismissible` | Adds a close button. |
| `icon` | `str` | - | Bootstrap icon name to prepend. |

::: faststrap.components.feedback.alert.Alert
    options:
        show_source: true
        heading_level: 4
