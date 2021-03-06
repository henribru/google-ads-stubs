# @generated by mypy-protobuf.  Do not edit manually!
import sys
from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Text as typing___Text,
    overload as typing___overload,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)
from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
)
from google.protobuf.message import Message as google___protobuf___message___Message
from typing_extensions import Literal as typing_extensions___Literal

from google.ads.google_ads.v6.proto.enums.lead_form_call_to_action_type_pb2 import (
    LeadFormCallToActionTypeEnum as google___ads___googleads___v6___enums___lead_form_call_to_action_type_pb2___LeadFormCallToActionTypeEnum,
)
from google.ads.google_ads.v6.proto.enums.lead_form_desired_intent_pb2 import (
    LeadFormDesiredIntentEnum as google___ads___googleads___v6___enums___lead_form_desired_intent_pb2___LeadFormDesiredIntentEnum,
)
from google.ads.google_ads.v6.proto.enums.lead_form_field_user_input_type_pb2 import (
    LeadFormFieldUserInputTypeEnum as google___ads___googleads___v6___enums___lead_form_field_user_input_type_pb2___LeadFormFieldUserInputTypeEnum,
)
from google.ads.google_ads.v6.proto.enums.lead_form_post_submit_call_to_action_type_pb2 import (
    LeadFormPostSubmitCallToActionTypeEnum as google___ads___googleads___v6___enums___lead_form_post_submit_call_to_action_type_pb2___LeadFormPostSubmitCallToActionTypeEnum,
)
from google.ads.google_ads.v6.proto.enums.mime_type_pb2 import (
    MimeTypeEnum as google___ads___googleads___v6___enums___mime_type_pb2___MimeTypeEnum,
)

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class YoutubeVideoAsset(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    youtube_video_id: typing___Text = ...
    def __init__(
        self, *, youtube_video_id: typing___Optional[typing___Text] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "_youtube_video_id",
            b"_youtube_video_id",
            "youtube_video_id",
            b"youtube_video_id",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "_youtube_video_id",
            b"_youtube_video_id",
            "youtube_video_id",
            b"youtube_video_id",
        ],
    ) -> None: ...
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "_youtube_video_id", b"_youtube_video_id"
        ],
    ) -> typing_extensions___Literal["youtube_video_id"]: ...

type___YoutubeVideoAsset = YoutubeVideoAsset

class MediaBundleAsset(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    data: builtin___bytes = ...
    def __init__(self, *, data: typing___Optional[builtin___bytes] = None,) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal["_data", b"_data", "data", b"data"],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal["_data", b"_data", "data", b"data"],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["_data", b"_data"]
    ) -> typing_extensions___Literal["data"]: ...

type___MediaBundleAsset = MediaBundleAsset

class ImageAsset(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    data: builtin___bytes = ...
    file_size: builtin___int = ...
    mime_type: google___ads___googleads___v6___enums___mime_type_pb2___MimeTypeEnum.MimeTypeValue = ...
    @property
    def full_size(self) -> type___ImageDimension: ...
    def __init__(
        self,
        *,
        data: typing___Optional[builtin___bytes] = None,
        file_size: typing___Optional[builtin___int] = None,
        mime_type: typing___Optional[
            google___ads___googleads___v6___enums___mime_type_pb2___MimeTypeEnum.MimeTypeValue
        ] = None,
        full_size: typing___Optional[type___ImageDimension] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "_data",
            b"_data",
            "_file_size",
            b"_file_size",
            "data",
            b"data",
            "file_size",
            b"file_size",
            "full_size",
            b"full_size",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "_data",
            b"_data",
            "_file_size",
            b"_file_size",
            "data",
            b"data",
            "file_size",
            b"file_size",
            "full_size",
            b"full_size",
            "mime_type",
            b"mime_type",
        ],
    ) -> None: ...
    @typing___overload
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["_data", b"_data"]
    ) -> typing_extensions___Literal["data"]: ...
    @typing___overload
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["_file_size", b"_file_size"]
    ) -> typing_extensions___Literal["file_size"]: ...

type___ImageAsset = ImageAsset

class ImageDimension(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    height_pixels: builtin___int = ...
    width_pixels: builtin___int = ...
    url: typing___Text = ...
    def __init__(
        self,
        *,
        height_pixels: typing___Optional[builtin___int] = None,
        width_pixels: typing___Optional[builtin___int] = None,
        url: typing___Optional[typing___Text] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "_height_pixels",
            b"_height_pixels",
            "_url",
            b"_url",
            "_width_pixels",
            b"_width_pixels",
            "height_pixels",
            b"height_pixels",
            "url",
            b"url",
            "width_pixels",
            b"width_pixels",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "_height_pixels",
            b"_height_pixels",
            "_url",
            b"_url",
            "_width_pixels",
            b"_width_pixels",
            "height_pixels",
            b"height_pixels",
            "url",
            b"url",
            "width_pixels",
            b"width_pixels",
        ],
    ) -> None: ...
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal["_height_pixels", b"_height_pixels"],
    ) -> typing_extensions___Literal["height_pixels"]: ...
    @typing___overload
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["_url", b"_url"]
    ) -> typing_extensions___Literal["url"]: ...
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal["_width_pixels", b"_width_pixels"],
    ) -> typing_extensions___Literal["width_pixels"]: ...

