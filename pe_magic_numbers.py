def get_image_type(code):
    if code == 0x10B:
        return "PE32"
    elif code == 0x20B:
        return "PE32+"
