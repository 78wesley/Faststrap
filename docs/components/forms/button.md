# Button

The `Button` component is one of the most fundamental components in web development. In FastStrap, the `Button` component wraps the standard HTML `<button>` or `<a>` element, adding beautiful Bootstrap styling, automatic loading states, and icon support—all in pure Python.

!!! success "Goal"
    By the end of this guide, you will be able to create buttons for forms, navigation, and interactive actions, and customize them to fit your exact design needs, **even if you've never used Bootstrap before.**

---

## Quick Start

Here is the simplest way to create a button.

```python
from faststrap import Button

# A standard primary action button
Button("Click Me", variant="primary")
```

<div class="result" markdown>
![Screenshot: Basic Primary Button - A blue button saying 'Click Me'](../../assets/images/button-basic.png){ width=200 }
</div>

---

## Visual Examples & Use Cases

### 1. Variants (Colors = Meaning)

In Bootstrap (and FastStrap), colors carry *semantic meaning*. You don't just pick "blue"; you pick "Primary" (for the main action).

!!! note "Code & Output"
    
    ```python
    Button("Primary", variant="primary")
    Button("Secondary", variant="secondary")
    Button("Success", variant="success")
    Button("Danger", variant="danger")
    Button("Warning", variant="warning")
    Button("Info", variant="info")
    Button("Light", variant="light")
    Button("Dark", variant="dark")
    Button("Link", variant="link")
    ```

    <div class="result" markdown>
    ![Screenshot: Row of solid buttons in all colors: Blue (Primary), Gray (Secondary), Green (Success), Red (Danger), Yellow (Warning), Cyan (Info), White (Light), Black (Dark), Standard Link (Link)](../../assets/images/buttons-solid.png)
    </div>

**Understanding Semantic Colors:**

| Variant | Meaning | Typical Usage |
| :--- | :--- | :--- |
| `primary` | **Main Action** | Submit, Save, Login, Sign Up |
| `secondary` | **Secondary** | Cancel, Back, More Info |
| `success` | **Positive** | Confirm, Complete, Uploaded |
| `danger` | **Negative** | Delete, Remove, Stop |
| `warning` | **Caution** | Pause, Archive, Reset |
| `info` | **Information** | Help, About, Status |
| `light` | **Light** | Backgrounds, App Bars |
| `dark` | **Dark** | Footer actions, Inverse styling |
| `link` | **Link** | Look like a text link but act like a button |

### 2. Outline Styles

Sometimes a solid color is too "heavy" for a UI. Use `outline=True` for a lighter look with a transparent background and colored border.

!!! note "Code & Output"

    ```python
    # A less aggressive 'Delete' button
    Button("Delete", variant="danger", outline=True)
    Button("Save Draft", variant="primary", outline=True)
    ```

    <div class="result" markdown>
    ![Screenshot: Outline Buttons - Primary Outline (Blue border), Danger Outline (Red border)](../../assets/images/buttons-outline.png)
    </div>

### 3. Sizes

Hierarchy matters. Make your most important buttons larger and secondary actions smaller.

!!! note "Code & Output"

    ```python
    Button("Join Now!", size="lg", variant="primary") # Large Call-to-Action
    Button("Default", variant="secondary")            # Default Size
    Button("Details", size="sm", variant="info")      # Small table action
    ```
    
    <div class="result" markdown>
    ![Screenshot: Button Sizes - Large 'Join Now', Default 'Default', Small 'Details'](../../assets/images/buttons-sizes.png)
    </div>

### 4. Full Width Buttons

On mobile devices or in cards, you often want a button to stretch the full width of its container. Use `full_width=True`.

!!! note "Code & Output"

    ```python
    from faststrap import Card, Input

    # A Login Card example
    Card(
        Input(placeholder="Email"),
        Button("Sign In", variant="primary", full_width=True), # Stretches 100%
        style={"max-width": "300px"}
    )
    ```

    <div class="result" markdown>
    ![Screenshot: Full Width Button inside a Card](../assets/images/button-full-width.png){ width=300 }
    </div>

---

## Practical Functionality

### 1. Buttons as Links

Sometimes you need a button that *looks* like a button but *acts* like a link (taking you to a new page without HTMX). Use the `as_` argument.

```python
# Renders as an <a href="/login" class="btn btn-primary"> tag
Button("Go to Login", as_="a", href="/login", variant="primary")
```

### 2. Adding Icons

