from typing import Any

class ResourceName:
    @classmethod
    def format_composite(cls, *arg: str):
        str

def get_nested_attr(obj: Any, attr: str, *args: Any) -> Any: ...
def convert_upper_case_to_snake_case(string: str) -> str: ...
def convert_snake_case_to_upper_case(string: str) -> str: ...
