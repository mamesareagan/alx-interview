#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """ determines if a given data set represents a valid UTF-8 encoding
    Args:
        data (list): list of integers
    Returns:
        bool: True if data is a valid UTF-8 encoding, else False
    """
    bytes = 0
    for num in data:
        mask = 1 << 7
        if not bytes:
            while mask & num:
                bytes += 1
                mask >>= 1
            if not bytes:
                continue
            if bytes == 1 or bytes > 4:
                return False
        else:
            if num >> 6 != 2:
                return False
        bytes -= 1
    return bytes == 0
