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
)
from google.protobuf.message import Message as google___protobuf___message___Message
from typing_extensions import Literal as typing_extensions___Literal

from google.ads.google_ads.v6.proto.common.criterion_category_availability_pb2 import (
    CriterionCategoryAvailability as google___ads___googleads___v6___common___criterion_category_availability_pb2___CriterionCategoryAvailability,
)
from google.ads.google_ads.v6.proto.enums.user_interest_taxonomy_type_pb2 import (
    UserInterestTaxonomyTypeEnum as google___ads___googleads___v6___enums___user_interest_taxonomy_type_pb2___UserInterestTaxonomyTypeEnum,
)

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class UserInterest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name: typing___Text = ...
    taxonomy_type: google___ads___googleads___v6___enums___user_interest_taxonomy_type_pb2___UserInterestTaxonomyTypeEnum.UserInterestTaxonomyTypeValue = ...
    user_interest_id: builtin___int = ...
    name: typing___Text = ...
    user_interest_parent: typing___Text = ...
    launched_to_all: builtin___bool = ...
    @property
    def availabilities(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        google___ads___googleads___v6___common___criterion_category_availability_pb2___CriterionCategoryAvailability
    ]: ...
    def __init__(
        self,
        *,
        resource_name: typing___Optional[typing___Text] = None,
        taxonomy_type: typing___Optional[
            google___ads___googleads___v6___enums___user_interest_taxonomy_type_pb2___UserInterestTaxonomyTypeEnum.UserInterestTaxonomyTypeValue
        ] = None,
        user_interest_id: typing___Optional[builtin___int] = None,
        name: typing___Optional[typing___Text] = None,
        user_interest_parent: typing___Optional[typing___Text] = None,
        launched_to_all: typing___Optional[builtin___bool] = None,
        availabilities: typing___Optional[
            typing___Iterable[
                google___ads___googleads___v6___common___criterion_category_availability_pb2___CriterionCategoryAvailability
            ]
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "_launched_to_all",
            b"_launched_to_all",
            "_name",
            b"_name",
            "_user_interest_id",
            b"_user_interest_id",
            "_user_interest_parent",
            b"_user_interest_parent",
            "launched_to_all",
            b"launched_to_all",
            "name",
            b"name",
            "user_interest_id",
            b"user_interest_id",
            "user_interest_parent",
            b"user_interest_parent",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "_launched_to_all",
            b"_launched_to_all",
            "_name",
            b"_name",
            "_user_interest_id",
            b"_user_interest_id",
            "_user_interest_parent",
            b"_user_interest_parent",
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
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "_launched_to_all", b"_launched_to_all"
        ],
    ) -> typing_extensions___Literal["launched_to_all"]: ...
    @typing___overload
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["_name", b"_name"]
    ) -> typing_extensions___Literal["name"]: ...
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "_user_interest_id", b"_user_interest_id"
        ],
    ) -> typing_extensions___Literal["user_interest_id"]: ...
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "_user_interest_parent", b"_user_interest_parent"
        ],
    ) -> typing_extensions___Literal["user_interest_parent"]: ...

type___UserInterest = UserInterest
