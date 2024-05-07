from typing import Sequence


def split_bytes(byte_str: bytes) -> list[bytes]:
    return byte_str.split(b' ') if byte_str else []


def to_int(collection: Sequence) -> list[int]:
    return [int(item) for item in collection]
