from typing import Any

import proto

from google.ads.googleads.v7.common.types import (
    criteria as criteria,
    feed_common as feed_common,
)
from google.ads.googleads.v7.enums.types import (
    lead_form_call_to_action_type as lead_form_call_to_action_type,
    lead_form_desired_intent as lead_form_desired_intent,
    lead_form_field_user_input_type as lead_form_field_user_input_type,
    lead_form_post_submit_call_to_action_type as lead_form_post_submit_call_to_action_type,
    promotion_extension_discount_modifier as promotion_extension_discount_modifier,
    promotion_extension_occasion as promotion_extension_occasion,
)

__protobuf__: Any

class YoutubeVideoAsset(proto.Message):
    youtube_video_id: Any
    youtube_video_title: Any

class MediaBundleAsset(proto.Message):
    data: Any

class ImageAsset(proto.Message):
    data: Any
    file_size: Any
    mime_type: Any
    full_size: Any

class ImageDimension(proto.Message):
    height_pixels: Any
    width_pixels: Any
    url: Any

class TextAsset(proto.Message):
    text: Any

class LeadFormAsset(proto.Message):
    business_name: Any
    call_to_action_type: Any
    call_to_action_description: Any
    headline: Any
    description: Any
    privacy_policy_url: Any
    post_submit_headline: Any
    post_submit_description: Any
    fields: Any
    delivery_methods: Any
    post_submit_call_to_action_type: Any
    background_image_asset: Any
    desired_intent: Any
    custom_disclosure: Any

class LeadFormField(proto.Message):
    input_type: Any
    single_choice_answers: Any

class LeadFormSingleChoiceAnswers(proto.Message):
    answers: Any

class LeadFormDeliveryMethod(proto.Message):
    webhook: Any

class WebhookDelivery(proto.Message):
    advertiser_webhook_url: Any
    google_secret: Any
    payload_schema_version: Any

class BookOnGoogleAsset(proto.Message): ...

class PromotionAsset(proto.Message):
    promotion_target: Any
    discount_modifier: Any
    redemption_start_date: Any
    redemption_end_date: Any
    occasion: Any
    language_code: Any
    start_date: Any
    end_date: Any
    ad_schedule_targets: Any
    percent_off: Any
    money_amount_off: Any
    promotion_code: Any
    orders_over_amount: Any

class CalloutAsset(proto.Message):
    callout_text: Any
    start_date: Any
    end_date: Any
    ad_schedule_targets: Any

class StructuredSnippetAsset(proto.Message):
    header: Any
    values: Any

class SitelinkAsset(proto.Message):
    link_text: Any
    description1: Any
    description2: Any
    start_date: Any
    end_date: Any
    ad_schedule_targets: Any
