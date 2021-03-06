"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.ads.google_ads.v4.proto.common.text_label_pb2
import google.ads.google_ads.v4.proto.enums.label_status_pb2
import google.protobuf.descriptor
import google.protobuf.message
import google.protobuf.wrappers_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class Label(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    TEXT_LABEL_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    status: google.ads.google_ads.v4.proto.enums.label_status_pb2.LabelStatusEnum.LabelStatus.V = (
        ...
    )
    @property
    def id(self) -> google.protobuf.wrappers_pb2.Int64Value: ...
    @property
    def name(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def text_label(
        self,
    ) -> google.ads.google_ads.v4.proto.common.text_label_pb2.TextLabel: ...
    def __init__(
        self,
        *,
        resource_name: typing.Text = ...,
        id: typing.Optional[google.protobuf.wrappers_pb2.Int64Value] = ...,
        name: typing.Optional[google.protobuf.wrappers_pb2.StringValue] = ...,
        status: google.ads.google_ads.v4.proto.enums.label_status_pb2.LabelStatusEnum.LabelStatus.V = ...,
        text_label: typing.Optional[
            google.ads.google_ads.v4.proto.common.text_label_pb2.TextLabel
        ] = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "id", b"id", "name", b"name", "text_label", b"text_label"
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "id",
            b"id",
            "name",
            b"name",
            "resource_name",
            b"resource_name",
            "status",
            b"status",
            "text_label",
            b"text_label",
        ],
    ) -> None: ...

global___Label = Label
