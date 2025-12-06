"""FastStrap - Modern Bootstrap 5 components for FastHTML.

Build beautiful web UIs in pure Python with zero JavaScript knowledge.
"""

__version__ = "0.2.0"  # ← Update version!
__author__ = "FastStrap Contributors"
__license__ = "MIT"

# Core functionality
# Display
from .components.display import Badge, Card

# Feedback
from .components.feedback import Alert, Modal, Toast, ToastContainer

# Forms
from .components.forms import Button, ButtonGroup, ButtonToolbar

# Layout
from .components.layout import Col, Container, Row

# Navigation
from .components.navigation import Drawer, Navbar
from .core.assets import add_bootstrap, get_assets
from .core.base import merge_classes

# Utils
from .utils.icons import Icon

__all__ = [
    # Core
    "add_bootstrap",
    "get_assets",
    "merge_classes",
    # Forms
    "Button",
    "ButtonGroup",
    "ButtonToolbar",
    # Display
    "Badge",
    "Card",
    # Feedback
    "Alert",
    "Toast",
    "ToastContainer",
    "Modal",
    # Layout
    "Container",
    "Row",
    "Col",
    # Navigation
    "Drawer",
    "Navbar",
    # Utils
    "Icon",
    # Metadata
    "__version__",
    "__author__",
    "__license__",
]
