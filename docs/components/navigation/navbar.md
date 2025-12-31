# Navbar

The `Navbar` is a responsive meta-component that serves as a navigation header for your application. It supports branding, links, dropdowns, and forms (like search).

!!! tip "Bootstrap Reference"
    [Bootstrap 5 Navbar](https://getbootstrap.com/docs/5.3/components/navbar/)

---

## Quick Start

```python
from faststrap import Navbar, NavbarBrand, NavItem

Navbar(
    NavbarBrand("🚀 FastStrap", href="/"),
    NavItem("Home", href="/"),
    NavItem("Docs", href="/docs"),
    NavItem("Pricing", href="/pricing"),
    expand="lg",
    variant="dark",
    bg_variant="primary"
)
```

<div class="result" markdown>
![Screenshot: Responsive blue navbar with home/docs link](../../assets/images/navbar-basic.png)
</div>

---

## Visual Examples & Use Cases

### 1. Positioning & Sticky
Keep the navigation visible while scrolling using `sticky="top"` or `fixed="top"`.

```python
Navbar(..., sticky="top") # Pushes content down
Navbar(..., fixed="top")  # Floats over content
```

### 2. Dark vs Light Themes
Match your application's aesthetic.

!!! note "Code & Output"
    ```python
    # Dark brand: Primary background, light text
    Navbar(..., variant="dark", bg_variant="primary")
    
    # Light brand: Light background, dark text
    Navbar(..., variant="light", bg_variant="light")
    ```

### 3. Adding a Search Form
Navbars are common places for search inputs.

!!! note "Code & Output"
    ```python
    from faststrap import Form, Input, Button

    Navbar(
        NavbarBrand("My App"),
        Form(
            Input(placeholder="Search...", size="sm", cls="me-2"),
            Button("Search", variant="outline-success", size="sm"),
            cls="d-flex"
        ),
        expand="md"
    )
    ```

---

## Technical Hierarchy (LLM Spec)

To build a correct Navbar, follow this nested structure:

1.  **Navbar** (Main Container)
    *   **Container** (Optional, for centered alignment)
        *   **NavbarBrand** (Text or Logo)
        *   **NavbarToggler** (Created automatically if `expand` is set)
        *   **NavbarCollapse** (Parent for menu items)
            *   **NavItem** (Single Link)
            *   **Dropdown** (Grouped Links)

---

## Parameter Reference

| FastStrap Param | Type | Bootstrap Class | Description |
| :--- | :--- | :--- | :--- |
| `expand` | `str` | `.navbar-expand-{val}` | Responsive breakpoint: `sm`, `md`, `lg`, `xl`. |
| `variant` | `str` | `.navbar-{variant}` | Text contrast: `light` (dark text) or `dark` (light text). |
| `bg_variant` | `str` | `.bg-{variant}` | Background color (e.g., `primary`, `white`). |
| `sticky` | `str` | `.sticky-top` | Position style. |
| `fixed` | `str` | `.fixed-top` | Floating position style. |

::: faststrap.components.navigation.navbar.Navbar
    options:
        show_source: false
        heading_level: 4
