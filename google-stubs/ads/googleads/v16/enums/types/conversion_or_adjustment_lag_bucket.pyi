from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class ConversionOrAdjustmentLagBucketEnum(proto.Message):
    class ConversionOrAdjustmentLagBucket(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        CONVERSION_LESS_THAN_ONE_DAY = 2
        CONVERSION_ONE_TO_TWO_DAYS = 3
        CONVERSION_TWO_TO_THREE_DAYS = 4
        CONVERSION_THREE_TO_FOUR_DAYS = 5
        CONVERSION_FOUR_TO_FIVE_DAYS = 6
        CONVERSION_FIVE_TO_SIX_DAYS = 7
        CONVERSION_SIX_TO_SEVEN_DAYS = 8
        CONVERSION_SEVEN_TO_EIGHT_DAYS = 9
        CONVERSION_EIGHT_TO_NINE_DAYS = 10
        CONVERSION_NINE_TO_TEN_DAYS = 11
        CONVERSION_TEN_TO_ELEVEN_DAYS = 12
        CONVERSION_ELEVEN_TO_TWELVE_DAYS = 13
        CONVERSION_TWELVE_TO_THIRTEEN_DAYS = 14
        CONVERSION_THIRTEEN_TO_FOURTEEN_DAYS = 15
        CONVERSION_FOURTEEN_TO_TWENTY_ONE_DAYS = 16
        CONVERSION_TWENTY_ONE_TO_THIRTY_DAYS = 17
        CONVERSION_THIRTY_TO_FORTY_FIVE_DAYS = 18
        CONVERSION_FORTY_FIVE_TO_SIXTY_DAYS = 19
        CONVERSION_SIXTY_TO_NINETY_DAYS = 20
        ADJUSTMENT_LESS_THAN_ONE_DAY = 21
        ADJUSTMENT_ONE_TO_TWO_DAYS = 22
        ADJUSTMENT_TWO_TO_THREE_DAYS = 23
        ADJUSTMENT_THREE_TO_FOUR_DAYS = 24
        ADJUSTMENT_FOUR_TO_FIVE_DAYS = 25
        ADJUSTMENT_FIVE_TO_SIX_DAYS = 26
        ADJUSTMENT_SIX_TO_SEVEN_DAYS = 27
        ADJUSTMENT_SEVEN_TO_EIGHT_DAYS = 28
        ADJUSTMENT_EIGHT_TO_NINE_DAYS = 29
        ADJUSTMENT_NINE_TO_TEN_DAYS = 30
        ADJUSTMENT_TEN_TO_ELEVEN_DAYS = 31
        ADJUSTMENT_ELEVEN_TO_TWELVE_DAYS = 32
        ADJUSTMENT_TWELVE_TO_THIRTEEN_DAYS = 33
        ADJUSTMENT_THIRTEEN_TO_FOURTEEN_DAYS = 34
        ADJUSTMENT_FOURTEEN_TO_TWENTY_ONE_DAYS = 35
        ADJUSTMENT_TWENTY_ONE_TO_THIRTY_DAYS = 36
        ADJUSTMENT_THIRTY_TO_FORTY_FIVE_DAYS = 37
        ADJUSTMENT_FORTY_FIVE_TO_SIXTY_DAYS = 38
        ADJUSTMENT_SIXTY_TO_NINETY_DAYS = 39
        ADJUSTMENT_NINETY_TO_ONE_HUNDRED_AND_FORTY_FIVE_DAYS = 40
        CONVERSION_UNKNOWN = 41
        ADJUSTMENT_UNKNOWN = 42

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
