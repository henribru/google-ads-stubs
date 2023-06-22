from collections.abc import MutableSequence
from typing import Any

import proto

from google.ads.googleads.v14.enums.types.asset_field_type import AssetFieldTypeEnum
from google.ads.googleads.v14.enums.types.call_to_action_type import (
    CallToActionTypeEnum,
)
from google.ads.googleads.v14.enums.types.hotel_asset_suggestion_status import (
    HotelAssetSuggestionStatusEnum,
)

class HotelAssetSuggestion(proto.Message):
    place_id: str
    final_url: str
    hotel_name: str
    call_to_action: CallToActionTypeEnum.CallToActionType
    text_assets: MutableSequence[HotelTextAsset]
    image_assets: MutableSequence[HotelImageAsset]
    status: HotelAssetSuggestionStatusEnum.HotelAssetSuggestionStatus
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
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
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        uri: str = ...,
        asset_field_type: AssetFieldTypeEnum.AssetFieldType = ...
    ) -> None: ...

class HotelTextAsset(proto.Message):
    text: str
    asset_field_type: AssetFieldTypeEnum.AssetFieldType
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        text: str = ...,
        asset_field_type: AssetFieldTypeEnum.AssetFieldType = ...
    ) -> None: ...

class SuggestTravelAssetsRequest(proto.Message):
    customer_id: str
    language_option: str
    place_ids: MutableSequence[str]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        language_option: str = ...,
        place_ids: MutableSequence[str] = ...
    ) -> None: ...

class SuggestTravelAssetsResponse(proto.Message):
    hotel_asset_suggestions: MutableSequence[HotelAssetSuggestion]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        hotel_asset_suggestions: MutableSequence[HotelAssetSuggestion] = ...
    ) -> None: ...
