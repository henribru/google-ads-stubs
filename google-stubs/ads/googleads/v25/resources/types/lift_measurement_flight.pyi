from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v25.enums.types.lift_measurement_flight_status import (
    LiftMeasurementFlightStatusEnum,
)
from google.ads.googleads.v25.enums.types.lift_metric_type import LiftMetricTypeEnum
from google.ads.googleads.v25.enums.types.survey_lift_flight_target_response_mode import (
    SurveyLiftFlightTargetResponseModeEnum,
)

_M = TypeVar("_M")

class LiftMeasurementFlight(proto.Message):
    resource_name: str
    lift_measurement_config_id: int
    lift_measurement_flight_id: int
    survey_lift_info: LiftMeasurementFlightSurveyLiftInfo
    name: str
    status: LiftMeasurementFlightStatusEnum.LiftMeasurementFlightStatus
    lift_type: LiftMetricTypeEnum.LiftMetricType
    survey_lift_measurement: LiftMeasurementFlightSurveyLiftMeasurement
    start_date: str
    end_date: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        lift_measurement_config_id: int = ...,
        lift_measurement_flight_id: int = ...,
        survey_lift_info: LiftMeasurementFlightSurveyLiftInfo = ...,
        name: str = ...,
        status: LiftMeasurementFlightStatusEnum.LiftMeasurementFlightStatus = ...,
        lift_type: LiftMetricTypeEnum.LiftMetricType = ...,
        survey_lift_measurement: LiftMeasurementFlightSurveyLiftMeasurement = ...,
        start_date: str = ...,
        end_date: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "resource_name",
            "lift_measurement_config_id",
            "lift_measurement_flight_id",
            "survey_lift_info",
            "name",
            "status",
            "lift_type",
            "survey_lift_measurement",
            "start_date",
            "end_date",
        ],
    ) -> bool: ...

class LiftMeasurementFlightSurveyLiftInfo(proto.Message):
    target_response_mode: (
        SurveyLiftFlightTargetResponseModeEnum.SurveyLiftFlightTargetResponseMode
    )
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        target_response_mode: SurveyLiftFlightTargetResponseModeEnum.SurveyLiftFlightTargetResponseMode = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["target_response_mode"]
    ) -> bool: ...

class LiftMeasurementFlightSurveyLiftMeasurement(proto.Message):
    response_collection_ratio_micros: int
    min_survey_response_date: str
    max_survey_response_date: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        response_collection_ratio_micros: int = ...,
        min_survey_response_date: str = ...,
        max_survey_response_date: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "response_collection_ratio_micros",
            "min_survey_response_date",
            "max_survey_response_date",
        ],
    ) -> bool: ...
