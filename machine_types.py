def get_machine_type(code):
    if code == 0x0:
        return "IMAGE_FILE_MACHINE_UNKNOWN"
    elif code == 0x184:
        return "IMAGE_FILE_MACHINE_ALPHA"
    elif code == 0x284:
        return "IMAGE_FILE_MACHINE_ALPHA64"
    elif code == 0x1D3:
        return "IMAGE_FILE_MACHINE_AM33"
    elif code == 0x8664:
        return "IMAGE_FILE_MACHINE_AMD64"
    elif code == 0x1C0:
        return "IMAGE_FILE_MACHINE_ARM"
    elif code == 0xAA64:
        return "IMAGE_FILE_MACHINE_ARM64"
    elif code == 0x1C4:
        return "IMAGE_FILE_MACHINE_ARMNT"
    elif code == 0x284:
        return "IMAGE_FILE_MACHINE_AXP64"
    elif code == 0xEBC:
        return "IMAGE_FILE_MACHINE_EBC"
    elif code == 0x14C:
        return "IMAGE_FILE_MACHINE_I386"
    elif code == 0x200:
        return "IMAGE_FILE_MACHINE_IA64"
    elif code == 0x6232:
        return "IMAGE_FILE_MACHINE_LOONGARCH32"
    elif code == 0x6264:
        return "IMAGE_FILE_MACHINE_LOONGARCH64"
    elif code == 0x9041:
        return "IMAGE_FILE_MACHINE_M32R"
    elif code == 0x266:
        return "IMAGE_FILE_MACHINE_MIPS16"
    elif code == 0x366:
        return "IMAGE_FILE_MACHINE_MIPSFPU"
    elif code == 0x466:
        return "IMAGE_FILE_MACHINE_MIPSFPU16"
    elif code == 0x1F0:
        return "IMAGE_FILE_MACHINE_POWERPC"
    elif code == 0x1F1:
        return "IMAGE_FILE_MACHINE_POWERPCFP"
    elif code == 0x166:
        return "IMAGE_FILE_MACHINE_R4000"
    elif code == 0x5032:
        return "IMAGE_FILE_MACHINE_RISCV32"
    elif code == 0x5064:
        return "IMAGE_FILE_MACHINE_RISCV64"
    elif code == 0x5128:
        return "IMAGE_FILE_MACHINE_RISCV128"
    elif code == 0x1A2:
        return "IMAGE_FILE_MACHINE_SH3"
    elif code == 0x1A3:
        return "IMAGE_FILE_MACHINE_SH3DSP"
    elif code == 0x1A6:
        return "IMAGE_FILE_MACHINE_SH4"
    elif code == 0x1A8:
        return "IMAGE_FILE_MACHINE_SH5"
    elif code == 0x1C2:
        return "IMAGE_FILE_MACHINE_THUMB"
    elif code == 0x169:
        return "IMAGE_FILE_MACHINE_WCEMIPSV2"
