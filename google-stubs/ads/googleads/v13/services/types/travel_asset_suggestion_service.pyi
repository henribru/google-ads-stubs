from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v13.enums.types.asset_field_type import AssetFieldTypeEnum
from google.ads.googleads.v13.enums.types.call_to_action_type import (
    CallToActionTypeEnum,
)
from google.ads.googleads.v13.enums.types.hotel_asset_suggestion_status import (
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
        status: HotelAssetSuggestionStatusEnum.HotelAssetSuggestionStatus = ...
    ) -> None: ...

class HotelImageAsset(proto.Message):
    uri: str
    asset_field_type: AssetFieldTypeEnum.AssetFieldType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        uri: str = ...,
        asset_field_type: AssetFieldTypeEnum.AssetFieldType = ...
    ) -> None: ...

class HotelTextAsset(proto.Message):
    text: str
    asset_field_type: AssetFieldTypeEnum.AssetFieldType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        text: str = ...,
        asset_field_type: AssetFieldTypeEnum.AssetFieldType = ...
    ) -> None: ...

class SuggestTravelAssetsRequest(proto.Message):
    customer_id: str
    language_option: str
    place_id: MutableSequence[str]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        language_option: str = ...,
        place_id: MutableSequence[str] = ...
    ) -> None: ...

class SuggestTravelAssetsResponse(proto.Message):
    hotel_asset_suggestions: MutableSequence[HotelAssetSuggestion]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        hotel_asset_suggestions: MutableSequence[HotelAssetSuggestion] = ...
    ) -> None: ...
