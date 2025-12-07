#Import


#Golden Hour Template


#Gritty Contrast Template
def apply_gritty_contrast(img: Image.Image) -> Image.Image:
    img = adjust_sharpness(img, 2.50)
    img = adjust_brightness(img, 0.90)
    img = adjust_shadows(img, -0.20)
    img = adjust_saturation(img, 0.80) 
    return img

#Pastel Matte Template
