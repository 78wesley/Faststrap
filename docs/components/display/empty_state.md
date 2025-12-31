# Empty State

The `EmptyState` component provides a visual placeholder for when data is missing or a user hasn't completed an action yet. It usually contains an icon, a title, a description, and a call-to-action button.

---

## Quick Start

```python
from faststrap import EmptyState, Button

EmptyState(
    title="No items found",
    description="You haven't added any items to your collection yet.",
    icon="search",
    action=Button("Add First Item", variant="primary")
)
```

<div class="result" markdown>
![Screenshot: Centered icon, title, text, and button](../../assets/images/empty-state-basic.png)
</div>

---

## Visual Examples & Use Cases

### 1. Dashboard Placeholders
Use inside cards or grids to signify empty data sets.

!!! note "Code & Output"
    ```python
    from faststrap import Card

    Card(
        EmptyState(
            title="No Activity",
            description="Log some activity to see it here.",
            icon="activity",
            variant="light"
        )
    )
    ```

---

## Parameter Reference

| FastStrap Param | Type | Description |
| :--- | :--- | :--- |
| `title` | `str` | Main bold heading. |
| `description` | `str` | Explanatory message. |
| `icon` | `str` | Bootstrap icon name. |
| `action` | `Any` | Call to action (usually a Button or Link). |
| `variant` | `str` | Color variant for the icon and title. |

::: faststrap.components.display.empty_state.EmptyState
    options:
        show_source: true
        heading_level: 4
