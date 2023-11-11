from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v13.common.types.asset_usage import AssetUsage

_M = TypeVar("_M")

class AdGroupAdAssetCombinationView(proto.Message):
    resource_name: str
    served_assets: MutableSequence[AssetUsage]
    enabled: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        served_assets: MutableSequence[AssetUsage] = ...,
        enabled: bool = ...
    ) -> None: ...