type___ImageDimension = ImageDimension

class TextAsset(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    text: typing___Text = ...
    def __init__(self, *, text: typing___Optional[typing___Text] = None,) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal["_text", b"_text", "text", b"text"],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal["_text", b"_text", "text", b"text"],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["_text", b"_text"]
    ) -> typing_extensions___Literal["text"]: ...

type___TextAsset = TextAsset

class LeadFormAsset(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    business_name: typing___Text = ...
    call_to_action_type: google___ads___googleads___v6___enums___lead_form_call_to_action_type_pb2___LeadFormCallToActionTypeEnum.LeadFormCallToActionTypeValue = ...
    call_to_action_description: typing___Text = ...
    headline: typing___Text = ...
    description: typing___Text = ...
    privacy_policy_url: typing___Text = ...
    post_submit_headline: typing___Text = ...
    post_submit_description: typing___Text = ...
    post_submit_call_to_action_type: google___ads___googleads___v6___enums___lead_form_post_submit_call_to_action_type_pb2___LeadFormPostSubmitCallToActionTypeEnum.LeadFormPostSubmitCallToActionTypeValue = ...
    background_image_asset: typing___Text = ...
    desired_intent: google___ads___googleads___v6___enums___lead_form_desired_intent_pb2___LeadFormDesiredIntentEnum.LeadFormDesiredIntentValue = ...
    custom_disclosure: typing___Text = ...
    @property
    def fields(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        type___LeadFormField
    ]: ...
    @property
    def delivery_methods(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        type___LeadFormDeliveryMethod
    ]: ...
    def __init__(
        self,
        *,
        business_name: typing___Optional[typing___Text] = None,
        call_to_action_type: typing___Optional[
            google___ads___googleads___v6___enums___lead_form_call_to_action_type_pb2___LeadFormCallToActionTypeEnum.LeadFormCallToActionTypeValue
        ] = None,
        call_to_action_description: typing___Optional[typing___Text] = None,
        headline: typing___Optional[typing___Text] = None,
        description: typing___Optional[typing___Text] = None,
        privacy_policy_url: typing___Optional[typing___Text] = None,
        post_submit_headline: typing___Optional[typing___Text] = None,
        post_submit_description: typing___Optional[typing___Text] = None,
        fields: typing___Optional[typing___Iterable[type___LeadFormField]] = None,
        delivery_methods: typing___Optional[
            typing___Iterable[type___LeadFormDeliveryMethod]
        ] = None,
        post_submit_call_to_action_type: typing___Optional[
            google___ads___googleads___v6___enums___lead_form_post_submit_call_to_action_type_pb2___LeadFormPostSubmitCallToActionTypeEnum.LeadFormPostSubmitCallToActionTypeValue
        ] = None,
        background_image_asset: typing___Optional[typing___Text] = None,
        desired_intent: typing___Optional[
            google___ads___googleads___v6___enums___lead_form_desired_intent_pb2___LeadFormDesiredIntentEnum.LeadFormDesiredIntentValue
        ] = None,
        custom_disclosure: typing___Optional[typing___Text] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "_background_image_asset",
            b"_background_image_asset",
            "_custom_disclosure",
            b"_custom_disclosure",
            "_post_submit_description",
            b"_post_submit_description",
            "_post_submit_headline",
            b"_post_submit_headline",
            "background_image_asset",
            b"background_image_asset",
            "custom_disclosure",
            b"custom_disclosure",
            "post_submit_description",
            b"post_submit_description",
            "post_submit_headline",
            b"post_submit_headline",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "_background_image_asset",
            b"_background_image_asset",
            "_custom_disclosure",
            b"_custom_disclosure",
            "_post_submit_description",
            b"_post_submit_description",
            "_post_submit_headline",
            b"_post_submit_headline",
            "background_image_asset",
            b"background_image_asset",
            "business_name",
            b"business_name",
            "call_to_action_description",
            b"call_to_action_description",
            "call_to_action_type",
            b"call_to_action_type",
            "custom_disclosure",
            b"custom_disclosure",
            "delivery_methods",
            b"delivery_methods",
            "description",
            b"description",
            "desired_intent",
            b"desired_intent",
            "fields",
            b"fields",
            "headline",
            b"headline",
            "post_submit_call_to_action_type",
            b"post_submit_call_to_action_type",
            "post_submit_description",
            b"post_submit_description",
            "post_submit_headline",
            b"post_submit_headline",
            "privacy_policy_url",
            b"privacy_policy_url",
        ],
    ) -> None: ...
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "_background_image_asset", b"_background_image_asset"
        ],
    ) -> typing_extensions___Literal["background_image_asset"]: ...
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "_custom_disclosure", b"_custom_disclosure"
        ],
    ) -> typing_extensions___Literal["custom_disclosure"]: ...
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "_post_submit_description", b"_post_submit_description"
        ],
    ) -> typing_extensions___Literal["post_submit_description"]: ...
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "_post_submit_headline", b"_post_submit_headline"
        ],
    ) -> typing_extensions___Literal["post_submit_headline"]: ...

