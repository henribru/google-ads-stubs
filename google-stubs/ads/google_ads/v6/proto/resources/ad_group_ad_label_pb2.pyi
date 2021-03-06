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

class AdGroupAdLabel(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    AD_GROUP_AD_FIELD_NUMBER: builtins.int
    LABEL_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    ad_group_ad: typing.Text = ...
    label: typing.Text = ...
    def __init__(
        self,
        *,
        resource_name: typing.Text = ...,
        ad_group_ad: typing.Text = ...,
        label: typing.Text = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "_ad_group_ad",
            b"_ad_group_ad",
            "_label",
            b"_label",
            "ad_group_ad",
            b"ad_group_ad",
            "label",
            b"label",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "_ad_group_ad",
            b"_ad_group_ad",
            "_label",
            b"_label",
            "ad_group_ad",
            b"ad_group_ad",
            "label",
            b"label",
            "resource_name",
            b"resource_name",
        ],
    ) -> None: ...
    @typing.overload
    def WhichOneof(
        self, oneof_group: typing_extensions.Literal["_ad_group_ad", b"_ad_group_ad"]
    ) -> typing_extensions.Literal["ad_group_ad"]: ...
    @typing.overload
    def WhichOneof(
        self, oneof_group: typing_extensions.Literal["_label", b"_label"]
    ) -> typing_extensions.Literal["label"]: ...

global___AdGroupAdLabel = AdGroupAdLabel
