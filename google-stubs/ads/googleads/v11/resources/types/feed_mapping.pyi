from typing import Any

import proto

from google.ads.googleads.v11.enums.types.ad_customizer_placeholder_field import (
    AdCustomizerPlaceholderFieldEnum,
)
from google.ads.googleads.v11.enums.types.affiliate_location_placeholder_field import (
    AffiliateLocationPlaceholderFieldEnum,
)
from google.ads.googleads.v11.enums.types.app_placeholder_field import (
    AppPlaceholderFieldEnum,
)
from google.ads.googleads.v11.enums.types.call_placeholder_field import (
    CallPlaceholderFieldEnum,
)
from google.ads.googleads.v11.enums.types.callout_placeholder_field import (
    CalloutPlaceholderFieldEnum,
)
from google.ads.googleads.v11.enums.types.custom_placeholder_field import (
    CustomPlaceholderFieldEnum,
)
from google.ads.googleads.v11.enums.types.dsa_page_feed_criterion_field import (
    DsaPageFeedCriterionFieldEnum,
)
from google.ads.googleads.v11.enums.types.education_placeholder_field import (
    EducationPlaceholderFieldEnum,
)
from google.ads.googleads.v11.enums.types.feed_mapping_criterion_type import (
    FeedMappingCriterionTypeEnum,
)
from google.ads.googleads.v11.enums.types.feed_mapping_status import (
    FeedMappingStatusEnum,
)
from google.ads.googleads.v11.enums.types.flight_placeholder_field import (
    FlightPlaceholderFieldEnum,
)
from google.ads.googleads.v11.enums.types.hotel_placeholder_field import (
    HotelPlaceholderFieldEnum,
)
from google.ads.googleads.v11.enums.types.image_placeholder_field import (
    ImagePlaceholderFieldEnum,
)
from google.ads.googleads.v11.enums.types.job_placeholder_field import (
    JobPlaceholderFieldEnum,
)
from google.ads.googleads.v11.enums.types.local_placeholder_field import (
    LocalPlaceholderFieldEnum,
)
from google.ads.googleads.v11.enums.types.location_extension_targeting_criterion_field import (
    LocationExtensionTargetingCriterionFieldEnum,
)
from google.ads.googleads.v11.enums.types.location_placeholder_field import (
    LocationPlaceholderFieldEnum,
)
from google.ads.googleads.v11.enums.types.message_placeholder_field import (
    MessagePlaceholderFieldEnum,
)
from google.ads.googleads.v11.enums.types.placeholder_type import PlaceholderTypeEnum
from google.ads.googleads.v11.enums.types.price_placeholder_field import (
    PricePlaceholderFieldEnum,
)
from google.ads.googleads.v11.enums.types.promotion_placeholder_field import (
    PromotionPlaceholderFieldEnum,
)
from google.ads.googleads.v11.enums.types.real_estate_placeholder_field import (
    RealEstatePlaceholderFieldEnum,
)
from google.ads.googleads.v11.enums.types.sitelink_placeholder_field import (
    SitelinkPlaceholderFieldEnum,
)
from google.ads.googleads.v11.enums.types.structured_snippet_placeholder_field import (
    StructuredSnippetPlaceholderFieldEnum,
)
from google.ads.googleads.v11.enums.types.travel_placeholder_field import (
    TravelPlaceholderFieldEnum,
)

