from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v24.enums.types.preview_type import PreviewTypeEnum

_M = TypeVar("_M")

class GenerateShareablePreviewsOperation(proto.Message):
    shareable_previews: MutableSequence[ShareablePreview]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        shareable_previews: MutableSequence[ShareablePreview] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["shareable_previews"]
    ) -> bool: ...

class GenerateShareablePreviewsResult(proto.Message):
    previews: MutableSequence[ShareablePreviewResult]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        previews: MutableSequence[ShareablePreviewResult] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["previews"]
    ) -> bool: ...

class ShareablePreview(proto.Message):
    preview_type: PreviewTypeEnum.PreviewType
    ad_group_ad: str
    asset_group: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        preview_type: PreviewTypeEnum.PreviewType = ...,
        ad_group_ad: str = ...,
        asset_group: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["preview_type", "ad_group_ad", "asset_group"]
    ) -> bool: ...

class ShareablePreviewResult(proto.Message):
    expiration_date_time: str
    ui_preview_result: UiPreviewResult
    youtube_live_preview_result: YouTubeLivePreviewResult
    ad_group_ad: str
    asset_group: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        expiration_date_time: str = ...,
        ui_preview_result: UiPreviewResult = ...,
        youtube_live_preview_result: YouTubeLivePreviewResult = ...,
        ad_group_ad: str = ...,
        asset_group: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "expiration_date_time",
            "ui_preview_result",
            "youtube_live_preview_result",
            "ad_group_ad",
            "asset_group",
        ],
    ) -> bool: ...

class UiPreviewResult(proto.Message):
    shareable_preview_url: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        shareable_preview_url: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["shareable_preview_url"]
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
