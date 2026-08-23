from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class LiftMeasurementVideo(proto.Message):
    resource_name: str
    lift_measurement_config_id: int
    campaign: str
    video: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        lift_measurement_config_id: int = ...,
        campaign: str = ...,
        video: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "resource_name", "lift_measurement_config_id", "campaign", "video"
        ],
    ) -> bool: ...