Visual cues help users respond faster. FastStrap makes adding icons easy (using [Bootstrap Icons](https://icons.getbootstrap.com/)).

!!! note "Code & Output"

    ```python
    # Icon at the START (default)
    Button("Save", icon="check-circle", variant="success")

    # Icon at the END
    Button("Next Step", icon="arrow-right", icon_pos="end", variant="primary")
    ```

    <div class="result" markdown>
    ![Screenshot: Buttons with icons - 'Save' has checkmark on left, 'Next Step' has arrow on right](../../assets/images/buttons-icons.png)
    </div>

### 3. Loading States (Great for HTMX)

If you are using HTMX, you want to tell the user something is happening so they don't click twice. FastStrap buttons can handle this states automatically.

!!! note "Code & Output"

    ```python
    # 1. Shows "Saving..." text
    # 2. Shows a spinner
    # 3. Disables the button to prevent double-clicks
    Button(
        "Save Profile",
        hx_post="/profile/save",
        loading_text="Saving...",
        cls="btn-loading" # Helper class to trigger JS if needed
    )
    ```

    <div class="result" markdown>
    ![Video: Button click transition to loading spinner and disabled state](../../assets/videos/button-loading-demo.gif)
    </div>

---

## Advanced Customization

### 1. Override using CSS Variables (The Pro Way)

Bootstrap 5 is built on CSS Variables. This is the **best way** to customize a specific button (like making a "Purple" brand button) without fighting the framework's CSS rules.

The following variables are available on every button:

| CSS Variable | Description | Example Value |
| :--- | :--- | :--- |
| `--bs-btn-bg` | Background color of the button. | `#6f42c1` (Purple) |
| `--bs-btn-color` | Text color of the button. | `#ffffff` (White) |
| `--bs-btn-border-color` | Border color. Usually same as bg. | `#6f42c1` |
| `--bs-btn-hover-bg` | Background color when hovered. | `#59359a` (Darker Purple) |
| `--bs-btn-hover-color` | Text color when hovered. | `#ffffff` |
| `--bs-btn-hover-border-color` | Border color when hovered. | `#59359a` |
| `--bs-btn-border-radius` | Corner roundness. | `2rem` (Pill), `0` (Square) |
| `--bs-btn-padding-y` | Vertical padding (height). | `1rem` |
| `--bs-btn-padding-x` | Horizontal padding (width). | `2rem` |
| `--bs-btn-font-size` | Text size. | `1.25rem` |

**Example: Creating a Custom Purple Button**

```python
# Create a dictionary of the variables you want to override
purple_btn_theme = {
    "--bs-btn-bg": "#6f42c1",
    "--bs-btn-border-color": "#6f42c1",
    "--bs-btn-hover-bg": "#59359a",
    "--bs-btn-hover-border-color": "#59359a",
    "--bs-btn-color": "#fff"
}

# Pass it to the css_vars argument
Button("Purple Button", variant="primary", css_vars=purple_btn_theme)
```

<div class="result" markdown>
![Screenshot: A custom purple button styled via CSS variables](../../assets/images/button-purple.png)
</div>

### 2. Standard CSS Classes

You can pass standard Bootstrap utility classes (or your own classes) using `cls`.

```python
# 'rounded-pill': Fully rounded corners
# 'shadow-lg': Large drop shadow
# 'text-uppercase': ALL CAPS TEXT
Button("Custom Style", variant="info", cls="rounded-pill shadow-lg text-uppercase")
```

### 3. Data Attributes & Accessibility

You can pass any standard HTML attribute. FastStrap cleans them up for you (converting python `underscore_names` to HTML `hyphen-names`).

```python
Button(
    "Menu", 
    # Data attributes (Python converts underscores to hyphens)
    data_bs_toggle="dropdown", 
    data_custom_id="123",
    
    # ARIA attributes for accessibility
    aria_label="Open main menu",
    aria_expanded="false"
)
# Renders: <button data-bs-toggle="dropdown" data-custom-id="123" aria-label="..." ...>
```

---

## Common "Recipes"

### The "Submit & Reset" Toolbar
A common pattern for forms, aligning buttons to the right or left.

```python
from faststrap import Div, Button

def FormActions():
    return Div(
        Button("Submit", type="submit", variant="primary"),
        Button("Reset", type="reset", variant="link", cls="text-decoration-none text-muted"),
        cls="d-flex align-items-center gap-2" # d-flex (flexbox), gap-2 (spacing)
    )
```

### The "Destructive Action"
For actions that can't be undone, use `outline-danger` to warn the user but not catch the eye *too* much (to avoid accidental clicks), but switch to solid danger for the confirmation.

```python
Button(
    "Delete Account", 
    variant="outline-danger", # Subtle warning
    icon="trash",
    data_bs_toggle="modal", 
    data_bs_target="#confirm-delete-modal" # Triggers a modal
)
```

---

## Parameter Reference

This table maps every FastStrap specific parameter to what it actually does in HTML/Bootstrap.

| FastStrap Param | Type | Bootstrap Class / Attribute | Description |
| :--- | :--- | :--- | :--- |
| `variant` | `str` | `.btn-{variant}` | Color theme. Options: `primary`, `secondary`, `success`, `danger`, `warning`, `info`, `light`, `dark`, `link`. |
| `outline` | `bool` | `.btn-outline-{variant}` | If `True`, renders outline style instead of solid fill. |
| `size` | `str` | `.btn-{size}` | Size of button. Options: `sm` (Small), `lg` (Large). Default is Medium. |
| `full_width` | `bool` | `.w-100` | Makes button span full width of parent. |
| `pill` | `bool` | `.rounded-pill` | Gives button fully rounded corners. |
| `as_` | `str` | `<tag>` | Tag to render. Default `button`. Use `a` for links. |
| `href` | `str` | `href="..."` | URL destination (requires `as_="a"`). |
| `disabled` | `bool` | `disabled` / `.disabled` | Disables interactivity and applies disabled styling. |
| `active` | `bool` | `.active` | Forces the button to appear in a "pressed" state. |
| `icon` | `str` | `<i class="bi bi-{icon}">` | Adds a Bootstrap Icon (e.g., "check", "house"). |
| `icon_pos` | `str` | - | Position of icon: `start` (default) or `end`. |
| `spinner` | `bool` | `.spinner-border` | Adds a loading spinner. |
| `loading` | `bool` | - | Helper that enables `spinner` and `disabled` state together. |
| `loading_text` | `str` | - | Text to display when `loading=True`. |
| `css_vars` | `dict` | `style="--var: val"` | Dict of CSS variables to apply inline. |

::: faststrap.components.forms.button.Button
    options:
        show_source: true
        heading_level: 4
