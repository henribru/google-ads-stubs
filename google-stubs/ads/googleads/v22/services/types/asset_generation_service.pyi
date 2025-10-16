from collections.abc import MutableSequence
from google.ads.googleads.v22.enums.types.asset_field_type import AssetFieldTypeEnum
from google.ads.googleads.v22.enums.types.asset_field_type import AssetFieldTypeEnum
from collections.abc import MutableSequence
from google.ads.googleads.v22.enums.types.advertising_channel_type import AdvertisingChannelTypeEnum
from collections.abc import MutableSequence
from collections.abc import MutableSequence
from google.ads.googleads.v22.enums.types.asset_field_type import AssetFieldTypeEnum
from collections.abc import MutableSequence
from google.ads.googleads.v22.enums.types.advertising_channel_type import AdvertisingChannelTypeEnum
from collections.abc import MutableSequence
from google.ads.googleads.v22.enums.types.asset_field_type import AssetFieldTypeEnum
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class AssetGenerationExistingContext(proto.Message):
    existing_asset_group: str
    existing_ad_group_ad: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, existing_asset_group: str = ..., existing_ad_group_ad: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["existing_asset_group", "existing_ad_group_ad"]) -> bool: ...
class FinalUrlImageGenerationInput(proto.Message):
    final_url: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, final_url: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["final_url"]) -> bool: ...
class FreeformImageGenerationInput(proto.Message):
    freeform_prompt: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, freeform_prompt: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["freeform_prompt"]) -> bool: ...
class GenerateImagesRequest(proto.Message):
    customer_id: str
    asset_field_types: MutableSequence[AssetFieldTypeEnum.AssetFieldType]
    advertising_channel_type: AdvertisingChannelTypeEnum.AdvertisingChannelType
    final_url_generation: FinalUrlImageGenerationInput
    freeform_generation: FreeformImageGenerationInput
    product_recontext_generation: ProductRecontextGenerationImageInput
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, customer_id: str = ..., asset_field_types: MutableSequence[AssetFieldTypeEnum.AssetFieldType] = ..., advertising_channel_type: AdvertisingChannelTypeEnum.AdvertisingChannelType = ..., final_url_generation: FinalUrlImageGenerationInput = ..., freeform_generation: FreeformImageGenerationInput = ..., product_recontext_generation: ProductRecontextGenerationImageInput = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["customer_id", "asset_field_types", "advertising_channel_type", "final_url_generation", "freeform_generation", "product_recontext_generation"]) -> bool: ...
class GenerateImagesResponse(proto.Message):
    generated_images: MutableSequence[GeneratedImage]
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, generated_images: MutableSequence[GeneratedImage] = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["generated_images"]) -> bool: ...
class GenerateTextRequest(proto.Message):
    customer_id: str
    asset_field_types: MutableSequence[AssetFieldTypeEnum.AssetFieldType]
    final_url: str
    freeform_prompt: str
    keywords: MutableSequence[str]
    existing_generation_context: AssetGenerationExistingContext
    advertising_channel_type: AdvertisingChannelTypeEnum.AdvertisingChannelType
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, customer_id: str = ..., asset_field_types: MutableSequence[AssetFieldTypeEnum.AssetFieldType] = ..., final_url: str = ..., freeform_prompt: str = ..., keywords: MutableSequence[str] = ..., existing_generation_context: AssetGenerationExistingContext = ..., advertising_channel_type: AdvertisingChannelTypeEnum.AdvertisingChannelType = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["customer_id", "asset_field_types", "final_url", "freeform_prompt", "keywords", "existing_generation_context", "advertising_channel_type"]) -> bool: ...
class GenerateTextResponse(proto.Message):
    generated_text: MutableSequence[GeneratedText]
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, generated_text: MutableSequence[GeneratedText] = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["generated_text"]) -> bool: ...
class GeneratedImage(proto.Message):
    image_temporary_url: str
    asset_field_type: AssetFieldTypeEnum.AssetFieldType
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, image_temporary_url: str = ..., asset_field_type: AssetFieldTypeEnum.AssetFieldType = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["image_temporary_url", "asset_field_type"]) -> bool: ...
class GeneratedText(proto.Message):
    text: str
    asset_field_type: AssetFieldTypeEnum.AssetFieldType
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, text: str = ..., asset_field_type: AssetFieldTypeEnum.AssetFieldType = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["text", "asset_field_type"]) -> bool: ...
class ProductRecontextGenerationImageInput(proto.Message):
    prompt: str
    source_images: MutableSequence[SourceImage]
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, prompt: str = ..., source_images: MutableSequence[SourceImage] = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["prompt", "source_images"]) -> bool: ...
class SourceImage(proto.Message):
    image_data: bytes
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, image_data: bytes = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["image_data"]) -> bool: ...
