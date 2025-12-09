# FastStrap

**Modern Bootstrap 5 components for FastHTML - Build beautiful web UIs in pure Python with zero JavaScript knowledge.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![FastHTML](https://img.shields.io/badge/FastHTML-0.6+-green.svg)](https://fastht.ml/)
[![PyPI version](https://img.shields.io/pypi/v/faststrap.svg)](https://pypi.org/project/faststrap/)
[![Tests](https://github.com/Evayoung/Faststrap/workflows/Tests/badge.svg)](https://github.com/Evayoung/Faststrap/actions)

---

## Why FastStrap?

FastHTML is amazing for building web apps in pure Python, but it lacks pre-built UI components. FastStrap fills that gap by providing:

✅ **12+ Bootstrap components** - Buttons, Cards, Modals, Navbars, Forms, and more  
✅ **Zero JavaScript knowledge required** - Components just work  
✅ **No build steps** - Pure Python, no npm/webpack/vite  
✅ **Full HTMX integration** - Dynamic updates without page reloads  
✅ **Dark mode built-in** - Automatic theme switching  
✅ **Type-safe** - Full type hints for better IDE support  
✅ **Pythonic API** - Kwargs style that feels natural

---

## Quick Start

### Installation

```bash
pip install faststrap
```

### Hello World

```python
from fasthtml.common import FastHTML, serve
from faststrap import add_bootstrap, Card, Button

app = FastHTML()
add_bootstrap(app, theme="dark")

@app.route("/")
def home():
    return Card(
        "Welcome to FastStrap! Build beautiful UIs in pure Python.",
        header="Hello World 👋",
        footer=Button("Get Started", variant="primary")
    )

serve()
```

That's it! You now have a modern, responsive web app with zero JavaScript.

---

## Core Concepts

### 1. Adding Bootstrap to Your App

```python
from fasthtml.common import FastHTML
from faststrap import add_bootstrap

app = FastHTML()

# Basic setup
add_bootstrap(app)

# With dark theme
add_bootstrap(app, theme="dark")

# Using CDN (default is local assets)
add_bootstrap(app, use_cdn=True)
```

### 2. Using Components

All components follow Bootstrap's conventions with Pythonic names:

```python
from faststrap import Button, Badge, Alert, Card, Modal

# Button with variants
Button("Click me", variant="primary", size="lg")

# Alert with icon
Alert("Success!", variant="success", dismissible=True)

# Card with header and footer
Card(
    "Main content here",
    header="Card Title",
    footer=Button("Action")
)
```

### 3. HTMX Integration

All components support HTMX attributes for dynamic behavior:

```python
Button(
    "Load More",
    variant="primary",
    hx_get="/api/items",
    hx_target="#items",
    hx_swap="beforeend"
)
```

### 4. Responsive Grid System

```python
from faststrap import Container, Row, Col

Container(
    Row(
        Col("Left column", cols=12, md=6, lg=4),
        Col("Middle column", cols=12, md=6, lg=4),
        Col("Right column", cols=12, md=12, lg=4)
    )
)
```

---

## Available Components

### ✅ Phase 1 (v0.1.0 - v0.2.1)

| Component | Description | Status |
|-----------|-------------|--------|
| **Button** | Buttons with variants, sizes, loading states | ✅ |
| **ButtonGroup** | Grouped buttons and toolbars | ✅ |
| **Badge** | Status indicators and labels | ✅ |
| **Card** | Content containers with headers/footers | ✅ |
| **Alert** | Dismissible alerts with variants | ✅ |
| **Modal** | Dialog boxes and confirmations | ✅ |
| **Drawer** | Offcanvas side panels | ✅ |
| **Toast** | Auto-dismiss notifications | ✅ |
| **Navbar** | Responsive navigation bars | ✅ |
| **Container/Row/Col** | Bootstrap grid system | ✅ |
| **Icon** | Bootstrap Icons helper | ✅ |

### 🚧 Phase 2 (v0.3.0 - Planned Q1 2025)

- **Tabs** - Navigation tabs and pills
- **Dropdown** - Contextual menus
- **Input** - Text form controls with validation
- **Select** - Dropdown selections
- **Breadcrumb** - Navigation trails
- **Pagination** - Page navigation
- **Spinner** - Loading indicators
- **Progress** - Progress bars

See [ROADMAP.md](ROADMAP.md) for complete feature timeline.

---

## Examples

### Modal Dialog

```python
from faststrap import Modal, Button

# Create modal
modal = Modal(
    "Are you sure you want to delete this item?",
    modal_id="deleteModal",
    title="Confirm Delete",
    footer=Div(
        Button("Cancel", variant="secondary", data_bs_dismiss="modal"),
        Button("Delete", variant="danger")
    )
)

# Trigger button
trigger = Button("Delete Item", variant="danger", 
                data_bs_toggle="modal", data_bs_target="#deleteModal")
```

### Navigation Drawer

```python
from faststrap import Drawer, Button, Nav, A

# Create drawer
drawer = Drawer(
    Nav(
        A("Home", href="/", cls="nav-link"),
        A("About", href="/about", cls="nav-link"),
        A("Contact", href="/contact", cls="nav-link"),
        cls="flex-column"
    ),
    drawer_id="sidebar",
    title="Menu",
    placement="start"
)

# Trigger button
trigger = Button("Open Menu", data_bs_toggle="offcanvas", 
                data_bs_target="#sidebar")
```

### Responsive Navbar

```python
from faststrap import Navbar

nav = Navbar(
    brand="MyApp",
    brand_href="/",
    links=[
        ("Home", "/"),
        ("Features", "/features"),
        ("Pricing", "/pricing"),
    ],
    variant="dark",
    expand="lg"
)
```

### Toast Notifications

```python
from faststrap import Toast, ToastContainer

# Toast container (add once to layout)
container = ToastContainer(placement="top-end")

# Individual toast
toast = Toast(
    "Profile updated successfully!",
    title="Success",
    variant="success",
    autohide=True,
    delay=3000
)
```

---

## Project Structure

```
faststrap/
├── src/faststrap/
│   ├── __init__.py              # Public API
│   ├── core/
│   │   ├── assets.py            # Bootstrap injection
│   │   ├── base.py              # Component base classes
│   │   └── registry.py          # Component registry
│   ├── components/
│   │   ├── forms/               # Buttons, inputs
│   │   ├── display/             # Cards, badges
│   │   ├── feedback/            # Alerts, toasts, modals
│   │   ├── navigation/          # Navbars, drawers
│   │   └── layout/              # Grid system
│   └── utils/
│       ├── icons.py             # Bootstrap Icons
│       └── attrs.py             # Attribute helpers
├── static/                      # Bootstrap assets
│   ├── css/
│   │   ├── bootstrap.min.css
│   │   └── bootstrap-icons.min.css
│   └── js/
│       └── bootstrap.bundle.min.js
├── tests/                       # Pytest suite (121 tests)
├── examples/                    # Demo applications
└── docs/                        # Documentation
```

---

## Development

### Prerequisites

- Python 3.10+
- FastHTML 0.6+
- Git

### Setup

```bash
# Clone repository
git clone https://github.com/Evayoung/Faststrap.git
cd Faststrap

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install with dev dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Run with coverage
pytest --cov=faststrap

# Type checking
mypy src/faststrap

# Format code
black src/faststrap tests
ruff check src/faststrap tests
```

---

## Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Quick Contribution Guide

1. **Pick a component** from [ROADMAP.md](ROADMAP.md)
2. **Follow patterns** in [BUILDING_COMPONENTS.md](BUILDING_COMPONENTS.md)
3. **Write tests** - Aim for 100% coverage
4. **Submit PR** - We review within 48 hours

### Component Development

See [BUILDING_COMPONENTS.md](BUILDING_COMPONENTS.md) for detailed guide on building new components.

---

## Documentation

- 📖 **Component Spec**: [COMPONENT_SPEC.md](COMPONENT_SPEC.md)
- 🏗️ **Building Guide**: [BUILDING_COMPONENTS.md](BUILDING_COMPONENTS.md)
- 🗺️ **Roadmap**: [ROADMAP.md](ROADMAP.md)
- 🤝 **Contributing**: [CONTRIBUTING.md](CONTRIBUTING.md)
- 📝 **Changelog**: [CHANGELOG.md](CHANGELOG.md)

---

## Roadmap

### v0.2.1 (Current)
- ✅ 12 core components
- ✅ 121 tests, 84% coverage
- ✅ Complete documentation
- ✅ HTMX integration

### v0.3.0 (Q1 2025)
- Form components (Input, Select, Checkbox, Radio)
- Navigation (Tabs, Dropdown, Breadcrumb, Pagination)
- Feedback (Spinner, Progress)
- 20+ components total

### v1.0.0 (Q4 2025)
- 50+ components
- Component playground
- Video tutorials
- Production ready

See [ROADMAP.md](ROADMAP.md) for complete timeline.

---

## Support

- 📖 **Documentation**: [GitHub README](https://github.com/Evayoung/Faststrap#readme)
- 🐛 **Bug Reports**: [GitHub Issues](https://github.com/Evayoung/Faststrap/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/Evayoung/Faststrap/discussions)
- 🎮 **Discord**: Join [FastHTML Discord](https://discord.gg/qcXvcxMhdP)

---

## License

MIT License - see [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- **FastHTML** - The amazing pure-Python web framework
- **Bootstrap** - Battle-tested UI components
- **HTMX** - Dynamic interactions without complexity
- **Contributors** - Thank you! 🙏

---

**Built with ❤️ for the FastHTML community**