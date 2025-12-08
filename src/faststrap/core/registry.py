# src/faststrap/core/registry.py
"""Component registry for FastStrap."""

from __future__ import annotations

from collections.abc import Callable
from typing import Any

# Global registry for component metadata
_component_registry: dict[str, dict[str, Any]] = {}


def register(
    name: str | None = None,
    category: str | None = None,
    bootstrap_version: str = "5.3.3",
    requires_js: bool = False,
):
    """Decorator to register component metadata.

    Args:
        name: Component name (defaults to function name)
        category: Component category (layout, display, etc.)
        bootstrap_version: Min Bootstrap version required
        requires_js: Whether component needs Bootstrap JS

    Example:
        >>> @register(category="feedback", requires_js=True)
        >>> def Modal(...): ...
    """

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        component_name = name or func.__name__

        _component_registry[component_name] = {
            "func": func,
            "category": category,
            "bootstrap_version": bootstrap_version,
            "requires_js": requires_js,
            "module": func.__module__,
            "doc": func.__doc__,
        }

        # Mark function as registered
        func.__faststrap_registered__ = True
        func.__faststrap_metadata__ = _component_registry[component_name]

        return func

    return decorator


def get_registry() -> dict[str, dict[str, Any]]:
    """Get copy of component registry."""
    return _component_registry.copy()


def get_component(name: str) -> Callable[..., Any] | None:
    """Get component function by name."""
    return _component_registry.get(name, {}).get("func")


def list_components(category: str | None = None) -> list[str]:
    """List all registered components, optionally filtered by category.

    Args:
        category: Filter by category (layout, display, feedback, etc.)

    Returns:
        List of component names

    Example:
        >>> list_components(category="feedback")
        ['Alert', 'Toast', 'Modal', 'Spinner']
    """
    if category is None:
        return list(_component_registry.keys())

    return [name for name, meta in _component_registry.items() if meta.get("category") == category]


def autodiscover() -> None:
    """Auto-discover and register all components.

    This is called automatically when importing faststrap.
    Can be called manually to refresh registry after dynamic imports.
    """
    import importlib
    import pkgutil

    try:
        from faststrap import components

        # Recursively import all component modules
        for module_name in pkgutil.walk_packages(
            components.__path__, prefix="faststrap.components."
        ):
            try:
                importlib.import_module(module_name)
            except ImportError as e:
                # Log but don't fail - some components might have optional deps
                print(f"Warning: Could not import {module_name}: {e}")

    except ImportError:
        pass  # Components not yet installed


# Call autodiscover when registry is imported
autodiscover()
