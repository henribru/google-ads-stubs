from typing import TypeVar

from google.protobuf.message import Message

from google.ads.googleads.util import (
    convert_proto_plus_to_protobuf as convert_proto_plus_to_protobuf,
    get_nested_attr as get_nested_attr,
    proto_copy_from as proto_copy_from,
    set_nested_message_field as set_nested_message_field,
)

_M = TypeVar("_M", bound=Message)

def mask_message(message: _M, mask: str) -> _M: ...
