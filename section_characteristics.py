def _get_characteristic(code):
    if code == 0x00000008:
        return "IMAGE_SCN_TYPE_NO_PAD"
    elif code == 0x00000020:
        return "IMAGE_SCN_CNT_CODE"
    elif code == 0x00000040:
        return "IMAGE_SCN_CNT_INITIALIZED_DATA"
    elif code == 0x00000080:
        return "IMAGE_SCN_CNT_UNINITIALIZED_DATA"
    elif code == 0x00000200:
        return "IMAGE_SCN_LNK_INFO"
    elif code == 0x00000800:
        return "IMAGE_SCN_LNK_REMOVE"
    elif code == 0x00001000:
        return "IMAGE_SCN_LNK_COMDAT"
    elif code == 0x00008000:
        return "IMAGE_SCN_GPREL"
    elif code == 0x00020000:
        return "IMAGE_SCN_MEM_PURGEABLE"
    elif code == 0x00020000:
        return "IMAGE_SCN_MEM_16BIT"
    elif code == 0x00040000:
        return "IMAGE_SCN_MEM_LOCKED"
    elif code == 0x00080000:
        return "IMAGE_SCN_MEM_PRELOAD"
    elif code == 0x00100000:
        return "IMAGE_SCN_ALIGN_1BYTES"
    elif code == 0x00200000:
        return "IMAGE_SCN_ALIGN_2BYTES"
    elif code == 0x00300000:
        return "IMAGE_SCN_ALIGN_4BYTES"
    elif code == 0x00400000:
        return "IMAGE_SCN_ALIGN_8BYTES"
    elif code == 0x00500000:
        return "IMAGE_SCN_ALIGN_16BYTES"
    elif code == 0x00600000:
        return "IMAGE_SCN_ALIGN_32BYTES"
    elif code == 0x00700000:
        return "IMAGE_SCN_ALIGN_64BYTES"
    elif code == 0x00800000:
        return "IMAGE_SCN_ALIGN_128BYTES"
    elif code == 0x00900000:
        return "IMAGE_SCN_ALIGN_256BYTES"
    elif code == 0x00A00000:
        return "IMAGE_SCN_ALIGN_512BYTES"
    elif code == 0x00B00000:
        return "IMAGE_SCN_ALIGN_1024BYTES"
    elif code == 0x00C00000:
        return "IMAGE_SCN_ALIGN_2048BYTES"
    elif code == 0x00D00000:
        return "IMAGE_SCN_ALIGN_4096BYTES"
    elif code == 0x00E00000:
        return "IMAGE_SCN_ALIGN_8192BYTES"
    elif code == 0x01000000:
        return "IMAGE_SCN_LNK_NRELOC_OVFL"
    elif code == 0x02000000:
        return "IMAGE_SCN_MEM_DISCARDABLE"
    elif code == 0x04000000:
        return "IMAGE_SCN_MEM_NOT_CACHED"
    elif code == 0x08000000:
        return "IMAGE_SCN_MEM_NOT_PAGED"
    elif code == 0x10000000:
        return "IMAGE_SCN_MEM_SHARED"
    elif code == 0x20000000:
        return "IMAGE_SCN_MEM_EXECUTE"
    elif code == 0x40000000:
        return "IMAGE_SCN_MEM_READ"
    elif code == 0x80000000:
        return "IMAGE_SCN_MEM_WRITE"


def get_sn_characteristics(number):
    flags = []
    for i in range(0, 32):
        flag = 1 << i
        if number & flag:
            flags.append(_get_characteristic(flag))
    return flags
