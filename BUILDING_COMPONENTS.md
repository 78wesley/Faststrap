# Building FastStrap Components - Complete Guide

**For contributors, LLMs, and developers building new components.**

---

## 🎯 Quick Start (30 seconds)

1. Copy an existing component from `src/faststrap/components/` as template
2. Follow the patterns below
3. Add tests to `tests/test_components/`
4. Submit PR

**Best templates to copy:**
- Simple component: `badge.py`
- Complex component: `card.py`
- Interactive (Bootstrap JS): `modal.py`

---

## 📋 Component Checklist

Before submitting, ensure:

- [ ] File in correct directory (`forms/`, `display/`, `feedback/`, `navigation/`, `layout/`)
- [ ] Function uses Python 3.10+ type hints (`str | None` not `Optional[str]`)
- [ ] Includes `_convert_attrs()` helper for HTMX support
- [ ] Uses `merge_classes()` from `core.base` for CSS
- [ ] Comprehensive docstring with examples
- [ ] Test file with 8-15 tests
- [ ] Exported in `__init__.py` files
- [ ] Works with `to_xml()` (not just `str()`)

---

## 🏗️ Component Structure Template

```python
"""Bootstrap [ComponentName] for [purpose]."""

from typing import Any, Literal

from fasthtml.common import Div  # Or appropriate FT type

from ...core.base import merge_classes

# Type aliases
VariantType = Literal["primary", "secondary", "success", "danger", "warning", "info", "light", "dark"]


def _convert_attrs(kwargs: dict[str, Any]) -> dict[str, Any]:
    """Convert hx_get → hx-get, data_id → data-id, aria_label → aria-label."""
    converted = {}
    for k, v in kwargs.items():
        if k.startswith("hx_") or k.startswith("data_") or k.startswith("aria_"):
            converted[k.replace("_", "-")] = v
        elif k == "cls":
            converted[k] = v
        else:
            converted[k.replace("_", "-")] = v
    return converted


def ComponentName(
    *children: Any,
    variant: VariantType = "primary",
    **kwargs: Any,
) -> Div:
    """Bootstrap [ComponentName] component.

    Args:
        *children: Component content
        variant: Bootstrap color variant
        **kwargs: Additional HTML attributes (cls, id, hx-*, data-*, etc.)

    Returns:
        FastHTML Div element

    Example:
        Basic:
        >>> ComponentName("Content", variant="success")

        With HTMX:
        >>> ComponentName("Load", hx_get="/api", hx_target="#result")

        Custom styling:
        >>> ComponentName("Custom", cls="mt-3 shadow")

    See Also:
        Bootstrap docs: https://getbootstrap.com/docs/5.3/components/[name]/
    """
    # Build classes
    classes = ["component-base", f"component-{variant}"]

    # Merge with user classes
    user_cls = kwargs.pop("cls", "")
    all_classes = merge_classes(" ".join(classes), user_cls)

    # Build attributes
    attrs: dict[str, Any] = {"cls": all_classes}
    attrs.update(_convert_attrs(kwargs))

    return Div(*children, **attrs)
```

---

## 🔧 Critical Patterns

### 1. **Type Hints (Python 3.10+)**

```python
# ✅ CORRECT
from typing import Any, Literal

def Component(
    *children: Any,
    size: Literal["sm", "lg"] | None = None,
    **kwargs: Any
) -> Div:
    ...

# ❌ WRONG (old style)
from typing import Optional, Union

def Component(
    size: Optional[Union[str, None]] = None
) -> Div:
    ...
```

### 2. **Class Merging**

```python
from ...core.base import merge_classes

# Always merge user classes
user_cls = kwargs.pop("cls", "")
all_classes = merge_classes("btn btn-primary", user_cls)
```

### 3. **HTMX Attribute Conversion**

```python
# Always include _convert_attrs() function
attrs.update(_convert_attrs(kwargs))

# This allows:
Button("Save", hx_post="/save", hx_target="#result")
# To become: <button hx-post="/save" hx-target="#result">Save</button>
```

### 4. **Bootstrap Variants**

```python
# Standard variants
VariantType = Literal[
    "primary", "secondary", "success", "danger",
    "warning", "info", "light", "dark"
]

# Apply as:
classes.append(f"btn-{variant}")  # OR
classes.append(f"text-bg-{variant}")  # For colored backgrounds
```

### 5. **Component IDs (Special Handling)**

If your component requires an `id` (like Modal, Drawer):

