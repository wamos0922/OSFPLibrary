#Import

#Brightness


#Saturation
def adjust_saturation(img: Image.Image, factor: float) -> Image.Image:
    """
    Adjusts the intensity of colors (saturation).
    
    Args:
        img: Input PIL Image object
        factor: Saturation adjustment factor
            - 1.0 = original
            - 0.0 = grayscale
            - > 1.0 = more vibrant colors
            
    Returns:
        PIL.Image.Image: Saturation-adjusted image
        
    Raises:
        TypeError: If img is not a PIL Image object
        
    Example:
        >>> vibrant = adjust_saturation(img, 1.4)  # 40% more saturated
        >>> grayscale = adjust_saturation(img, 0.0)  # Black & white
    """
    if not isinstance(img, Image.Image):
        raise TypeError("Input must be a PIL Image object.")
        
    enhancer = ImageEnhance.Color(img)
    return enhancer.enhance(factor)

#Sharpness


#Shadows

#Manual
