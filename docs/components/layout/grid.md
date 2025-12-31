# Grid System

Bootstrap's grid system uses a series of containers, rows, and columns to layout and align content. It's built with flexbox and is fully responsive. FastStrap mirrors this with `Container`, `Row`, and `Col`.

!!! tip "Bootstrap Reference"
    [Bootstrap 5 Grid System Documentation](https://getbootstrap.com/docs/5.3/layout/grid/)

---

## Quick Start

The grid follows a 12-column system.

```python
from faststrap import Container, Row, Col

Container(
    Row(
        Col("Left Column", width=4),   # 4/12 width
        Col("Center Column", width=4), # 4/12 width
        Col("Right Column", width=4)   # 4/12 width
    )
)
```

<div class="result" markdown>
![Screenshot: A three-column layout with equal widths](../../assets/images/grid-basic.png)
</div>

---

## Visual Examples & Use Cases

### 1. Responsive Breakpoints
You can specify different widths for different screen sizes (sm, md, lg, xl, xxl).

!!! note "Code & Output"
    ```python
    # 1 column on mobile, 2 on tablet, 3 on desktop
    Row(
        Col("Item 1", width=12, md=6, lg=4),
        Col("Item 2", width=12, md=6, lg=4),
        Col("Item 3", width=12, md=12, lg=4)
    )
    ```

### 2. Alignment & Spacing (Gutter)
Bootstrap's Flexbox utilities are available through the `Row` and `Col` arguments.

!!! note "Code & Output"
    ```python
    # Centered Row with gap (gutter) level 4
    Row(
        Col("I am centered", width=6),
        justify="center",
        gutter=4
    )
    ```

### 3. Container Fluid
By default, `Container` has a fixed width that changes at each breakpoint. Use `fluid=True` for a container that is always 100% wide.

```python
Container("Full width content", fluid=True)
```

---

## Practical Functionality

### 1. Auto-width Columns
If you don't specify a width, `Col` will automatically share the space with other sibling columns.

```python
Row(
    Col("Variable width"),
    Col("Variable width"),
    Col("Variable width")
)
```

### 2. Offsetting Columns
Move columns to the right using `offset`.

```python
Row(
    Col("Centered offset", width=6, offset=3)
)
```

---

## Parameter Reference

### Container
| Param | Type | Bootstrap Class | Description |
| :--- | :--- | :--- | :--- |
| `fluid` | `bool` | `.container-fluid` | Spans the full width of the viewport. |

### Row
| Param | Type | Bootstrap Class | Description |
| :--- | :--- | :--- | :--- |
| `gutter` | `int` | `.g-{val}` | Spacing between columns (0-5). |
| `gx` | `int` | `.gx-{val}` | Horizontal gutter only. |
| `gy` | `int` | `.gy-{val}` | Vertical gutter only. |
| `justify` | `str` | `.justify-content-{val}` | Alignment: `start`, `center`, `end`, `around`, `between`. |
| `align` | `str` | `.align-items-{val}` | Vertical alignment: `start`, `center`, `end`. |

### Col
| Param | Type | Bootstrap Class | Description |
| :--- | :--- | :--- | :--- |
| `width` | `int` | `.col-{val}` | Mobile/default width (1-12). |
| `sm` | `int` | `.col-sm-{val}` | Tablet width. |
| `md` | `int` | `.col-md-{val}` | Desktop width. |
| `lg` | `int` | `.col-lg-{val}` | Large screen width. |
| `offset` | `int` | `.offset-{val}` | Prepend empty columns. |

::: faststrap.components.layout.grid.Container
    options:
        heading_level: 4

::: faststrap.components.layout.grid.Row
    options:
        heading_level: 4

::: faststrap.components.layout.grid.Col
    options:
        heading_level: 4
