from collections.abc import Sequence
from typing import Any, overload

import proto
from google.protobuf.message import Message

def get_nested_attr(obj: Any, attr: str, *args: Any) -> Any: ...
def set_nested_message_field(
    message: Message, field_path: str | Sequence[str], value: Any
) -> None: ...
def convert_upper_case_to_snake_case(string: str) -> str: ...
def convert_snake_case_to_upper_case(string: str) -> str: ...
def convert_proto_plus_to_protobuf(message: proto.Message | Message) -> Message: ...
def convert_protobuf_to_proto_plus(
    message: Message | proto.Message,
) -> proto.Message: ...
def proto_copy_from(
    destination: proto.Message | Message, origin: proto.Message | Message
) -> None: ...
