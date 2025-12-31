# Tabs & Pills

Use tabs and pills to navigate between different views or panes of content within the same page.

!!! tip "Bootstrap Reference"
    [Bootstrap 5 Navs & Tabs](https://getbootstrap.com/docs/5.3/components/navs-tabs/)

---

## Quick Start

Tabs require a list of `NavItem` objects and a list of `TabPane` objects. FastStrap simplifies this with the `Tabs` component.

```python
from faststrap import Tabs, TabPane

Tabs(
    TabPane("This is Content A", label="Profile"),
    TabPane("This is Content B", label="Settings"),
    TabPane("This is Content C", label="Security")
)
```

<div class="result" markdown>
![Screenshot: Tab navigation with Profile/Settings/Security items](../../assets/images/tabs-basic.png)
</div>

---

## Visual Examples & Use Cases

### 1. Pills Variant
Pills look like rounded buttons and are often used for filtering or sub-navigation.

!!! note "Code & Output"
    ```python
    Tabs(..., pills=True)
    ```
    <div class="result" markdown>
    ![Screenshot: Navigation pills instead of tabs](../../assets/images/tabs-pills.png)
    </div>

### 2. Vertical Alignment
For sidebar-style navigation, you can stack the nav items vertically.

!!! note "Code & Output"
    ```python
    Tabs(..., vertical=True)
    ```

### 3. HTMX Content Loading
Load tab content only when it's clicked to save initial page load time.

```python
Tabs(
    TabPane(
        Div(hx_get="/api/user-stats", hx_trigger="load"), # Loads on click
        label="Analytics"
    )
)
```

---

## Components Map

| Component | Responsibility |
| :--- | :--- |
| `Tabs` | The main container that handles switching logic. |
| `TabPane` | A single container of content. Use the `label` argument to define the tab text. |

---

## Parameter Reference

| FastStrap Param | Type | Bootstrap Class | Description |
| :--- | :--- | :--- | :--- |
| `pills` | `bool` | `.nav-pills` | Switches from underlined tabs to rounded pills. |
| `vertical` | `bool` | `.flex-column` | Aligns items vertically. |
| `fade` | `bool` | `.fade` | Adds transition animation when switching. |
| `fill` | `bool` | `.nav-fill` | Proportionally fills the entire width. |
| `justified` | `bool` | `.nav-justified` | Every item has the exact same width. |

::: faststrap.components.navigation.tabs.Tabs
    options:
        show_source: false
        heading_level: 4
