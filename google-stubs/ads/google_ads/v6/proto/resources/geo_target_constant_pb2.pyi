"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.ads.google_ads.v6.proto.enums.geo_target_constant_status_pb2
import google.protobuf.descriptor
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class GeoTargetConstant(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    COUNTRY_CODE_FIELD_NUMBER: builtins.int
    TARGET_TYPE_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    CANONICAL_NAME_FIELD_NUMBER: builtins.int
    PARENT_GEO_TARGET_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    id: builtins.int = ...
    name: typing.Text = ...
    country_code: typing.Text = ...
    target_type: typing.Text = ...
    status: google.ads.google_ads.v6.proto.enums.geo_target_constant_status_pb2.GeoTargetConstantStatusEnum.GeoTargetConstantStatus.V = (
        ...
    )
    canonical_name: typing.Text = ...
    parent_geo_target: typing.Text = ...
    def __init__(
        self,
        *,
        resource_name: typing.Text = ...,
        id: builtins.int = ...,
        name: typing.Text = ...,
        country_code: typing.Text = ...,
        target_type: typing.Text = ...,
        status: google.ads.google_ads.v6.proto.enums.geo_target_constant_status_pb2.GeoTargetConstantStatusEnum.GeoTargetConstantStatus.V = ...,
        canonical_name: typing.Text = ...,
        parent_geo_target: typing.Text = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "_canonical_name",
            b"_canonical_name",
            "_country_code",
            b"_country_code",
            "_id",
            b"_id",
            "_name",
            b"_name",
            "_parent_geo_target",
            b"_parent_geo_target",
            "_target_type",
            b"_target_type",
            "canonical_name",
            b"canonical_name",
            "country_code",
            b"country_code",
            "id",
            b"id",
            "name",
            b"name",
            "parent_geo_target",
            b"parent_geo_target",
            "target_type",
            b"target_type",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "_canonical_name",
            b"_canonical_name",
            "_country_code",
            b"_country_code",
            "_id",
            b"_id",
            "_name",
            b"_name",
            "_parent_geo_target",
            b"_parent_geo_target",
            "_target_type",
            b"_target_type",
            "canonical_name",
            b"canonical_name",
            "country_code",
            b"country_code",
            "id",
            b"id",
            "name",
            b"name",
            "parent_geo_target",
            b"parent_geo_target",
            "resource_name",
            b"resource_name",
            "status",
            b"status",
            "target_type",
            b"target_type",
        ],
    ) -> None: ...
    @typing.overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions.Literal["_canonical_name", b"_canonical_name"],
    ) -> typing_extensions.Literal["canonical_name"]: ...
    @typing.overload
    def WhichOneof(
        self, oneof_group: typing_extensions.Literal["_country_code", b"_country_code"]
    ) -> typing_extensions.Literal["country_code"]: ...
    @typing.overload
    def WhichOneof(
        self, oneof_group: typing_extensions.Literal["_id", b"_id"]
    ) -> typing_extensions.Literal["id"]: ...
    @typing.overload
    def WhichOneof(
        self, oneof_group: typing_extensions.Literal["_name", b"_name"]
    ) -> typing_extensions.Literal["name"]: ...
    @typing.overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions.Literal[
            "_parent_geo_target", b"_parent_geo_target"
        ],
    ) -> typing_extensions.Literal["parent_geo_target"]: ...
    @typing.overload
    def WhichOneof(
        self, oneof_group: typing_extensions.Literal["_target_type", b"_target_type"]
    ) -> typing_extensions.Literal["target_type"]: ...

global___GeoTargetConstant = GeoTargetConstant
