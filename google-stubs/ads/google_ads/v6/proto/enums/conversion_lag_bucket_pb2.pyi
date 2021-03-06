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

class ConversionLagBucketEnum(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _ConversionLagBucket(
        google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
            ConversionLagBucket.V
        ],
        builtins.type,
    ):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED = ConversionLagBucketEnum.ConversionLagBucket.V(0)
        UNKNOWN = ConversionLagBucketEnum.ConversionLagBucket.V(1)
        LESS_THAN_ONE_DAY = ConversionLagBucketEnum.ConversionLagBucket.V(2)
        ONE_TO_TWO_DAYS = ConversionLagBucketEnum.ConversionLagBucket.V(3)
        TWO_TO_THREE_DAYS = ConversionLagBucketEnum.ConversionLagBucket.V(4)
        THREE_TO_FOUR_DAYS = ConversionLagBucketEnum.ConversionLagBucket.V(5)
        FOUR_TO_FIVE_DAYS = ConversionLagBucketEnum.ConversionLagBucket.V(6)
        FIVE_TO_SIX_DAYS = ConversionLagBucketEnum.ConversionLagBucket.V(7)
        SIX_TO_SEVEN_DAYS = ConversionLagBucketEnum.ConversionLagBucket.V(8)
        SEVEN_TO_EIGHT_DAYS = ConversionLagBucketEnum.ConversionLagBucket.V(9)
        EIGHT_TO_NINE_DAYS = ConversionLagBucketEnum.ConversionLagBucket.V(10)
        NINE_TO_TEN_DAYS = ConversionLagBucketEnum.ConversionLagBucket.V(11)
        TEN_TO_ELEVEN_DAYS = ConversionLagBucketEnum.ConversionLagBucket.V(12)
        ELEVEN_TO_TWELVE_DAYS = ConversionLagBucketEnum.ConversionLagBucket.V(13)
        TWELVE_TO_THIRTEEN_DAYS = ConversionLagBucketEnum.ConversionLagBucket.V(14)
        THIRTEEN_TO_FOURTEEN_DAYS = ConversionLagBucketEnum.ConversionLagBucket.V(15)
        FOURTEEN_TO_TWENTY_ONE_DAYS = ConversionLagBucketEnum.ConversionLagBucket.V(16)
        TWENTY_ONE_TO_THIRTY_DAYS = ConversionLagBucketEnum.ConversionLagBucket.V(17)
        THIRTY_TO_FORTY_FIVE_DAYS = ConversionLagBucketEnum.ConversionLagBucket.V(18)
        FORTY_FIVE_TO_SIXTY_DAYS = ConversionLagBucketEnum.ConversionLagBucket.V(19)
        SIXTY_TO_NINETY_DAYS = ConversionLagBucketEnum.ConversionLagBucket.V(20)
    class ConversionLagBucket(metaclass=_ConversionLagBucket):
        V = typing.NewType("V", builtins.int)
    UNSPECIFIED = ConversionLagBucketEnum.ConversionLagBucket.V(0)
    UNKNOWN = ConversionLagBucketEnum.ConversionLagBucket.V(1)
    LESS_THAN_ONE_DAY = ConversionLagBucketEnum.ConversionLagBucket.V(2)
    ONE_TO_TWO_DAYS = ConversionLagBucketEnum.ConversionLagBucket.V(3)
    TWO_TO_THREE_DAYS = ConversionLagBucketEnum.ConversionLagBucket.V(4)
    THREE_TO_FOUR_DAYS = ConversionLagBucketEnum.ConversionLagBucket.V(5)
    FOUR_TO_FIVE_DAYS = ConversionLagBucketEnum.ConversionLagBucket.V(6)
    FIVE_TO_SIX_DAYS = ConversionLagBucketEnum.ConversionLagBucket.V(7)
    SIX_TO_SEVEN_DAYS = ConversionLagBucketEnum.ConversionLagBucket.V(8)
    SEVEN_TO_EIGHT_DAYS = ConversionLagBucketEnum.ConversionLagBucket.V(9)
    EIGHT_TO_NINE_DAYS = ConversionLagBucketEnum.ConversionLagBucket.V(10)
    NINE_TO_TEN_DAYS = ConversionLagBucketEnum.ConversionLagBucket.V(11)
    TEN_TO_ELEVEN_DAYS = ConversionLagBucketEnum.ConversionLagBucket.V(12)
    ELEVEN_TO_TWELVE_DAYS = ConversionLagBucketEnum.ConversionLagBucket.V(13)
    TWELVE_TO_THIRTEEN_DAYS = ConversionLagBucketEnum.ConversionLagBucket.V(14)
    THIRTEEN_TO_FOURTEEN_DAYS = ConversionLagBucketEnum.ConversionLagBucket.V(15)
    FOURTEEN_TO_TWENTY_ONE_DAYS = ConversionLagBucketEnum.ConversionLagBucket.V(16)
    TWENTY_ONE_TO_THIRTY_DAYS = ConversionLagBucketEnum.ConversionLagBucket.V(17)
    THIRTY_TO_FORTY_FIVE_DAYS = ConversionLagBucketEnum.ConversionLagBucket.V(18)
    FORTY_FIVE_TO_SIXTY_DAYS = ConversionLagBucketEnum.ConversionLagBucket.V(19)
    SIXTY_TO_NINETY_DAYS = ConversionLagBucketEnum.ConversionLagBucket.V(20)
    def __init__(
        self,
    ) -> None: ...

global___ConversionLagBucketEnum = ConversionLagBucketEnum
