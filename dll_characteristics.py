def _get_dll_characteristic(code):
    if code == 0x0020:
        return "IMAGE_DLLCHARACTERISTICS_HIGH_ENTROPY_VA"
    elif code == 0x0040:
        return "IMAGE_DLLCHARACTERISTICS_DYNAMIC_BASE"
    elif code == 0x0080:
        return "IMAGE_DLLCHARACTERISTICS_FORCE_INTEGRITY"
    elif code == 0x0100:
        return "IMAGE_DLLCHARACTERISTICS_NX_COMPAT"
    elif code == 0x0200:
        return "IMAGE_DLLCHARACTERISTICS_NO_ISOLATION"
    elif code == 0x0400:
        return "IMAGE_DLLCHARACTERISTICS_NO_SEH"
    elif code == 0x0800:
        return "IMAGE_DLLCHARACTERISTICS_NO_BIND"
    elif code == 0x1000:
        return "IMAGE_DLLCHARACTERISTICS_APPCONTAINER"
    elif code == 0x2000:
        return "IMAGE_DLLCHARACTERISTICS_WDM_DRIVER"
    elif code == 0x4000:
        return "IMAGE_DLLCHARACTERISTICS_GUARD_CF"
    elif code == 0x8000:
        return "IMAGE_DLLCHARACTERISTICS_TERMINAL_SERVER_AWARE"


def get_dll_characteristics(number):
    flags = []
    for i in range(0, 16):
        flag = 1 << i
        if number & flag:
            flags.append(_get_dll_characteristic(flag))
    return flags
