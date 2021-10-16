from typing import Any, Sequence, Union, overload

import proto
from google.protobuf.message import Message

def get_nested_attr(obj: Any, attr: str, *args: Any) -> Any: ...
def set_nested_message_field(
    message: Message, field_path: Union[str, Sequence[str]], value: Any
) -> None: ...
def convert_upper_case_to_snake_case(string: str) -> str: ...
def convert_snake_case_to_upper_case(string: str) -> str: ...
def convert_proto_plus_to_protobuf(
    message: Union[proto.Message, Message]
) -> Message: ...
def convert_protobuf_to_proto_plus(
    message: Union[Message, proto.Message]
) -> proto.Message: ...
def proto_copy_from(
    destination: Union[proto.Message, Message], origin: Union[proto.Message, Message]
) -> None: ...