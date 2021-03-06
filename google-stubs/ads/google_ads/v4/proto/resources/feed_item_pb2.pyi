"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.ads.google_ads.v4.proto.common.custom_parameter_pb2
import google.ads.google_ads.v4.proto.common.feed_common_pb2
import google.ads.google_ads.v4.proto.common.policy_pb2
import google.ads.google_ads.v4.proto.enums.feed_item_quality_approval_status_pb2
import google.ads.google_ads.v4.proto.enums.feed_item_quality_disapproval_reason_pb2
import google.ads.google_ads.v4.proto.enums.feed_item_status_pb2
import google.ads.google_ads.v4.proto.enums.feed_item_validation_status_pb2
import google.ads.google_ads.v4.proto.enums.geo_targeting_restriction_pb2
import google.ads.google_ads.v4.proto.enums.placeholder_type_pb2
import google.ads.google_ads.v4.proto.enums.policy_approval_status_pb2
import google.ads.google_ads.v4.proto.enums.policy_review_status_pb2
import google.ads.google_ads.v4.proto.errors.feed_item_validation_error_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.wrappers_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class FeedItem(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    FEED_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    START_DATE_TIME_FIELD_NUMBER: builtins.int
    END_DATE_TIME_FIELD_NUMBER: builtins.int
    ATTRIBUTE_VALUES_FIELD_NUMBER: builtins.int
    GEO_TARGETING_RESTRICTION_FIELD_NUMBER: builtins.int
    URL_CUSTOM_PARAMETERS_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    POLICY_INFOS_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    geo_targeting_restriction: google.ads.google_ads.v4.proto.enums.geo_targeting_restriction_pb2.GeoTargetingRestrictionEnum.GeoTargetingRestriction.V = (
        ...
    )
    status: google.ads.google_ads.v4.proto.enums.feed_item_status_pb2.FeedItemStatusEnum.FeedItemStatus.V = (
        ...
    )
    @property
    def feed(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def id(self) -> google.protobuf.wrappers_pb2.Int64Value: ...
    @property
    def start_date_time(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def end_date_time(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def attribute_values(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___FeedItemAttributeValue
    ]: ...
    @property
    def url_custom_parameters(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        google.ads.google_ads.v4.proto.common.custom_parameter_pb2.CustomParameter
    ]: ...
    @property
    def policy_infos(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___FeedItemPlaceholderPolicyInfo
    ]: ...
    def __init__(
        self,
        *,
        resource_name: typing.Text = ...,
        feed: typing.Optional[google.protobuf.wrappers_pb2.StringValue] = ...,
        id: typing.Optional[google.protobuf.wrappers_pb2.Int64Value] = ...,
        start_date_time: typing.Optional[
            google.protobuf.wrappers_pb2.StringValue
        ] = ...,
        end_date_time: typing.Optional[google.protobuf.wrappers_pb2.StringValue] = ...,
        attribute_values: typing.Optional[
            typing.Iterable[global___FeedItemAttributeValue]
        ] = ...,
        geo_targeting_restriction: google.ads.google_ads.v4.proto.enums.geo_targeting_restriction_pb2.GeoTargetingRestrictionEnum.GeoTargetingRestriction.V = ...,
        url_custom_parameters: typing.Optional[
            typing.Iterable[
                google.ads.google_ads.v4.proto.common.custom_parameter_pb2.CustomParameter
            ]
        ] = ...,
        status: google.ads.google_ads.v4.proto.enums.feed_item_status_pb2.FeedItemStatusEnum.FeedItemStatus.V = ...,
        policy_infos: typing.Optional[
            typing.Iterable[global___FeedItemPlaceholderPolicyInfo]
        ] = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "end_date_time",
            b"end_date_time",
            "feed",
            b"feed",
            "id",
            b"id",
            "start_date_time",
            b"start_date_time",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "attribute_values",
            b"attribute_values",
            "end_date_time",
            b"end_date_time",
            "feed",
            b"feed",
            "geo_targeting_restriction",
            b"geo_targeting_restriction",
            "id",
            b"id",
            "policy_infos",
            b"policy_infos",
            "resource_name",
            b"resource_name",
            "start_date_time",
            b"start_date_time",
            "status",
            b"status",
            "url_custom_parameters",
            b"url_custom_parameters",
        ],
    ) -> None: ...

global___FeedItem = FeedItem

class FeedItemAttributeValue(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    FEED_ATTRIBUTE_ID_FIELD_NUMBER: builtins.int
    INTEGER_VALUE_FIELD_NUMBER: builtins.int
    BOOLEAN_VALUE_FIELD_NUMBER: builtins.int
    STRING_VALUE_FIELD_NUMBER: builtins.int
    DOUBLE_VALUE_FIELD_NUMBER: builtins.int
    PRICE_VALUE_FIELD_NUMBER: builtins.int
    INTEGER_VALUES_FIELD_NUMBER: builtins.int
    BOOLEAN_VALUES_FIELD_NUMBER: builtins.int
    STRING_VALUES_FIELD_NUMBER: builtins.int
    DOUBLE_VALUES_FIELD_NUMBER: builtins.int
    @property
    def feed_attribute_id(self) -> google.protobuf.wrappers_pb2.Int64Value: ...
    @property
    def integer_value(self) -> google.protobuf.wrappers_pb2.Int64Value: ...
    @property
    def boolean_value(self) -> google.protobuf.wrappers_pb2.BoolValue: ...
    @property
    def string_value(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def double_value(self) -> google.protobuf.wrappers_pb2.DoubleValue: ...
    @property
    def price_value(
        self,
    ) -> google.ads.google_ads.v4.proto.common.feed_common_pb2.Money: ...
    @property
    def integer_values(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        google.protobuf.wrappers_pb2.Int64Value
    ]: ...
    @property
    def boolean_values(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        google.protobuf.wrappers_pb2.BoolValue
    ]: ...
    @property
    def string_values(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        google.protobuf.wrappers_pb2.StringValue
    ]: ...
    @property
    def double_values(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        google.protobuf.wrappers_pb2.DoubleValue
    ]: ...
    def __init__(
        self,
        *,
        feed_attribute_id: typing.Optional[
            google.protobuf.wrappers_pb2.Int64Value
        ] = ...,
        integer_value: typing.Optional[google.protobuf.wrappers_pb2.Int64Value] = ...,
        boolean_value: typing.Optional[google.protobuf.wrappers_pb2.BoolValue] = ...,
        string_value: typing.Optional[google.protobuf.wrappers_pb2.StringValue] = ...,
        double_value: typing.Optional[google.protobuf.wrappers_pb2.DoubleValue] = ...,
        price_value: typing.Optional[
            google.ads.google_ads.v4.proto.common.feed_common_pb2.Money
        ] = ...,
        integer_values: typing.Optional[
            typing.Iterable[google.protobuf.wrappers_pb2.Int64Value]
        ] = ...,
        boolean_values: typing.Optional[
            typing.Iterable[google.protobuf.wrappers_pb2.BoolValue]
        ] = ...,
        string_values: typing.Optional[
            typing.Iterable[google.protobuf.wrappers_pb2.StringValue]
        ] = ...,
        double_values: typing.Optional[
            typing.Iterable[google.protobuf.wrappers_pb2.DoubleValue]
        ] = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "boolean_value",
            b"boolean_value",
            "double_value",
            b"double_value",
            "feed_attribute_id",
            b"feed_attribute_id",
            "integer_value",
            b"integer_value",
            "price_value",
            b"price_value",
            "string_value",
            b"string_value",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "boolean_value",
            b"boolean_value",
            "boolean_values",
            b"boolean_values",
            "double_value",
            b"double_value",
            "double_values",
            b"double_values",
            "feed_attribute_id",
            b"feed_attribute_id",
            "integer_value",
            b"integer_value",
            "integer_values",
            b"integer_values",
            "price_value",
            b"price_value",
            "string_value",
            b"string_value",
            "string_values",
            b"string_values",
        ],
    ) -> None: ...

global___FeedItemAttributeValue = FeedItemAttributeValue

class FeedItemPlaceholderPolicyInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PLACEHOLDER_TYPE_ENUM_FIELD_NUMBER: builtins.int
    FEED_MAPPING_RESOURCE_NAME_FIELD_NUMBER: builtins.int
    REVIEW_STATUS_FIELD_NUMBER: builtins.int
    APPROVAL_STATUS_FIELD_NUMBER: builtins.int
    POLICY_TOPIC_ENTRIES_FIELD_NUMBER: builtins.int
    VALIDATION_STATUS_FIELD_NUMBER: builtins.int
    VALIDATION_ERRORS_FIELD_NUMBER: builtins.int
    QUALITY_APPROVAL_STATUS_FIELD_NUMBER: builtins.int
    QUALITY_DISAPPROVAL_REASONS_FIELD_NUMBER: builtins.int
    placeholder_type_enum: google.ads.google_ads.v4.proto.enums.placeholder_type_pb2.PlaceholderTypeEnum.PlaceholderType.V = (
        ...
    )
    review_status: google.ads.google_ads.v4.proto.enums.policy_review_status_pb2.PolicyReviewStatusEnum.PolicyReviewStatus.V = (
        ...
    )
    approval_status: google.ads.google_ads.v4.proto.enums.policy_approval_status_pb2.PolicyApprovalStatusEnum.PolicyApprovalStatus.V = (
        ...
    )
    validation_status: google.ads.google_ads.v4.proto.enums.feed_item_validation_status_pb2.FeedItemValidationStatusEnum.FeedItemValidationStatus.V = (
        ...
    )
    quality_approval_status: google.ads.google_ads.v4.proto.enums.feed_item_quality_approval_status_pb2.FeedItemQualityApprovalStatusEnum.FeedItemQualityApprovalStatus.V = (
        ...
    )
    quality_disapproval_reasons: google.protobuf.internal.containers.RepeatedScalarFieldContainer[
        google.ads.google_ads.v4.proto.enums.feed_item_quality_disapproval_reason_pb2.FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason.V
    ] = ...
    @property
    def feed_mapping_resource_name(
        self,
    ) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def policy_topic_entries(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        google.ads.google_ads.v4.proto.common.policy_pb2.PolicyTopicEntry
    ]: ...
    @property
    def validation_errors(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___FeedItemValidationError
    ]: ...
    def __init__(
        self,
        *,
        placeholder_type_enum: google.ads.google_ads.v4.proto.enums.placeholder_type_pb2.PlaceholderTypeEnum.PlaceholderType.V = ...,
        feed_mapping_resource_name: typing.Optional[
            google.protobuf.wrappers_pb2.StringValue
        ] = ...,
        review_status: google.ads.google_ads.v4.proto.enums.policy_review_status_pb2.PolicyReviewStatusEnum.PolicyReviewStatus.V = ...,
        approval_status: google.ads.google_ads.v4.proto.enums.policy_approval_status_pb2.PolicyApprovalStatusEnum.PolicyApprovalStatus.V = ...,
        policy_topic_entries: typing.Optional[
            typing.Iterable[
                google.ads.google_ads.v4.proto.common.policy_pb2.PolicyTopicEntry
            ]
        ] = ...,
        validation_status: google.ads.google_ads.v4.proto.enums.feed_item_validation_status_pb2.FeedItemValidationStatusEnum.FeedItemValidationStatus.V = ...,
        validation_errors: typing.Optional[
            typing.Iterable[global___FeedItemValidationError]
        ] = ...,
        quality_approval_status: google.ads.google_ads.v4.proto.enums.feed_item_quality_approval_status_pb2.FeedItemQualityApprovalStatusEnum.FeedItemQualityApprovalStatus.V = ...,
        quality_disapproval_reasons: typing.Optional[
            typing.Iterable[
                google.ads.google_ads.v4.proto.enums.feed_item_quality_disapproval_reason_pb2.FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason.V
            ]
        ] = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "feed_mapping_resource_name", b"feed_mapping_resource_name"
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "approval_status",
            b"approval_status",
            "feed_mapping_resource_name",
            b"feed_mapping_resource_name",
            "placeholder_type_enum",
            b"placeholder_type_enum",
            "policy_topic_entries",
            b"policy_topic_entries",
            "quality_approval_status",
            b"quality_approval_status",
            "quality_disapproval_reasons",
            b"quality_disapproval_reasons",
            "review_status",
            b"review_status",
            "validation_errors",
            b"validation_errors",
            "validation_status",
            b"validation_status",
        ],
    ) -> None: ...

global___FeedItemPlaceholderPolicyInfo = FeedItemPlaceholderPolicyInfo

class FeedItemValidationError(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    VALIDATION_ERROR_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    FEED_ATTRIBUTE_IDS_FIELD_NUMBER: builtins.int
    EXTRA_INFO_FIELD_NUMBER: builtins.int
    validation_error: google.ads.google_ads.v4.proto.errors.feed_item_validation_error_pb2.FeedItemValidationErrorEnum.FeedItemValidationError.V = (
        ...
    )
    @property
    def description(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def feed_attribute_ids(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        google.protobuf.wrappers_pb2.Int64Value
    ]: ...
    @property
    def extra_info(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    def __init__(
        self,
        *,
        validation_error: google.ads.google_ads.v4.proto.errors.feed_item_validation_error_pb2.FeedItemValidationErrorEnum.FeedItemValidationError.V = ...,
        description: typing.Optional[google.protobuf.wrappers_pb2.StringValue] = ...,
        feed_attribute_ids: typing.Optional[
            typing.Iterable[google.protobuf.wrappers_pb2.Int64Value]
        ] = ...,
        extra_info: typing.Optional[google.protobuf.wrappers_pb2.StringValue] = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "description", b"description", "extra_info", b"extra_info"
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "description",
            b"description",
            "extra_info",
            b"extra_info",
            "feed_attribute_ids",
            b"feed_attribute_ids",
            "validation_error",
            b"validation_error",
        ],
    ) -> None: ...

global___FeedItemValidationError = FeedItemValidationError