```python
def Modal(
    *children: Any,
    modal_id: str,  # ← Use custom param name, NOT "id"
    **kwargs: Any
) -> Div:
    # Build component first
    result = Div(*parts, **attrs)
    
    # Set id AFTER creation (bypasses FastHTML quirk)
    result.attrs['id'] = modal_id
    
    return result
```

**Why:** FastHTML's `str()` has a bug with `id` parameter. Use `modal_id`/`drawer_id`/etc.

---

## 🧪 Test File Template

```python
"""Tests for ComponentName."""

from fasthtml.common import to_xml  # ← IMPORTANT: Use to_xml(), not str()

from faststrap.components.category import ComponentName


def test_component_basic():
    """Component renders correctly."""
    comp = ComponentName("Test")
    html = to_xml(comp)  # ← Use to_xml()
    
    assert "Test" in html
    assert "component-base" in html


def test_component_variants():
    """Component supports all variants."""
    variants = ["primary", "secondary", "success", "danger"]
    
    for variant in variants:
        comp = ComponentName("Test", variant=variant)
        html = to_xml(comp)
        assert f"component-{variant}" in html


def test_component_custom_classes():
    """Component merges custom classes."""
    comp = ComponentName("Test", cls="custom-class mt-3")
    html = to_xml(comp)
    
    assert "component-base" in html
    assert "custom-class" in html
    assert "mt-3" in html


def test_component_htmx():
    """Component supports HTMX."""
    comp = ComponentName("Load", hx_get="/api", hx_target="#result")
    html = to_xml(comp)
    
    assert 'hx-get="/api"' in html
    assert 'hx-target="#result"' in html


def test_component_data_attributes():
    """Component handles data attributes."""
    comp = ComponentName("Test", data_id="123", data_type="info")
    html = to_xml(comp)
    
    assert 'data-id="123"' in html
    assert 'data-type="info"' in html
```

**CRITICAL:** Always use `to_xml(component)`, **never** `str(component)` due to FastHTML bug.

---

## 📁 File Structure

```
src/faststrap/components/
├── display/          # Visual elements (Badge, Card, Avatar)
│   ├── __init__.py
│   └── component.py
├── feedback/         # User feedback (Alert, Toast, Modal)
├── forms/            # Form inputs (Button, Input, Select)
├── layout/           # Layout helpers (Container, Row, Col)
└── navigation/       # Navigation (Navbar, Tabs, Breadcrumb)

tests/test_components/
└── test_component.py
```

---

## 🎨 Bootstrap Component Reference

When building a component, reference Bootstrap docs:

**Base URL:** `https://getbootstrap.com/docs/5.3/components/[name]/`

**Key classes to know:**
- Variants: `btn-primary`, `alert-success`, `text-bg-danger`
- Sizes: `btn-sm`, `btn-lg`, `form-control-lg`
- States: `disabled`, `active`, `show`, `fade`
- Utilities: `d-flex`, `gap-2`, `mt-3`, `shadow`

---

## 🚀 Component Priority List

### **Phase 2 (Next):**
1. Tabs
2. Dropdown
3. Input (text, email, password)
4. Select
5. Breadcrumb
6. Pagination
7. Spinner
8. Progress

### **Phase 3:**
9. Table
10. Accordion
11. Carousel
12. ListGroup
13. Tooltip
14. Popover
15. Checkbox/Radio/Switch
16. Range
17. FileInput
18. FormValidation

---

## 💡 Tips for LLMs

When asking an LLM to build a component:

**Good prompt:**
> "Build the Tabs component for FastStrap following BUILDING_COMPONENTS.md. Use Badge.py as template. Include nav-tabs, nav-pills, and content panes. Add 10 tests using to_xml(). Reference: https://getbootstrap.com/docs/5.3/components/navs-tabs/"

**Include:**
- This guide
- An existing component as reference
- Bootstrap docs link
- Specific test count

---

## 🤝 Getting Help

- **Questions:** Open GitHub Discussion
- **Bugs:** Open GitHub Issue
- **PRs:** We review within 48 hours
- **Discord:** Join FastHTML community

---

## ✅ Submission Checklist

Before submitting PR:

```bash
# 1. Run tests
pytest tests/test_components/test_yourcomponent.py -v

# 2. Check coverage
pytest --cov=faststrap.components.category.yourcomponent

# 3. Type check
mypy src/faststrap/components/category/yourcomponent.py

# 4. Format
black src/faststrap/components/category/yourcomponent.py
ruff check src/faststrap/components/category/yourcomponent.py

# 5. Test example
python examples/demo_yourcomponent.py
```

All checks pass? Submit PR! 🎉

---

**Ready to build? Pick a component from Phase 2 and start coding!**