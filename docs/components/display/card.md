# Card

Cards are flexible and extensible content containers. They include options for headers and footers, a wide variety of content, contextual background colors, and powerful display options.

!!! tip "Bootstrap Reference"
    [Bootstrap 5 Card Documentation](https://getbootstrap.com/docs/5.3/components/card/)

---

## Quick Start

```python
from faststrap import Card, Button

Card(
    "A simple card with some content.",
    header="Featured",
    footer=Button("Go somewhere")
)
```

<div class="result" markdown>
![Screenshot: Card with header, body text, and footer button](../assets/images/card-basic.png){ width=300 }
</div>

---

## Visual Examples & Use Cases

### 1. Images & Structure
Cards commonly contain images at the top (`img_top`) or bottom (`img_bottom`).

!!! note "Code & Output"
    ```python
    Card(
        "Some quick example text to build on the card title.",
        title="Card Image Cap",
        img_top="https://placehold.co/600x400",
        footer="Last updated 3 mins ago"
    )
    ```
    <div class="result" markdown>
    ![Screenshot: Card showing an image cap](../assets/images/card-image.png)
    </div>

### 2. Semantic Variants
Apply background colors with `text-bg-{variant}` classes by using the `variant` argument.

!!! note "Code & Output"
    ```python
    Card("Success Card", title="Success", variant="success")
    Card("Danger Card", title="Error", variant="danger")
    Card("Dark Card", title="Dark", variant="dark")
    ```
    <div class="result" markdown>
    ![Screenshot: Colored cards](../assets/images/card-variants.png)
    </div>

### 3. Slot Class Customization 🛠️
FastStrap Cards have specialized "slots" for customization. You don't have to overwrite the base classes; just inject your own into specific parts.

| Slot Param | Targeting | Description |
| :--- | :--- | :--- |
| `header_cls` | `.card-header` | Styles the header container. |
| `body_cls` | `.card-body` | Styles the main content area. |
| `footer_cls` | `.card-footer` | Styles the footer. |
| `title_cls` | `.card-title` | Styles the H5 title. |

!!! note "Code & Output"
    ```python
    # A card with a blue header and padded body
    Card(
        "Content...",
        header="My Title",
        header_cls="bg-primary text-white text-center",
        body_cls="p-5 fs-4"
    )
    ```

---

## Parameter Reference

::: faststrap.components.display.card.Card
    options:
        show_source: true
        heading_level: 4
