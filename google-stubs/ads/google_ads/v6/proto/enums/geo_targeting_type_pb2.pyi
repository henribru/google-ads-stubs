"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class GeoTargetingTypeEnum(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _GeoTargetingType(
        google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[GeoTargetingType.V],
        builtins.type,
    ):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED = GeoTargetingTypeEnum.GeoTargetingType.V(0)
        UNKNOWN = GeoTargetingTypeEnum.GeoTargetingType.V(1)
        AREA_OF_INTEREST = GeoTargetingTypeEnum.GeoTargetingType.V(2)
        LOCATION_OF_PRESENCE = GeoTargetingTypeEnum.GeoTargetingType.V(3)
    class GeoTargetingType(metaclass=_GeoTargetingType):
        V = typing.NewType("V", builtins.int)
    UNSPECIFIED = GeoTargetingTypeEnum.GeoTargetingType.V(0)
    UNKNOWN = GeoTargetingTypeEnum.GeoTargetingType.V(1)
    AREA_OF_INTEREST = GeoTargetingTypeEnum.GeoTargetingType.V(2)
    LOCATION_OF_PRESENCE = GeoTargetingTypeEnum.GeoTargetingType.V(3)
    def __init__(
        self,
    ) -> None: ...

global___GeoTargetingTypeEnum = GeoTargetingTypeEnum
