import os

def verify():
    platform = os.name
    if platform == 'nt':
        if os.path.isdir('webanlimaks runtime windows'):
            get_runtime = True
        else:
            get_runtime = False
    
    if platform == 'posix':
        if os.path.isdir('webanlimaks runtime linux'):
            get_runtime = True
        else:
            get_runtime = False

    return get_runtime
    