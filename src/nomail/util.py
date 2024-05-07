from typing import List, Sequence


def split_bytes(byte_str: bytes) -> List[bytes]:
    return byte_str.split(b' ') if byte_str else []


def to_int(collection: Sequence) -> List[int]:
    return [int(item) for item in collection]
