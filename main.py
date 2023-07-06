from json import dumps
from machine_types import get_machine_type
from characteristics import get_characteristics
from pe_magic_numbers import get_image_type
from windows_subsystems import get_windows_subsystem
from dll_characteristics import get_dll_characteristics
from section_characteristics import get_sn_characteristics
from clr_flags import get_clr_flags

byte = 1
word = 2
dword = 4
qword = 8
paragraph = 16
page = 512


def get_content():
    file_path = "./ConsoleApp/bin/Debug/ConsoleApp.exe"
    try:
        f = open(file_path, "rb")
        return f.read()
    except:
        print(f"Couldn't open and read file at {file_path}")


def get_string(n):
    global content
    global bytes_unpacked
    bytes_unpacked += n
    data, content = (
        content[:n].decode("ascii").rstrip(" \t\r\n\0"),  # rstrip to remove \u0000
        content[n:],
    )
    return data


def get_number(n):
    global content
    global bytes_unpacked
    bytes_unpacked += n
    data, content = int.from_bytes(content[:n], "little"), content[n:]
    return data


def get_bytes(n):
    global content
    global bytes_unpacked
    bytes_unpacked += n
    data, content = content[:n], content[n:]
    return data


def fill_ms_dos_header(pe):
    mdh = pe["ms_dos_header"] = {}
    mdh["magic"] = get_string(word)
    mdh["bytes_on_last_page_of_file"] = get_number(word)
    mdh["number_of_whole_/_partial_pages"] = get_number(word)
    mdh["num_of_entries_in_rel_tbl"] = get_number(word)
    mdh["header_size_in_paragraphs"] = get_number(word)
    mdh["minimum_allocation_in_paragraphs"] = get_number(word)
    mdh["maximum_allocation_in_paragraphs"] = get_number(word)
    mdh["initial_SS"] = get_number(word)
    mdh["initial_SP"] = get_number(word)
    mdh["checksum"] = get_number(word)
    mdh["initial_IP"] = get_number(word)
    mdh["initial_CS"] = get_number(word)
    mdh["absolute_offset_to_relocation_table"] = get_number(word)
    mdh["overlay"] = get_number(word)
    mdh["reserved"] = get_number(qword)
    mdh["OEM_identifier"] = get_number(word)
    mdh["OEM_info"] = get_number(word)
    mdh["reserved"] = get_string(20)
    mdh["file_address_of_new_exe_header"] = get_number(dword)


def fill_ms_dos_stub(pe):
    pe["ms_dos_stub"] = str(get_bytes(64))


def fill_signature(pe):
    pe["SIGNATURE"] = get_string(dword)


def fill_coff_header(pe):
    ch = pe["coff_header"] = {}
    ch["machine"] = get_machine_type(get_number(word))
    ch["number_of_sections"] = get_number(word)
    ch["time_date_stamp"] = get_number(qword)
    ch["pointer_to_symbol_table"] = get_number(word)
    ch["number_of_symbols"] = get_number(word)
    ch["size_of_pe_header"] = get_number(word)
    ch["characteristics"] = get_characteristics(get_number(word))


def fill_std_fields(pe):
    sf = pe["standard_fields"] = {}
    sf["linker_major_version_number"] = get_number(byte)
    sf["linker_minor_version_number"] = get_number(byte)
    sf["sz_of_code"] = get_number(dword)
    sf["sz_of_initialized_data"] = get_number(dword)
    sf["sz_of_uninitialized_data"] = get_number(dword)
    sf["addr_of_entry_point"] = get_number(dword)
    sf["base_of_code"] = get_number(dword)
    sf["base_of_data"] = get_number(dword)


