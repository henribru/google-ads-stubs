from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v25.enums.types.brand_lift_measurement_type import (
    BrandLiftMeasurementTypeEnum,
)
from google.ads.googleads.v25.enums.types.survey_intended_action import (
    SurveyIntendedActionEnum,
)
from google.ads.googleads.v25.enums.types.survey_subject_type import (
    SurveySubjectTypeEnum,
)

_M = TypeVar("_M")

class LiftMeasurementConfig(proto.Message):
    class SingleMeasurementQuestionSet(proto.Message):
        question_text_intended_action: SurveyIntendedActionEnum.SurveyIntendedAction
        question_text_subject_type: SurveySubjectTypeEnum.SurveySubjectType
        question_measurements: MutableSequence[
            BrandLiftMeasurementTypeEnum.BrandLiftMeasurementType
        ]
        advertiser_preferred_choice: str
        competitor_choices: MutableSequence[str]
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            question_text_intended_action: SurveyIntendedActionEnum.SurveyIntendedAction = ...,
            question_text_subject_type: SurveySubjectTypeEnum.SurveySubjectType = ...,
            question_measurements: MutableSequence[
                BrandLiftMeasurementTypeEnum.BrandLiftMeasurementType
            ] = ...,
            advertiser_preferred_choice: str = ...,
            competitor_choices: MutableSequence[str] = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self,
            key: Literal[
                "question_text_intended_action",
                "question_text_subject_type",
                "question_measurements",
                "advertiser_preferred_choice",
                "competitor_choices",
            ],
        ) -> bool: ...

    resource_name: str
    lift_measurement_config_id: int
    name: str
    conversion_actions: MutableSequence[str]
    campaigns: MutableSequence[str]
    survey_language: str
    single_measurement_question_set: LiftMeasurementConfig.SingleMeasurementQuestionSet
    conversion_lift_holdback_ratio_micros: int
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        lift_measurement_config_id: int = ...,
        name: str = ...,
        conversion_actions: MutableSequence[str] = ...,
        campaigns: MutableSequence[str] = ...,
        survey_language: str = ...,
        single_measurement_question_set: LiftMeasurementConfig.SingleMeasurementQuestionSet = ...,
        conversion_lift_holdback_ratio_micros: int = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "resource_name",
            "lift_measurement_config_id",
            "name",
            "conversion_actions",
            "campaigns",
            "survey_language",
            "single_measurement_question_set",
            "conversion_lift_holdback_ratio_micros",
        ],
    ) -> bool: ...
