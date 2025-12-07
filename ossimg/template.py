#Import


#Golden Hour Template


#Gritty Contrast Template


#Pastel Matte Template
def apply_pastel_matte(img: Image.Image) -> Image.Image:
    img = adjust_saturation(img, 1.10)
    img = adjust_shadows(img, 0.70)
    img = adjust_brightness(img, 1.20)
    img = adjust_sharpness(img, 0.90)
    return img