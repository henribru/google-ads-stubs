from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v15.enums.types.asset_set_link_status import (
    AssetSetLinkStatusEnum,
)

_M = TypeVar("_M")

class CustomerAssetSet(proto.Message):
    resource_name: str
    asset_set: str
    customer: str
    status: AssetSetLinkStatusEnum.AssetSetLinkStatus
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        asset_set: str = ...,
        customer: str = ...,
        status: AssetSetLinkStatusEnum.AssetSetLinkStatus = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["resource_name", "asset_set", "customer", "status"]
    ) -> bool: ...
