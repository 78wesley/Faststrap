# Table

The `Table` component enables you to display tabular data efficiently. FastStrap's implementation decomposes the table into semantic sub-components (`THead`, `TBody`, `TRow`, `TCell`) for maximum flexibility, while providing high-level arguments for common styles like striping and hover effects.

!!! tip "Bootstrap Reference"
    [Bootstrap 5 Tables](https://getbootstrap.com/docs/5.3/content/tables/)

---

## Quick Start

```python
from faststrap import Table, THead, TBody, TRow, TCell

Table(
    THead(TRow(TCell("ID"), TCell("Name"), TCell("Role"))),
    TBody(
        TRow(TCell("1"), TCell("Alice"), TCell("Admin")),
        TRow(TCell("2"), TCell("Bob"), TCell("User")),
    ),
    striped=True, hover=True
)
```

<div class="result" markdown>
![Screenshot: Striped table with 2 rows](../assets/images/table-basic.png){ width=400 }
</div>

---

## Styling Options

FastStrap exposes Bootstrap's powerful table modifiers as simple boolean arguments.

### 1. Variants & Themes
Use `variant` to color the entire table, or set `striped` / `hover` for readability.

!!! note "Code & Output"
    ```python
    # Dark Mode Table
    Table(..., variant="dark", striped=True)
    
    # Borderless
    Table(..., borderless=True)
    
    # Small / Compact
    Table(..., small=True)
    ```

### 2. Responsiveness
Tables can overflow on small screens. Wrap them in a responsive container automatically using the `responsive` argument.

```python
# Enables horizontal scrolling on small devices
Table(..., responsive=True) # or responsive="sm", "md", "lg"
```

---

## API Reference

::: faststrap.components.display.table.Table
    options:
        show_source: true
        heading_level: 4
