"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.ads.google_ads.v5.proto.enums.keyword_plan_network_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.wrappers_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class KeywordPlanCampaign(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    KEYWORD_PLAN_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    LANGUAGE_CONSTANTS_FIELD_NUMBER: builtins.int
    KEYWORD_PLAN_NETWORK_FIELD_NUMBER: builtins.int
    CPC_BID_MICROS_FIELD_NUMBER: builtins.int
    GEO_TARGETS_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    keyword_plan_network: google.ads.google_ads.v5.proto.enums.keyword_plan_network_pb2.KeywordPlanNetworkEnum.KeywordPlanNetwork.V = (
        ...
    )
    @property
    def keyword_plan(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def id(self) -> google.protobuf.wrappers_pb2.Int64Value: ...
    @property
    def name(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def language_constants(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        google.protobuf.wrappers_pb2.StringValue
    ]: ...
    @property
    def cpc_bid_micros(self) -> google.protobuf.wrappers_pb2.Int64Value: ...
    @property
    def geo_targets(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___KeywordPlanGeoTarget
    ]: ...
    def __init__(
        self,
        *,
        resource_name: typing.Text = ...,
        keyword_plan: typing.Optional[google.protobuf.wrappers_pb2.StringValue] = ...,
        id: typing.Optional[google.protobuf.wrappers_pb2.Int64Value] = ...,
        name: typing.Optional[google.protobuf.wrappers_pb2.StringValue] = ...,
        language_constants: typing.Optional[
            typing.Iterable[google.protobuf.wrappers_pb2.StringValue]
        ] = ...,
        keyword_plan_network: google.ads.google_ads.v5.proto.enums.keyword_plan_network_pb2.KeywordPlanNetworkEnum.KeywordPlanNetwork.V = ...,
        cpc_bid_micros: typing.Optional[google.protobuf.wrappers_pb2.Int64Value] = ...,
        geo_targets: typing.Optional[
            typing.Iterable[global___KeywordPlanGeoTarget]
        ] = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "cpc_bid_micros",
            b"cpc_bid_micros",
            "id",
            b"id",
            "keyword_plan",
            b"keyword_plan",
            "name",
            b"name",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "cpc_bid_micros",
            b"cpc_bid_micros",
            "geo_targets",
            b"geo_targets",
            "id",
            b"id",
            "keyword_plan",
            b"keyword_plan",
            "keyword_plan_network",
            b"keyword_plan_network",
            "language_constants",
            b"language_constants",
            "name",
            b"name",
            "resource_name",
            b"resource_name",
        ],
    ) -> None: ...

global___KeywordPlanCampaign = KeywordPlanCampaign

class KeywordPlanGeoTarget(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    GEO_TARGET_CONSTANT_FIELD_NUMBER: builtins.int
    @property
    def geo_target_constant(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    def __init__(
        self,
        *,
        geo_target_constant: typing.Optional[
            google.protobuf.wrappers_pb2.StringValue
        ] = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "geo_target_constant", b"geo_target_constant"
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "geo_target_constant", b"geo_target_constant"
        ],
    ) -> None: ...

global___KeywordPlanGeoTarget = KeywordPlanGeoTarget
