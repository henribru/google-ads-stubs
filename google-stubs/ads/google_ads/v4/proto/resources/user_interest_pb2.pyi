"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.ads.google_ads.v4.proto.common.criterion_category_availability_pb2
import google.ads.google_ads.v4.proto.enums.user_interest_taxonomy_type_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.wrappers_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class UserInterest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    TAXONOMY_TYPE_FIELD_NUMBER: builtins.int
    USER_INTEREST_ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    USER_INTEREST_PARENT_FIELD_NUMBER: builtins.int
    LAUNCHED_TO_ALL_FIELD_NUMBER: builtins.int
    AVAILABILITIES_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    taxonomy_type: google.ads.google_ads.v4.proto.enums.user_interest_taxonomy_type_pb2.UserInterestTaxonomyTypeEnum.UserInterestTaxonomyType.V = (
        ...
    )
    @property
    def user_interest_id(self) -> google.protobuf.wrappers_pb2.Int64Value: ...
    @property
    def name(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def user_interest_parent(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def launched_to_all(self) -> google.protobuf.wrappers_pb2.BoolValue: ...
    @property
    def availabilities(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        google.ads.google_ads.v4.proto.common.criterion_category_availability_pb2.CriterionCategoryAvailability
    ]: ...
    def __init__(
        self,
        *,
        resource_name: typing.Text = ...,
        taxonomy_type: google.ads.google_ads.v4.proto.enums.user_interest_taxonomy_type_pb2.UserInterestTaxonomyTypeEnum.UserInterestTaxonomyType.V = ...,
        user_interest_id: typing.Optional[
            google.protobuf.wrappers_pb2.Int64Value
        ] = ...,
        name: typing.Optional[google.protobuf.wrappers_pb2.StringValue] = ...,
        user_interest_parent: typing.Optional[
            google.protobuf.wrappers_pb2.StringValue
        ] = ...,
        launched_to_all: typing.Optional[google.protobuf.wrappers_pb2.BoolValue] = ...,
        availabilities: typing.Optional[
            typing.Iterable[
                google.ads.google_ads.v4.proto.common.criterion_category_availability_pb2.CriterionCategoryAvailability
            ]
        ] = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "launched_to_all",
            b"launched_to_all",
            "name",
            b"name",
            "user_interest_id",
            b"user_interest_id",
            "user_interest_parent",
            b"user_interest_parent",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "availabilities",
            b"availabilities",
            "launched_to_all",
            b"launched_to_all",
            "name",
            b"name",
            "resource_name",
            b"resource_name",
            "taxonomy_type",
            b"taxonomy_type",
            "user_interest_id",
            b"user_interest_id",
            "user_interest_parent",
            b"user_interest_parent",
        ],
    ) -> None: ...

global___UserInterest = UserInterest
