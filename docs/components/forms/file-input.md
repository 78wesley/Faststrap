# File Input

The `FileInput` component is an enhanced wrapper for `<input type="file">`. It supports single/multiple uploads, size options, and includes a built-in **automatic preview** feature (Phase 4B).

!!! tip "Bootstrap Reference"
    [Bootstrap 5 File Input](https://getbootstrap.com/docs/5.3/forms/form-control/#file-input)

---

## Quick Start

```python
from faststrap import FileInput

FileInput("resume", label="Upload Resume")
```

<div class="result" markdown>
![Screenshot: Standard file input](../assets/images/file-basic.png){ width=300 }
</div>

---

## Visual Examples & Use Cases

### 1. Multiple Files & Sizing
Allow uploading multiple files at once.

!!! note "Code & Output"
    ```python
    FileInput("photos", label="Gallery Photos", multiple=True, size="lg")
    ```

### 2. Automatic Image Preview (✨ New in Phase 4B)
FastStrap includes a lightweight JavaScript snippet that can automatically show a preview of selected images *before* upload.

Set `preview_id="auto"` to have FastStrap handle everything for you.

!!! note "Code & Output"
    ```python
    # Automatically generates a preview container with ID 'file-avatar-preview'
    FileInput(
        "avatar", 
        label="Profile Picture", 
        accept="image/*", 
        preview_id="auto" 
    )
    ```
    
    <div class="result" markdown>
    ![Screenshot: File input showing an image preview below it](../assets/images/file-preview.png)
    </div>

---

## Parameter Reference

| Param | Type | HTML Attribute | Description |
| :--- | :--- | :--- | :--- |
| `name` | `str` | `name="..."` | Form field name. |
| `label` | `str` | `<label>` | Input label. |
| `multiple` | `bool` | `multiple` | Allow selecting multiple files. |
| `accept` | `str` | `accept="..."` | File type filter (e.g. `image/*`, `.pdf`). |
| `preview_id` | `str` | - | ID of element to display preview in. Use `"auto"` for automatic generation. |

::: faststrap.components.forms.file.FileInput
    options:
        show_source: true
        heading_level: 4
