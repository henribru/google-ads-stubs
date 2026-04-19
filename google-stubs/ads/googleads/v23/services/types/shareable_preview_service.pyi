from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from google.rpc.status_pb2 import Status
from typing_extensions import Literal

from google.ads.googleads.v23.enums.types.preview_type import PreviewTypeEnum

_M = TypeVar("_M")

class AssetGroupIdentifier(proto.Message):
    asset_group_id: int
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        asset_group_id: int = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["asset_group_id"]
    ) -> bool: ...

class GenerateShareablePreviewsRequest(proto.Message):
    customer_id: str
    shareable_previews: MutableSequence[ShareablePreview]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        shareable_previews: MutableSequence[ShareablePreview] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["customer_id", "shareable_previews"]
    ) -> bool: ...

class GenerateShareablePreviewsResponse(proto.Message):
    responses: MutableSequence[ShareablePreviewOrError]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        responses: MutableSequence[ShareablePreviewOrError] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["responses"]
    ) -> bool: ...

class ShareablePreview(proto.Message):
    asset_group_identifier: AssetGroupIdentifier
    preview_type: PreviewTypeEnum.PreviewType
    ad_group_ad: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        asset_group_identifier: AssetGroupIdentifier = ...,
        preview_type: PreviewTypeEnum.PreviewType = ...,
        ad_group_ad: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["asset_group_identifier", "preview_type", "ad_group_ad"]
    ) -> bool: ...

class ShareablePreviewOrError(proto.Message):
    asset_group_identifier: AssetGroupIdentifier
    shareable_preview_result: ShareablePreviewResult
    partial_failure_error: Status
    ad_group_ad: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        asset_group_identifier: AssetGroupIdentifier = ...,
        shareable_preview_result: ShareablePreviewResult = ...,
        partial_failure_error: Status = ...,
        ad_group_ad: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "asset_group_identifier",
            "shareable_preview_result",
            "partial_failure_error",
            "ad_group_ad",
        ],
    ) -> bool: ...

class ShareablePreviewResult(proto.Message):
    shareable_preview_url: str
    expiration_date_time: str
    youtube_live_preview_result: YouTubeLivePreviewResult
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        shareable_preview_url: str = ...,
        expiration_date_time: str = ...,
        youtube_live_preview_result: YouTubeLivePreviewResult = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "shareable_preview_url",
            "expiration_date_time",
            "youtube_live_preview_result",
        ],
    ) -> bool: ...

class YouTubeLivePreviewResult(proto.Message):
    youtube_preview_url: str
    youtube_tv_preview_url: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        youtube_preview_url: str = ...,
        youtube_tv_preview_url: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["youtube_preview_url", "youtube_tv_preview_url"]
    ) -> bool: ...
