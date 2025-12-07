# API Reference

Complete reference for all ossimg functions.

---

## Core Functions

### `load_image(path)`

Loads an image from a file path.

**Parameters:**
- `path` (str): Path to the image file

**Returns:**
- `PIL.Image.Image`: Loaded image object

**Example:**
```python
from ossimg import load_image
img = load_image('photo.jpg')
```

---

### `adjust_brightness(img, factor)`

Adjusts the overall brightness of an image.

**Parameters:**
- `img` (PIL.Image.Image): Input image
- `factor` (float): Brightness factor
  - `1.0` = original
  - `> 1.0` = brighter
  - `< 1.0` = darker

**Returns:**
- `PIL.Image.Image`: Brightness-adjusted image

**Raises:**
- `TypeError`: If img is not a PIL Image

**Example:**
```python
from ossimg import load_image, adjust_brightness

img = load_image('photo.jpg')
bright = adjust_brightness(img, 1.5)  
dark = adjust_brightness(img, 0.7)    
```

---

### `adjust_saturation(img, factor)`

Adjusts color intensity (saturation).

**Parameters:**
- `img` (PIL.Image.Image): Input image
- `factor` (float): Saturation factor
  - `1.0` = original
  - `0.0` = grayscale
  - `> 1.0` = more vibrant

**Returns:**
- `PIL.Image.Image`: Saturation-adjusted image

**Example:**
```python
vibrant = adjust_saturation(img, 1.4)   
bw = adjust_saturation(img, 0.0)        
```

---

### `adjust_sharpness(img, factor)`

Adjusts image sharpness.

**Parameters:**
- `img` (PIL.Image.Image): Input image
- `factor` (float): Sharpness factor
  - `1.0` = original
  - `> 1.0` = sharper
  - `< 1.0` = blurrier

**Returns:**
- `PIL.Image.Image`: Sharpness-adjusted image

**Example:**
```python
sharp = adjust_sharpness(img, 2.0)   
soft = adjust_sharpness(img, 0.5)    
```

---

### `adjust_shadows(img, amount)`

Lifts or crushes shadow areas.

**Parameters:**
- `img` (PIL.Image.Image): Input image
- `amount` (float): Shadow adjustment
  - `0.0` = neutral
  - `> 0.0` = lift shadows (brighter)
  - `< 0.0` = crush shadows (darker)

**Returns:**
- `PIL.Image.Image`: Shadow-adjusted image

**Example:**
```python
lifted = adjust_shadows(img, 0.5)    
crushed = adjust_shadows(img, -0.3)  
```

---

### `process_manual_edits(img, saturation, shadows, brightness, sharpness)`

Applies all four adjustments sequentially with step-by-step output.

**Parameters:**
- `img` (PIL.Image.Image): Input image
- `saturation_factor` (float): Saturation adjustment
- `shadows_amount` (float): Shadow adjustment
- `brightness_factor` (float): Brightness adjustment
- `sharpness_factor` (float): Sharpness adjustment

**Yields:**
- `Tuple[str, PIL.Image.Image]`: (feature_name, processed_image)

**Example:**
```python
for step_name, result in process_manual_edits(img, 1.2, 0.3, 1.1, 1.0):
    print(f"Applied: {step_name}")
    result.save(f"{step_name}.jpg")
```

---

## Template Functions

### `apply_golden_hour(img)`

Warm, soft golden hour aesthetic.

**Effect:**
- Saturation: +30%
- Shadows: +0.30 (lifted)
- Brightness: +15%
- Sharpness: -20% (softer)

**Example:**
```python
from ossimg import apply_golden_hour
result = apply_golden_hour(img)
```

---

### `apply_gritty_contrast(img)`

Urban high-contrast look.

**Effect:**
- Sharpness: +150%
- Brightness: -10%
- Shadows: -0.20 (crushed)
- Saturation: -20%

**Example:**
```python
from ossimg import apply_gritty_contrast
result = apply_gritty_contrast(img)
```

---

### `apply_pastel_matte(img)`

Soft, dreamy pastel aesthetic.

**Effect:**
- Saturation: +10%
- Shadows: +0.70 (heavily lifted)
- Brightness: +20%
- Sharpness: -10%

**Example:**
```python
from ossimg import apply_pastel_matte
result = apply_pastel_matte(img)
```