class AttributeFieldMapping(proto.Message):
    feed_attribute_id: int
    field_id: int
    sitelink_field: SitelinkPlaceholderFieldEnum.SitelinkPlaceholderField
    call_field: CallPlaceholderFieldEnum.CallPlaceholderField
    app_field: AppPlaceholderFieldEnum.AppPlaceholderField
    location_field: LocationPlaceholderFieldEnum.LocationPlaceholderField
    affiliate_location_field: AffiliateLocationPlaceholderFieldEnum.AffiliateLocationPlaceholderField
    callout_field: CalloutPlaceholderFieldEnum.CalloutPlaceholderField
    structured_snippet_field: StructuredSnippetPlaceholderFieldEnum.StructuredSnippetPlaceholderField
    message_field: MessagePlaceholderFieldEnum.MessagePlaceholderField
    price_field: PricePlaceholderFieldEnum.PricePlaceholderField
    promotion_field: PromotionPlaceholderFieldEnum.PromotionPlaceholderField
    ad_customizer_field: AdCustomizerPlaceholderFieldEnum.AdCustomizerPlaceholderField
    dsa_page_feed_field: DsaPageFeedCriterionFieldEnum.DsaPageFeedCriterionField
    location_extension_targeting_field: LocationExtensionTargetingCriterionFieldEnum.LocationExtensionTargetingCriterionField
    education_field: EducationPlaceholderFieldEnum.EducationPlaceholderField
    flight_field: FlightPlaceholderFieldEnum.FlightPlaceholderField
    custom_field: CustomPlaceholderFieldEnum.CustomPlaceholderField
    hotel_field: HotelPlaceholderFieldEnum.HotelPlaceholderField
    real_estate_field: RealEstatePlaceholderFieldEnum.RealEstatePlaceholderField
    travel_field: TravelPlaceholderFieldEnum.TravelPlaceholderField
    local_field: LocalPlaceholderFieldEnum.LocalPlaceholderField
    job_field: JobPlaceholderFieldEnum.JobPlaceholderField
    image_field: ImagePlaceholderFieldEnum.ImagePlaceholderField
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        feed_attribute_id: int = ...,
        field_id: int = ...,
        sitelink_field: SitelinkPlaceholderFieldEnum.SitelinkPlaceholderField = ...,
        call_field: CallPlaceholderFieldEnum.CallPlaceholderField = ...,
        app_field: AppPlaceholderFieldEnum.AppPlaceholderField = ...,
        location_field: LocationPlaceholderFieldEnum.LocationPlaceholderField = ...,
        affiliate_location_field: AffiliateLocationPlaceholderFieldEnum.AffiliateLocationPlaceholderField = ...,
        callout_field: CalloutPlaceholderFieldEnum.CalloutPlaceholderField = ...,
        structured_snippet_field: StructuredSnippetPlaceholderFieldEnum.StructuredSnippetPlaceholderField = ...,
        message_field: MessagePlaceholderFieldEnum.MessagePlaceholderField = ...,
        price_field: PricePlaceholderFieldEnum.PricePlaceholderField = ...,
        promotion_field: PromotionPlaceholderFieldEnum.PromotionPlaceholderField = ...,
        ad_customizer_field: AdCustomizerPlaceholderFieldEnum.AdCustomizerPlaceholderField = ...,
        dsa_page_feed_field: DsaPageFeedCriterionFieldEnum.DsaPageFeedCriterionField = ...,
        location_extension_targeting_field: LocationExtensionTargetingCriterionFieldEnum.LocationExtensionTargetingCriterionField = ...,
        education_field: EducationPlaceholderFieldEnum.EducationPlaceholderField = ...,
        flight_field: FlightPlaceholderFieldEnum.FlightPlaceholderField = ...,
        custom_field: CustomPlaceholderFieldEnum.CustomPlaceholderField = ...,
        hotel_field: HotelPlaceholderFieldEnum.HotelPlaceholderField = ...,
        real_estate_field: RealEstatePlaceholderFieldEnum.RealEstatePlaceholderField = ...,
        travel_field: TravelPlaceholderFieldEnum.TravelPlaceholderField = ...,
        local_field: LocalPlaceholderFieldEnum.LocalPlaceholderField = ...,
        job_field: JobPlaceholderFieldEnum.JobPlaceholderField = ...,
        image_field: ImagePlaceholderFieldEnum.ImagePlaceholderField = ...
    ) -> None: ...

class FeedMapping(proto.Message):
    resource_name: str
    feed: str
    attribute_field_mappings: list[AttributeFieldMapping]
    status: FeedMappingStatusEnum.FeedMappingStatus
    placeholder_type: PlaceholderTypeEnum.PlaceholderType
    criterion_type: FeedMappingCriterionTypeEnum.FeedMappingCriterionType
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        feed: str = ...,
        attribute_field_mappings: list[AttributeFieldMapping] = ...,
        status: FeedMappingStatusEnum.FeedMappingStatus = ...,
        placeholder_type: PlaceholderTypeEnum.PlaceholderType = ...,
        criterion_type: FeedMappingCriterionTypeEnum.FeedMappingCriterionType = ...
    ) -> None: ...
