def split_bytes(byte_str: bytes) -> list[bytes]:
    return byte_str.split(b' ') if byte_str else []
