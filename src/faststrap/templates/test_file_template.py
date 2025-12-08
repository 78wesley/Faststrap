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
