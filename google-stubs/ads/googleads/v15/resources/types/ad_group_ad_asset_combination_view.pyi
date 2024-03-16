from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v15.common.types.asset_usage import AssetUsage

_M = TypeVar("_M")

class AdGroupAdAssetCombinationView(proto.Message):
    resource_name: str
    served_assets: MutableSequence[AssetUsage]
    enabled: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        served_assets: MutableSequence[AssetUsage] = ...,
        enabled: bool = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["resource_name", "served_assets", "enabled"]
    ) -> bool: ...
