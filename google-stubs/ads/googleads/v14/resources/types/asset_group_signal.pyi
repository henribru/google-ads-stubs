from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v14.common.types.criteria import AudienceInfo

_M = TypeVar("_M")

class AssetGroupSignal(proto.Message):
    resource_name: str
    asset_group: str
    audience: AudienceInfo
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        asset_group: str = ...,
        audience: AudienceInfo = ...
    ) -> None: ...