def fill_windows_fields(pe):
    wf = pe["windows_fields"] = {}
    wf["image_base"] = get_number(dword)
    wf["section_alignment"] = get_number(dword)
    wf["file_alignment"] = get_number(dword)
    wf["major_os_ver"] = get_number(word)
    wf["minor_os_ver"] = get_number(word)
    wf["major_img_ver"] = get_number(word)
    wf["minor_img_ver"] = get_number(word)
    wf["major_subsystem_ver"] = get_number(word)
    wf["minor_subsystem_ver"] = get_number(word)
    wf["win_32_ver_value"] = get_number(dword)
    wf["sz_of_img"] = get_number(dword)
    wf["sz_oh_hdrs"] = get_number(dword)
    wf["checksum"] = get_number(dword)
    wf["subsystem"] = get_windows_subsystem(get_number(word))
    wf["dll_characteristics"] = get_dll_characteristics(get_number(word))
    wf["sz_stack_reserve"] = get_number(dword)
    wf["sz_stack_commit"] = get_number(dword)
    wf["sz_heap_reserve"] = get_number(dword)
    wf["sz_heap_commit"] = get_number(dword)
    wf["loader_flags"] = get_number(dword)
    wf["num_of_rva_and_sizes"] = get_number(dword)


def fill_data_dirs(pe):
    dd = pe["data_directories"] = {}
    dd["export_tbl_addr"] = get_number(dword)
    dd["export_tbl_sz"] = get_number(dword)
    dd["import_tbl_addr"] = get_number(dword)
    dd["import_tbl_sz"] = get_number(dword)
    dd["resource_tbl_addr"] = get_number(dword)
    dd["resource_tbl_sz"] = get_number(dword)
    dd["exception_tbl_addr"] = get_number(dword)
    dd["exception_tbl_sz"] = get_number(dword)
    dd["certificate_tbl_addr"] = get_number(dword)
    dd["certificate_tbl_sz"] = get_number(dword)
    dd["base_reloc_tbl_addr"] = get_number(dword)
    dd["base_reloc_tbl_sz"] = get_number(dword)
    dd["debug_addr"] = get_number(dword)
    dd["debug_sz"] = get_number(dword)
    dd["architecture_addr"] = get_number(dword)
    dd["architecture_sz"] = get_number(dword)
    dd["global_ptr_addr"] = get_number(dword)
    dd["global_ptr_sz"] = get_number(dword)
    dd["tls_tabl_addr"] = get_number(dword)
    dd["tls_tabl_sz"] = get_number(dword)
    dd["load_config_tbl_addr"] = get_number(dword)
    dd["load_config_tbl_sz"] = get_number(dword)
    dd["bound_import_tbl_addr"] = get_number(dword)
    dd["bound_import_tbl_sz"] = get_number(dword)
    dd["iat_addr"] = get_number(dword)
    dd["iat_sz"] = get_number(dword)
    dd["delay_import_desc_addr"] = get_number(dword)
    dd["delay_import_desc_sz"] = get_number(dword)
    dd["clr_runtime_hdr_addr"] = get_number(dword)
    dd["clr_runtime_hdr_sz"] = get_number(dword)
    dd["reserved_addr"] = get_number(dword)
    dd["reserved_sz"] = get_number(dword)


def fill_pe_header(pe):
    ph = pe["pe_header"] = {}
    ph["magic"] = get_image_type(get_number(word))
    fill_std_fields(ph)
    fill_windows_fields(ph)
    fill_data_dirs(ph)


def fill_sn_hdr(pe, sn_name):
    sn_hdr = pe[sn_name] = {}
    sn_hdr["name"] = get_string(qword)
    sn_hdr["virtual_sz"] = get_number(dword)
    sn_hdr["virtual_addr"] = get_number(dword)
    sn_hdr["sz_of_raw_data"] = get_number(dword)
    sn_hdr["ptr_to_raw_data"] = get_number(dword)
    sn_hdr["ptr_to_relocs"] = get_number(dword)
    sn_hdr["ptr_to_ln_numbers"] = get_number(dword)
    sn_hdr["num_of_relocs"] = get_number(word)
    sn_hdr["num_of_ln_numbers"] = get_number(word)
    sn_hdr["sn_characteristics"] = get_sn_characteristics(get_number(dword))


