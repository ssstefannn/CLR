def _get_characteristic(code):
    if code == 0x0001:
        return "IMAGE_FILE_RELOCS_STRIPPED"
    elif code == 0x0002:
        return "IMAGE_FILE_EXECUTABLE_IMAGE"
    elif code == 0x0004:
        return "IMAGE_FILE_LINE_NUMS_STRIPPED"
    elif code == 0x0008:
        return "IMAGE_FILE_LOCAL_SYMS_STRIPPED"
    elif code == 0x0010:
        return "IMAGE_FILE_AGGRESSIVE_WS_TRIM"
    elif code == 0x0020:
        return "IMAGE_FILE_LARGE_ADDRESS_AWARE"
    elif code == 0x0040:
        return "IMAGE_FILE_RESERVED_FOR_FUTURE"
    elif code == 0x0080:
        return "IMAGE_FILE_BYTES_REVERSED_LO"
    elif code == 0x0100:
        return "IMAGE_FILE_32BIT_MACHINE"
    elif code == 0x0200:
        return "IMAGE_FILE_DEBUG_STRIPPED"
    elif code == 0x0400:
        return "IMAGE_FILE_REMOVABLE_RUN_FROM_SWAP"
    elif code == 0x0800:
        return "IMAGE_FILE_NET_RUN_FROM_SWAP"
    elif code == 0x1000:
        return "IMAGE_FILE_SYSTEM"
    elif code == 0x2000:
        return "IMAGE_FILE_DLL"
    elif code == 0x4000:
        return "IMAGE_FILE_UP_SYSTEM_ONLY"
    elif code == 0x8000:
        return "IMAGE_FILE_BYTES_REVERSED_HI"


def get_characteristics(number):
    flags = []
    for i in range(0, 16):
        flag = 1 << i
        if number & flag:
            flags.append(_get_characteristic(flag))
    return flags
