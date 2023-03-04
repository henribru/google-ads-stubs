from collections.abc import MutableSequence
from typing import Any

import proto

from google.ads.googleads.v13.common.types.asset_usage import AssetUsage

class AdGroupAdAssetCombinationView(proto.Message):
    resource_name: str
    served_assets: MutableSequence[AssetUsage]
    enabled: bool
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        served_assets: MutableSequence[AssetUsage] = ...,
        enabled: bool = ...
    ) -> None: ...
