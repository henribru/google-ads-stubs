from typing import Any

import proto

from google.ads.googleads.v11.common.types.criteria import AudienceInfo

class AssetGroupSignal(proto.Message):
    resource_name: str
    asset_group: str
    audience: AudienceInfo
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        asset_group: str = ...,
        audience: AudienceInfo = ...
    ) -> None: ...
