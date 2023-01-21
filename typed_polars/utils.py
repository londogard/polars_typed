from typing import TypeVar

T = TypeVar("T")


def as_list(data: list[T] | T | None) -> list[T]:
    match data:
        case list():
            return data
        case None:
            return []
        case _:
            return [data]
