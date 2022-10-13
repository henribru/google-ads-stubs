from typing import Any

import proto

class ConversionLagBucketEnum(proto.Message):
    class ConversionLagBucket(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        LESS_THAN_ONE_DAY = 2
        ONE_TO_TWO_DAYS = 3
        TWO_TO_THREE_DAYS = 4
        THREE_TO_FOUR_DAYS = 5
        FOUR_TO_FIVE_DAYS = 6
        FIVE_TO_SIX_DAYS = 7
        SIX_TO_SEVEN_DAYS = 8
        SEVEN_TO_EIGHT_DAYS = 9
        EIGHT_TO_NINE_DAYS = 10
        NINE_TO_TEN_DAYS = 11
        TEN_TO_ELEVEN_DAYS = 12
        ELEVEN_TO_TWELVE_DAYS = 13
        TWELVE_TO_THIRTEEN_DAYS = 14
        THIRTEEN_TO_FOURTEEN_DAYS = 15
        FOURTEEN_TO_TWENTY_ONE_DAYS = 16
        TWENTY_ONE_TO_THIRTY_DAYS = 17
        THIRTY_TO_FORTY_FIVE_DAYS = 18
        FORTY_FIVE_TO_SIXTY_DAYS = 19
        SIXTY_TO_NINETY_DAYS = 20
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
