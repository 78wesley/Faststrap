"""Bootstrap [ComponentName] for [purpose]."""

from typing import Any, Literal

from fasthtml.common import Div  # Or appropriate FT type

from ...core.base import merge_classes

# Type aliases
VariantType = Literal[
    "primary", "secondary", "success", "danger", "warning", "info", "light", "dark"
]


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
