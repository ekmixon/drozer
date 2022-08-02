"""
A library of fileystem functions.
"""

import md5

def read(path):
    """
    Utility method to read a file from the filesystem into a string.
    """

    try:
        with open(path, 'rb') as f:
            line = data = f.read()

            while line != "":
                line = f.read()

                data += line

        return data
    except IOError:
        return None
    
def touch(path):
    """
    Utility method to touch a file on the filesystem.
    """
    
    open(path, 'w').close()
    
def write(path, data):
    """
    Utility method to write a string into a filesystem file.
    """

    try:
        with open(path, 'wb') as f:
            f.write(data)
        return len(data)
    except IOError:
        return None
        
def md5sum(path):
    """
    Utility method to get the md5sum of a file on the filesystem
    """

    try:
        with open(path, 'rb') as f:
            line = data = f.read()

            while line != "":
                line = f.read()

                data += line

        return md5.new(data).digest().encode("hex")
    except IOError:
        return None
        
