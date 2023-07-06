def get_windows_subsystem(code):
    if code == 0:
        return "IMAGE_SUBSYSTEM_UNKNOWN"
    elif code == 1:
        return "IMAGE_SUBSYSTEM_NATIVE"
    elif code == 2:
        return "IMAGE_SUBSYSTEM_WINDOWS_GUI"
    elif code == 3:
        return "IMAGE_SUBSYSTEM_WINDOWS_CUI"
    elif code == 5:
        return "IMAGE_SUBSYSTEM_OS2_CUI"
    elif code == 7:
        return "IMAGE_SUBSYSTEM_POSIX_CUI"
    elif code == 8:
        return "IMAGE_SUBSYSTEM_NATIVE_WINDOWS"
    elif code == 9:
        return "IMAGE_SUBSYSTEM_WINDOWS_CE_GUI"
    elif code == 10:
        return "IMAGE_SUBSYSTEM_EFI_APPLICATION"
    elif code == 11:
        return "IMAGE_SUBSYSTEM_EFI_BOOT_SERVICE_DRIVER"
    elif code == 12:
        return "IMAGE_SUBSYSTEM_EFI_RUNTIME_DRIVER"
    elif code == 13:
        return "IMAGE_SUBSYSTEM_EFI_ROM"
    elif code == 14:
        return "IMAGE_SUBSYSTEM_XBOX"
    elif code == 16:
        return "IMAGE_SUBSYSTEM_WINDOWS_BOOT_APPLICATION"
