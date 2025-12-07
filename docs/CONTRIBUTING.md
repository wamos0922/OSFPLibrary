# Contributing to ossimg

Thank you for your interest in contributing!

## How to Contribute

### 1. Fork and Clone
```bash
git clone https://github.com/wamos0922/OSFPLibrary.git
cd OSFPLibrary
```

### 2. Create a Branch
```bash
git checkout -b feature/your-feature-name
```

Branch naming:
- `feature/` - New features
- `bugfix/` - Bug fixes
- `docs/` - Documentation
- `test/` - Tests

### 3. Make Changes

**Code Style:**
- Follow PEP 8
- Add docstrings to all functions
- Include type hints
- Keep functions focused and simple

**Example:**
```python
def adjust_brightness(img: Image.Image, factor: float) -> Image.Image:
    """
    Adjusts image brightness.
    
    Args:
        img: Input PIL Image
        factor: Brightness factor (1.0 = original)
        
    Returns:
        Adjusted image
    """
    # Implementation
```

### 4. Add Tests

For every new function, add tests in `tests/test_core.py`:
```python
def test_your_function(sample_image):
    """Test your function."""
    result = your_function(sample_image, param)
    assert isinstance(result, Image.Image)
```

Run tests:
```bash
pytest
```

### 5. Commit Changes

Use clear commit messages:
```bash
git commit -m "Add: brightness adjustment function"
git commit -m "Fix: shadow calculation overflow"
git commit -m "Docs: update API reference"
git commit -m "Test: add brightness tests"
```

### 6. Push and Create PR
```bash
git push origin feature/your-feature-name
```

Then create a Pull Request on GitHub.

## Code Review Process

1. All PRs require at least one review
2. Tests must pass
3. Code must follow style guidelines
4. Documentation must be updated

## Questions?

Open an issue or contact the team!