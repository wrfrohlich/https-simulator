from binascii import unhexlify

def dec_to_hex(value: int)-> hex:
    return hex(value)

def hex_to_dec(value: str)-> hex:
    return int(value, 16)

def hex_to_bytes(value: str)-> bytes:
    '''
    Convert the value from hex to byte

    Args:
        value (str): String with values in hex (e.g. F20DBA6FF2).

    Return:
        Value converted into bytes
    '''
    return unhexlify(value)

def byte_to_hex(value: bytes)-> str:
    return value.hex()