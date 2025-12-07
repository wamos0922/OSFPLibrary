#Import

#Brightness


#Saturation


#Sharpness


#Shadows
def adjust_shadows(img: Image.Image, amount: float) -> Image.Image:
    if not isinstance(img, Image.Image):
        raise TypeError("Input must be a PIL Image object.")
        
    img = img.convert("RGB")
    
    def shadow_curve(x):
        """Applies a gamma-like curve only to dark pixels."""
        x_norm = x / 255.0
        # Ensure the amount is clipped to prevent extreme gamma values
        gamma_exponent = max(-2.0, min(2.0, -amount))
        gamma = math.pow(2, gamma_exponent) 
        result_norm = math.pow(x_norm, gamma)
        return int(result_norm * 255)

    lut = [shadow_curve(i) for i in range(256)]
    
    # Apply the custom lookup table to all three RGB channels
    return img.point(lut * 3)
#Manual