def fill_section_headers(pe):
    sections = pe["section_headers"] = {}
    fill_sn_hdr(sections, ".text")
    fill_sn_hdr(sections, ".rsrc")
    fill_sn_hdr(sections, ".reloc")


def fill_clr_header(pe):
    ch = pe["clr_header"] = {}
    ch["cb"] = get_number(dword)
    ch["major_runtime_ver"] = get_number(word)
    ch["minor_runtime_ver"] = get_number(word)
    ch["metadata_rva"] = get_number(dword)
    ch["metadata_sz"] = get_number(dword)
    ch["flags"] = get_clr_flags(get_number(word))
    ch["entry_point_token_/_rva"] = get_string(dword)
    ch["resources_rva"] = get_number(dword)
    ch["resources_sz"] = get_number(dword)
    ch["strong_name_signature_rva"] = get_number(dword)
    ch["strong_name_signature_sz"] = get_number(dword)
    ch["code_mngr_tbl_rva"] = get_number(dword)
    ch["code_mngr_tbl_sz"] = get_number(dword)
    ch["v_table_fixups_rva"] = get_number(dword)
    ch["v_table_fixups_sz"] = get_number(dword)
    ch["export_addr_tbl_jumps_rva"] = get_number(dword)
    ch["export_addr_tbl_jumps_sz"] = get_number(dword)
    ch["managed_native_hdr"] = get_number(qword)


def fill_storage_signature(pe):
    ss = pe["storage_signature"] = {}
    ss["lSignature"] = get_string(dword)
    ss["iMajorVersion"] = get_number(word)
    ss["iMinorVersion"] = get_number(word)
    ss["iExtraData"] = get_number(dword)
    ss["iVersionString"] = get_number(dword)
    ss["pVersion"] = get_string(ss["iVersionString"])


def fill_storage_header(pe):
    sh = pe["storage_header"] = {}
    sh["fFlags"] = get_number(byte)
    sh["padding"] = get_number(byte)
    sh["number_of_streams(iStream)"] = get_number(word)


def fill_stream_header(pe, stream_name, rc_name_length):
    sh = pe[stream_name] = {}
    sh["iOffset"] = get_number(dword)
    sh["iSize"] = get_number(dword)
    sh["rcName"] = get_string(rc_name_length)


def fill_stream_headers(pe):
    shdrs = pe["stream_headers"] = {}
    fill_stream_header(shdrs, "#~", 4)
    fill_stream_header(shdrs, "Strings", 12)
    fill_stream_header(shdrs, "US", 4)
    fill_stream_header(shdrs, "GUID", 8)
    fill_stream_header(shdrs, "Blob", 8)


def fill_metadata_general_header(pe):
    mgh = pe["metadata_general_header"] = {}
    fill_storage_signature(mgh)
    fill_storage_header(mgh)
    fill_stream_headers(mgh)


def fill_metadata(pe):
    m = pe["metadata"] = {}
    fill_metadata_general_header(m)
    # fill_metadata_streams


content = get_content()
bytes_unpacked = 0
pe = {}
fill_ms_dos_header(pe)
fill_ms_dos_stub(pe)
fill_signature(pe)
fill_coff_header(pe)
fill_pe_header(pe)
fill_section_headers(pe)

pe["section_padding"] = get_number(16)

ts = "text_section"
pe[ts] = {}
pe[ts]["import_addr_tbl"] = get_number(qword)
fill_clr_header(pe[ts])
pe[ts]["unknown_26_bytes"] = get_number(26)
fill_metadata(pe[ts])


# pe["text_section"][m][""]


print(dumps(pe, indent=4))
print(f"Bytes unpacked: {bytes_unpacked}")
print(f"Bytes remaining: {content.__len__()}")
print(f"Current rva: {7680 + bytes_unpacked}")
