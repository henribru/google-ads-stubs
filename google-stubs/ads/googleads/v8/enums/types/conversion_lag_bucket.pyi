from typing import Any

import proto

__protobuf__: Any

class ConversionLagBucketEnum(proto.Message):
    class ConversionLagBucket(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        LESS_THAN_ONE_DAY: int
        ONE_TO_TWO_DAYS: int
        TWO_TO_THREE_DAYS: int
        THREE_TO_FOUR_DAYS: int
        FOUR_TO_FIVE_DAYS: int
        FIVE_TO_SIX_DAYS: int
        SIX_TO_SEVEN_DAYS: int
        SEVEN_TO_EIGHT_DAYS: int
        EIGHT_TO_NINE_DAYS: int
        NINE_TO_TEN_DAYS: int
        TEN_TO_ELEVEN_DAYS: int
        ELEVEN_TO_TWELVE_DAYS: int
        TWELVE_TO_THIRTEEN_DAYS: int
        THIRTEEN_TO_FOURTEEN_DAYS: int
        FOURTEEN_TO_TWENTY_ONE_DAYS: int
        TWENTY_ONE_TO_THIRTY_DAYS: int
        THIRTY_TO_FORTY_FIVE_DAYS: int
        FORTY_FIVE_TO_SIXTY_DAYS: int
        SIXTY_TO_NINETY_DAYS: int
