# Temporary shim for Python 3.12+ where imghdr was removed.
# This prevents import errors from older libraries.
def what(file, h=None):
    return None
