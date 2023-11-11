from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class AdGroupCriterionLabel(proto.Message):
    resource_name: str
    ad_group_criterion: str
    label: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        ad_group_criterion: str = ...,
        label: str = ...
    ) -> None: ...
