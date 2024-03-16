from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v15.enums.types.geo_target_constant_status import (
    GeoTargetConstantStatusEnum,
)

_M = TypeVar("_M")

class GeoTargetConstant(proto.Message):
    resource_name: str
    id: int
    name: str
    country_code: str
    target_type: str
    status: GeoTargetConstantStatusEnum.GeoTargetConstantStatus
    canonical_name: str
    parent_geo_target: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        id: int = ...,
        name: str = ...,
        country_code: str = ...,
        target_type: str = ...,
        status: GeoTargetConstantStatusEnum.GeoTargetConstantStatus = ...,
        canonical_name: str = ...,
        parent_geo_target: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "resource_name",
            "id",
            "name",
            "country_code",
            "target_type",
            "status",
            "canonical_name",
            "parent_geo_target",
        ],
    ) -> bool: ...
