def _get_flag(code):
    if code == 0x00000001:
        return "COMIMAGE_FLAGS_ILONLY"
    elif code == 0x00000002:
        return "COMIMAGE_FLAGS_32BITREQUIRED"
    elif code == 0x00000004:
        return "COMIMAGE_FLAGS_IL_LIBRARY"
    elif code == 0x00000008:
        return "COMIMAGE_FLAGS_STRONGNAMESIGNED"
    elif code == 0x00000010:
        return "COMIMAGE_FLAGS_NATIVE_ENTRYPOINT"
    elif code == 0x00010000:
        return "COMIMAGE_FLAGS_TRACKDEBUGDATA"


def get_clr_flags(number):
    flags = []
    for i in range(0, 32):
        flag = 1 << i
        if number & flag:
            flags.append(_get_flag(flag))
    return flags
