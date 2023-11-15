from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class AdParameter(proto.Message):
    resource_name: str
    ad_group_criterion: str
    parameter_index: int
    insertion_text: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        ad_group_criterion: str = ...,
        parameter_index: int = ...,
        insertion_text: str = ...
    ) -> None: ...
