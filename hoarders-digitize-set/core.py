from bz2 import compress
import filetype

def open_file(path: str, force: bool):
    list_of_archiving_method = [
    'application/x-7z-compressed',
    'application/x-tar',
    'application/x-xz',
    'application/gzip',
    'application/zip'
]
    #file_status = False
    compressing = False
    compressing_type = ''
    path2file = path 
    try:
        type_of_file = filetype.guess(path2file)
        #file_status = True
    except None:
        #file_status = False
        return 'Could not read the file.', False
    if type_of_file.mime not in list_of_archiving_method:
        return 'This current file are not able to be read by this libary...\n"Could not read file type."\nSorry...', False
    else:
        pass
    if type_of_file.mime == list_of_archiving_method[0]:
        compressing = True
        compressing_type = '7z'
    elif type_of_file.mime == list_of_archiving_method[1]:
        compressing = False
        compressing_type = ''
    elif type_of_file == list_of_archiving_method[2]:
        compressing = True
        compressing_type = 'xz'
    elif type_of_file == list_of_archiving_method[3]:
        compressing = True
        compressing_type = 'gzip'
    elif type_of_file == list_of_archiving_method[4]:
        compressing = True
        compressing_type = 'zip'
    else:
        return "This file can't be read by this libary yet...\nSorry about that...", False
    

