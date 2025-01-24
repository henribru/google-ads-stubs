from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

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
        insertion_text: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "resource_name", "ad_group_criterion", "parameter_index", "insertion_text"
        ],
    ) -> bool: ...
