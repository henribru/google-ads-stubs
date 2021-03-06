"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class ClickLocation(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CITY_FIELD_NUMBER: builtins.int
    COUNTRY_FIELD_NUMBER: builtins.int
    METRO_FIELD_NUMBER: builtins.int
    MOST_SPECIFIC_FIELD_NUMBER: builtins.int
    REGION_FIELD_NUMBER: builtins.int
    city: typing.Text = ...
    country: typing.Text = ...
    metro: typing.Text = ...
    most_specific: typing.Text = ...
    region: typing.Text = ...
    def __init__(
        self,
        *,
        city: typing.Text = ...,
        country: typing.Text = ...,
        metro: typing.Text = ...,
        most_specific: typing.Text = ...,
        region: typing.Text = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "_city",
            b"_city",
            "_country",
            b"_country",
            "_metro",
            b"_metro",
            "_most_specific",
            b"_most_specific",
            "_region",
            b"_region",
            "city",
            b"city",
            "country",
            b"country",
            "metro",
            b"metro",
            "most_specific",
            b"most_specific",
            "region",
            b"region",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "_city",
            b"_city",
            "_country",
            b"_country",
            "_metro",
            b"_metro",
            "_most_specific",
            b"_most_specific",
            "_region",
            b"_region",
            "city",
            b"city",
            "country",
            b"country",
            "metro",
            b"metro",
            "most_specific",
            b"most_specific",
            "region",
            b"region",
        ],
    ) -> None: ...
    @typing.overload
    def WhichOneof(
        self, oneof_group: typing_extensions.Literal["_city", b"_city"]
    ) -> typing_extensions.Literal["city"]: ...
    @typing.overload
    def WhichOneof(
        self, oneof_group: typing_extensions.Literal["_country", b"_country"]
    ) -> typing_extensions.Literal["country"]: ...
    @typing.overload
    def WhichOneof(
        self, oneof_group: typing_extensions.Literal["_metro", b"_metro"]
    ) -> typing_extensions.Literal["metro"]: ...
    @typing.overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions.Literal["_most_specific", b"_most_specific"],
    ) -> typing_extensions.Literal["most_specific"]: ...
    @typing.overload
    def WhichOneof(
        self, oneof_group: typing_extensions.Literal["_region", b"_region"]
    ) -> typing_extensions.Literal["region"]: ...

global___ClickLocation = ClickLocation
