from sys import platform

SLASH = ''
if platform == 'win32':
    SLASH = '\\'
else:
    SLASH = '/'