type___LeadFormAsset = LeadFormAsset

class LeadFormField(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    input_type: google___ads___googleads___v6___enums___lead_form_field_user_input_type_pb2___LeadFormFieldUserInputTypeEnum.LeadFormFieldUserInputTypeValue = ...
    @property
    def single_choice_answers(self) -> type___LeadFormSingleChoiceAnswers: ...
    def __init__(
        self,
        *,
        input_type: typing___Optional[
            google___ads___googleads___v6___enums___lead_form_field_user_input_type_pb2___LeadFormFieldUserInputTypeEnum.LeadFormFieldUserInputTypeValue
        ] = None,
        single_choice_answers: typing___Optional[
            type___LeadFormSingleChoiceAnswers
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "answers", b"answers", "single_choice_answers", b"single_choice_answers"
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "answers",
            b"answers",
            "input_type",
            b"input_type",
            "single_choice_answers",
            b"single_choice_answers",
        ],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["answers", b"answers"]
    ) -> typing_extensions___Literal["single_choice_answers"]: ...

type___LeadFormField = LeadFormField

class LeadFormSingleChoiceAnswers(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    answers: google___protobuf___internal___containers___RepeatedScalarFieldContainer[
        typing___Text
    ] = ...
    def __init__(
        self, *, answers: typing___Optional[typing___Iterable[typing___Text]] = None,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["answers", b"answers"]
    ) -> None: ...

type___LeadFormSingleChoiceAnswers = LeadFormSingleChoiceAnswers

class LeadFormDeliveryMethod(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def webhook(self) -> type___WebhookDelivery: ...
    def __init__(
        self, *, webhook: typing___Optional[type___WebhookDelivery] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "delivery_details", b"delivery_details", "webhook", b"webhook"
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "delivery_details", b"delivery_details", "webhook", b"webhook"
        ],
    ) -> None: ...
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "delivery_details", b"delivery_details"
        ],
    ) -> typing_extensions___Literal["webhook"]: ...

type___LeadFormDeliveryMethod = LeadFormDeliveryMethod

class WebhookDelivery(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    advertiser_webhook_url: typing___Text = ...
    google_secret: typing___Text = ...
    payload_schema_version: builtin___int = ...
    def __init__(
        self,
        *,
        advertiser_webhook_url: typing___Optional[typing___Text] = None,
        google_secret: typing___Optional[typing___Text] = None,
        payload_schema_version: typing___Optional[builtin___int] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "_advertiser_webhook_url",
            b"_advertiser_webhook_url",
            "_google_secret",
            b"_google_secret",
            "_payload_schema_version",
            b"_payload_schema_version",
            "advertiser_webhook_url",
            b"advertiser_webhook_url",
            "google_secret",
            b"google_secret",
            "payload_schema_version",
            b"payload_schema_version",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "_advertiser_webhook_url",
            b"_advertiser_webhook_url",
            "_google_secret",
            b"_google_secret",
            "_payload_schema_version",
            b"_payload_schema_version",
            "advertiser_webhook_url",
            b"advertiser_webhook_url",
            "google_secret",
            b"google_secret",
            "payload_schema_version",
            b"payload_schema_version",
        ],
    ) -> None: ...
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "_advertiser_webhook_url", b"_advertiser_webhook_url"
        ],
    ) -> typing_extensions___Literal["advertiser_webhook_url"]: ...
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal["_google_secret", b"_google_secret"],
    ) -> typing_extensions___Literal["google_secret"]: ...
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "_payload_schema_version", b"_payload_schema_version"
        ],
    ) -> typing_extensions___Literal["payload_schema_version"]: ...

type___WebhookDelivery = WebhookDelivery

class BookOnGoogleAsset(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    def __init__(self,) -> None: ...

type___BookOnGoogleAsset = BookOnGoogleAsset
