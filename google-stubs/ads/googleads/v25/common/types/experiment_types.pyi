from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v25.enums.types.optimize_assets_experiment_subtype import (
    OptimizeAssetsExperimentSubtypeEnum,
)
from google.ads.googleads.v25.enums.types.video_experiment_subtype import (
    VideoExperimentSubtypeEnum,
)

_M = TypeVar("_M")

class OptimizeAssetsExperimentInfo(proto.Message):
    optimize_assets_experiment_subtype: (
        OptimizeAssetsExperimentSubtypeEnum.OptimizeAssetsExperimentSubtype
    )
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        optimize_assets_experiment_subtype: OptimizeAssetsExperimentSubtypeEnum.OptimizeAssetsExperimentSubtype = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["optimize_assets_experiment_subtype"]
    ) -> bool: ...

class VideoExperimentInfo(proto.Message):
    video_experiment_subtype: VideoExperimentSubtypeEnum.VideoExperimentSubtype
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        video_experiment_subtype: VideoExperimentSubtypeEnum.VideoExperimentSubtype = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["video_experiment_subtype"]
    ) -> bool: ...
