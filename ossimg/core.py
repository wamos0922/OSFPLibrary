#Import

#Brightness


#Saturation


#Sharpness
def adjust_sharpness(img: Image.Image, factor: float) -> Image.Image:
    """
    Adjusts the image sharpness.
    
    Args:
        img: Input PIL Image object
        factor: Sharpness adjustment factor
            - 1.0 = original
            - > 1.0 = sharper
            - < 1.0 = blurrier
            
    Returns:
        PIL.Image.Image: Sharpness-adjusted image
        
    Raises:
        TypeError: If img is not a PIL Image object
        
    Example:
        >>> sharp = adjust_sharpness(img, 2.0)  # Very sharp
        >>> soft = adjust_sharpness(img, 0.5)  # Soft focus
    """
    if not isinstance(img, Image.Image):
        raise TypeError("Input must be a PIL Image object.")
        
    enhancer = ImageEnhance.Sharpness(img)
    return enhancer.enhance(factor)


#Shadows

#Manual
