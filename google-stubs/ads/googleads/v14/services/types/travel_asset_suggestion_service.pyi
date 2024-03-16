from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v14.enums.types.asset_field_type import AssetFieldTypeEnum
from google.ads.googleads.v14.enums.types.call_to_action_type import (
    CallToActionTypeEnum,
)
from google.ads.googleads.v14.enums.types.hotel_asset_suggestion_status import (
    HotelAssetSuggestionStatusEnum,
)

_M = TypeVar("_M")

class HotelAssetSuggestion(proto.Message):
    place_id: str
    final_url: str
    hotel_name: str
    call_to_action: CallToActionTypeEnum.CallToActionType
    text_assets: MutableSequence[HotelTextAsset]
    image_assets: MutableSequence[HotelImageAsset]
    status: HotelAssetSuggestionStatusEnum.HotelAssetSuggestionStatus
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        place_id: str = ...,
        final_url: str = ...,
        hotel_name: str = ...,
        call_to_action: CallToActionTypeEnum.CallToActionType = ...,
        text_assets: MutableSequence[HotelTextAsset] = ...,
        image_assets: MutableSequence[HotelImageAsset] = ...,
        status: HotelAssetSuggestionStatusEnum.HotelAssetSuggestionStatus = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "place_id",
            "final_url",
            "hotel_name",
            "call_to_action",
            "text_assets",
            "image_assets",
            "status",
        ],
    ) -> bool: ...

class HotelImageAsset(proto.Message):
    uri: str
    asset_field_type: AssetFieldTypeEnum.AssetFieldType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        uri: str = ...,
        asset_field_type: AssetFieldTypeEnum.AssetFieldType = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["uri", "asset_field_type"]
    ) -> bool: ...

class HotelTextAsset(proto.Message):
    text: str
    asset_field_type: AssetFieldTypeEnum.AssetFieldType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        text: str = ...,
        asset_field_type: AssetFieldTypeEnum.AssetFieldType = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["text", "asset_field_type"]
    ) -> bool: ...

class SuggestTravelAssetsRequest(proto.Message):
    customer_id: str
    language_option: str
    place_ids: MutableSequence[str]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        language_option: str = ...,
        place_ids: MutableSequence[str] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["customer_id", "language_option", "place_ids"]
    ) -> bool: ...

class SuggestTravelAssetsResponse(proto.Message):
    hotel_asset_suggestions: MutableSequence[HotelAssetSuggestion]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        hotel_asset_suggestions: MutableSequence[HotelAssetSuggestion] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["hotel_asset_suggestions"]
    ) -> bool: ...
