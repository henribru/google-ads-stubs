import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.enums.types import asset_field_type as gage_asset_field_type, call_to_action_type, hotel_asset_suggestion_status
from typing import MutableSequence

__protobuf__: Incomplete

class SuggestTravelAssetsRequest(proto.Message):
    customer_id: str
    language_option: str
    place_ids: MutableSequence[str]

class SuggestTravelAssetsResponse(proto.Message):
    hotel_asset_suggestions: MutableSequence['HotelAssetSuggestion']

class HotelAssetSuggestion(proto.Message):
    place_id: str
    final_url: str
    hotel_name: str
    call_to_action: call_to_action_type.CallToActionTypeEnum.CallToActionType
    text_assets: MutableSequence['HotelTextAsset']
    image_assets: MutableSequence['HotelImageAsset']
    status: hotel_asset_suggestion_status.HotelAssetSuggestionStatusEnum.HotelAssetSuggestionStatus

class HotelTextAsset(proto.Message):
    text: str
    asset_field_type: gage_asset_field_type.AssetFieldTypeEnum.AssetFieldType

class HotelImageAsset(proto.Message):
    uri: str
    asset_field_type: gage_asset_field_type.AssetFieldTypeEnum.AssetFieldType
