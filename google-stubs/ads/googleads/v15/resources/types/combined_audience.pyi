from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v15.enums.types.combined_audience_status import (
    CombinedAudienceStatusEnum,
)

_M = TypeVar("_M")

class CombinedAudience(proto.Message):
    resource_name: str
    id: int
    status: CombinedAudienceStatusEnum.CombinedAudienceStatus
    name: str
    description: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        id: int = ...,
        status: CombinedAudienceStatusEnum.CombinedAudienceStatus = ...,
        name: str = ...,
        description: str = ...
    ) -> None: ...
