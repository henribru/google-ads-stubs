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

from google.ads.google_ads.v5.proto.common.custom_parameter_pb2 import (
    CustomParameter as google___ads___googleads___v5___common___custom_parameter_pb2___CustomParameter,
)
from google.ads.google_ads.v5.proto.common.explorer_auto_optimizer_setting_pb2 import (
    ExplorerAutoOptimizerSetting as google___ads___googleads___v5___common___explorer_auto_optimizer_setting_pb2___ExplorerAutoOptimizerSetting,
)
from google.ads.google_ads.v5.proto.common.targeting_setting_pb2 import (
    TargetingSetting as google___ads___googleads___v5___common___targeting_setting_pb2___TargetingSetting,
)
from google.ads.google_ads.v5.proto.enums.ad_group_ad_rotation_mode_pb2 import (
    AdGroupAdRotationModeEnum as google___ads___googleads___v5___enums___ad_group_ad_rotation_mode_pb2___AdGroupAdRotationModeEnum,
)
from google.ads.google_ads.v5.proto.enums.ad_group_status_pb2 import (
    AdGroupStatusEnum as google___ads___googleads___v5___enums___ad_group_status_pb2___AdGroupStatusEnum,
)
from google.ads.google_ads.v5.proto.enums.ad_group_type_pb2 import (
    AdGroupTypeEnum as google___ads___googleads___v5___enums___ad_group_type_pb2___AdGroupTypeEnum,
)
from google.ads.google_ads.v5.proto.enums.bidding_source_pb2 import (
    BiddingSourceEnum as google___ads___googleads___v5___enums___bidding_source_pb2___BiddingSourceEnum,
)
from google.ads.google_ads.v5.proto.enums.targeting_dimension_pb2 import (
    TargetingDimensionEnum as google___ads___googleads___v5___enums___targeting_dimension_pb2___TargetingDimensionEnum,
)

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class AdGroup(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name: typing___Text = ...
    id: builtin___int = ...
    name: typing___Text = ...
    status: google___ads___googleads___v5___enums___ad_group_status_pb2___AdGroupStatusEnum.AdGroupStatusValue = ...
    type: google___ads___googleads___v5___enums___ad_group_type_pb2___AdGroupTypeEnum.AdGroupTypeValue = ...
    ad_rotation_mode: google___ads___googleads___v5___enums___ad_group_ad_rotation_mode_pb2___AdGroupAdRotationModeEnum.AdGroupAdRotationModeValue = ...
    base_ad_group: typing___Text = ...
    tracking_url_template: typing___Text = ...
    campaign: typing___Text = ...
    cpc_bid_micros: builtin___int = ...
    cpm_bid_micros: builtin___int = ...
    target_cpa_micros: builtin___int = ...
    cpv_bid_micros: builtin___int = ...
    target_cpm_micros: builtin___int = ...
    target_roas: builtin___float = ...
    percent_cpc_bid_micros: builtin___int = ...
    display_custom_bid_dimension: google___ads___googleads___v5___enums___targeting_dimension_pb2___TargetingDimensionEnum.TargetingDimensionValue = ...
    final_url_suffix: typing___Text = ...
    effective_target_cpa_micros: builtin___int = ...
    effective_target_cpa_source: google___ads___googleads___v5___enums___bidding_source_pb2___BiddingSourceEnum.BiddingSourceValue = ...
    effective_target_roas: builtin___float = ...
    effective_target_roas_source: google___ads___googleads___v5___enums___bidding_source_pb2___BiddingSourceEnum.BiddingSourceValue = ...
    labels: google___protobuf___internal___containers___RepeatedScalarFieldContainer[
        typing___Text
    ] = ...
    @property
    def url_custom_parameters(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        google___ads___googleads___v5___common___custom_parameter_pb2___CustomParameter
    ]: ...
    @property
    def explorer_auto_optimizer_setting(
        self,
    ) -> google___ads___googleads___v5___common___explorer_auto_optimizer_setting_pb2___ExplorerAutoOptimizerSetting: ...
    @property
    def targeting_setting(
        self,
    ) -> google___ads___googleads___v5___common___targeting_setting_pb2___TargetingSetting: ...
    def __init__(
        self,
        *,
        resource_name: typing___Optional[typing___Text] = None,
        id: typing___Optional[builtin___int] = None,
        name: typing___Optional[typing___Text] = None,
        status: typing___Optional[
            google___ads___googleads___v5___enums___ad_group_status_pb2___AdGroupStatusEnum.AdGroupStatusValue
        ] = None,
        type: typing___Optional[
            google___ads___googleads___v5___enums___ad_group_type_pb2___AdGroupTypeEnum.AdGroupTypeValue
        ] = None,
        ad_rotation_mode: typing___Optional[
            google___ads___googleads___v5___enums___ad_group_ad_rotation_mode_pb2___AdGroupAdRotationModeEnum.AdGroupAdRotationModeValue
        ] = None,
        base_ad_group: typing___Optional[typing___Text] = None,
        tracking_url_template: typing___Optional[typing___Text] = None,
        url_custom_parameters: typing___Optional[
            typing___Iterable[
                google___ads___googleads___v5___common___custom_parameter_pb2___CustomParameter
            ]
        ] = None,
        campaign: typing___Optional[typing___Text] = None,
        cpc_bid_micros: typing___Optional[builtin___int] = None,
        cpm_bid_micros: typing___Optional[builtin___int] = None,
        target_cpa_micros: typing___Optional[builtin___int] = None,
        cpv_bid_micros: typing___Optional[builtin___int] = None,
        target_cpm_micros: typing___Optional[builtin___int] = None,
        target_roas: typing___Optional[builtin___float] = None,
        percent_cpc_bid_micros: typing___Optional[builtin___int] = None,
        explorer_auto_optimizer_setting: typing___Optional[
            google___ads___googleads___v5___common___explorer_auto_optimizer_setting_pb2___ExplorerAutoOptimizerSetting
        ] = None,
        display_custom_bid_dimension: typing___Optional[
            google___ads___googleads___v5___enums___targeting_dimension_pb2___TargetingDimensionEnum.TargetingDimensionValue
        ] = None,
        final_url_suffix: typing___Optional[typing___Text] = None,
        targeting_setting: typing___Optional[
            google___ads___googleads___v5___common___targeting_setting_pb2___TargetingSetting
        ] = None,
        effective_target_cpa_micros: typing___Optional[builtin___int] = None,
        effective_target_cpa_source: typing___Optional[
            google___ads___googleads___v5___enums___bidding_source_pb2___BiddingSourceEnum.BiddingSourceValue
        ] = None,
        effective_target_roas: typing___Optional[builtin___float] = None,
        effective_target_roas_source: typing___Optional[
            google___ads___googleads___v5___enums___bidding_source_pb2___BiddingSourceEnum.BiddingSourceValue
        ] = None,
        labels: typing___Optional[typing___Iterable[typing___Text]] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "_base_ad_group",
            b"_base_ad_group",
            "_campaign",
            b"_campaign",
            "_cpc_bid_micros",
            b"_cpc_bid_micros",
            "_cpm_bid_micros",
            b"_cpm_bid_micros",
            "_cpv_bid_micros",
            b"_cpv_bid_micros",
            "_effective_target_cpa_micros",
            b"_effective_target_cpa_micros",
            "_effective_target_roas",
            b"_effective_target_roas",
            "_final_url_suffix",
            b"_final_url_suffix",
            "_id",
            b"_id",
            "_name",
            b"_name",
            "_percent_cpc_bid_micros",
            b"_percent_cpc_bid_micros",
            "_target_cpa_micros",
            b"_target_cpa_micros",
            "_target_cpm_micros",
            b"_target_cpm_micros",
            "_target_roas",
            b"_target_roas",
            "_tracking_url_template",
            b"_tracking_url_template",
            "base_ad_group",
            b"base_ad_group",
            "campaign",
            b"campaign",
            "cpc_bid_micros",
            b"cpc_bid_micros",
            "cpm_bid_micros",
            b"cpm_bid_micros",
            "cpv_bid_micros",
            b"cpv_bid_micros",
            "effective_target_cpa_micros",
            b"effective_target_cpa_micros",
            "effective_target_roas",
            b"effective_target_roas",
            "explorer_auto_optimizer_setting",
            b"explorer_auto_optimizer_setting",
            "final_url_suffix",
            b"final_url_suffix",
            "id",
            b"id",
            "name",
            b"name",
            "percent_cpc_bid_micros",
            b"percent_cpc_bid_micros",
            "target_cpa_micros",
            b"target_cpa_micros",
            "target_cpm_micros",
            b"target_cpm_micros",
            "target_roas",
            b"target_roas",
            "targeting_setting",
            b"targeting_setting",
            "tracking_url_template",
            b"tracking_url_template",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "_base_ad_group",
            b"_base_ad_group",
            "_campaign",
            b"_campaign",
            "_cpc_bid_micros",
            b"_cpc_bid_micros",
            "_cpm_bid_micros",
            b"_cpm_bid_micros",
            "_cpv_bid_micros",
            b"_cpv_bid_micros",
            "_effective_target_cpa_micros",
            b"_effective_target_cpa_micros",
            "_effective_target_roas",
            b"_effective_target_roas",
            "_final_url_suffix",
            b"_final_url_suffix",
            "_id",
            b"_id",
            "_name",
            b"_name",
            "_percent_cpc_bid_micros",
            b"_percent_cpc_bid_micros",
            "_target_cpa_micros",
            b"_target_cpa_micros",
            "_target_cpm_micros",
            b"_target_cpm_micros",
            "_target_roas",
            b"_target_roas",
            "_tracking_url_template",
            b"_tracking_url_template",
            "ad_rotation_mode",
            b"ad_rotation_mode",
            "base_ad_group",
            b"base_ad_group",
            "campaign",
            b"campaign",
            "cpc_bid_micros",
            b"cpc_bid_micros",
            "cpm_bid_micros",
            b"cpm_bid_micros",
            "cpv_bid_micros",
            b"cpv_bid_micros",
            "display_custom_bid_dimension",
            b"display_custom_bid_dimension",
            "effective_target_cpa_micros",
            b"effective_target_cpa_micros",
            "effective_target_cpa_source",
            b"effective_target_cpa_source",
            "effective_target_roas",
            b"effective_target_roas",
            "effective_target_roas_source",
            b"effective_target_roas_source",
            "explorer_auto_optimizer_setting",
            b"explorer_auto_optimizer_setting",
            "final_url_suffix",
            b"final_url_suffix",
            "id",
            b"id",
            "labels",
            b"labels",
            "name",
            b"name",
            "percent_cpc_bid_micros",
            b"percent_cpc_bid_micros",
            "resource_name",
            b"resource_name",
            "status",
            b"status",
            "target_cpa_micros",
            b"target_cpa_micros",
            "target_cpm_micros",
            b"target_cpm_micros",
            "target_roas",
            b"target_roas",
            "targeting_setting",
            b"targeting_setting",
            "tracking_url_template",
            b"tracking_url_template",
            "type",
            b"type",
            "url_custom_parameters",
            b"url_custom_parameters",
        ],
    ) -> None: ...
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal["_base_ad_group", b"_base_ad_group"],
    ) -> typing_extensions___Literal["base_ad_group"]: ...
    @typing___overload
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["_campaign", b"_campaign"]
    ) -> typing_extensions___Literal["campaign"]: ...
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal["_cpc_bid_micros", b"_cpc_bid_micros"],
    ) -> typing_extensions___Literal["cpc_bid_micros"]: ...
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal["_cpm_bid_micros", b"_cpm_bid_micros"],
    ) -> typing_extensions___Literal["cpm_bid_micros"]: ...
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal["_cpv_bid_micros", b"_cpv_bid_micros"],
    ) -> typing_extensions___Literal["cpv_bid_micros"]: ...
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "_effective_target_cpa_micros", b"_effective_target_cpa_micros"
        ],
    ) -> typing_extensions___Literal["effective_target_cpa_micros"]: ...
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "_effective_target_roas", b"_effective_target_roas"
        ],
    ) -> typing_extensions___Literal["effective_target_roas"]: ...
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "_final_url_suffix", b"_final_url_suffix"
        ],
    ) -> typing_extensions___Literal["final_url_suffix"]: ...
    @typing___overload
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["_id", b"_id"]
    ) -> typing_extensions___Literal["id"]: ...
    @typing___overload
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["_name", b"_name"]
    ) -> typing_extensions___Literal["name"]: ...
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "_percent_cpc_bid_micros", b"_percent_cpc_bid_micros"
        ],
    ) -> typing_extensions___Literal["percent_cpc_bid_micros"]: ...
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "_target_cpa_micros", b"_target_cpa_micros"
        ],
    ) -> typing_extensions___Literal["target_cpa_micros"]: ...
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "_target_cpm_micros", b"_target_cpm_micros"
        ],
    ) -> typing_extensions___Literal["target_cpm_micros"]: ...
    @typing___overload
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["_target_roas", b"_target_roas"]
    ) -> typing_extensions___Literal["target_roas"]: ...
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "_tracking_url_template", b"_tracking_url_template"
        ],
    ) -> typing_extensions___Literal["tracking_url_template"]: ...

type___AdGroup = AdGroup
