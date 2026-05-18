from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v24.enums.types.asset_field_type import AssetFieldTypeEnum
from google.ads.googleads.v24.enums.types.bidding_strategy_type import (
    BiddingStrategyTypeEnum,
)
from google.ads.googleads.v24.enums.types.experiment_asset_detail_operation import (
    ExperimentAssetDetailOperationEnum,
)

_M = TypeVar("_M")

class ExperimentArm(proto.Message):
    class AssetDetail(proto.Message):
        asset: str
        field_type: AssetFieldTypeEnum.AssetFieldType
        asset_detail_operation: (
            ExperimentAssetDetailOperationEnum.ExperimentAssetDetailOperation
        )
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            asset: str = ...,
            field_type: AssetFieldTypeEnum.AssetFieldType = ...,
            asset_detail_operation: ExperimentAssetDetailOperationEnum.ExperimentAssetDetailOperation = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self, key: Literal["asset", "field_type", "asset_detail_operation"]
        ) -> bool: ...

    class AssetGroupAssetInfo(proto.Message):
        asset: str
        field_type: AssetFieldTypeEnum.AssetFieldType
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            asset: str = ...,
            field_type: AssetFieldTypeEnum.AssetFieldType = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self, key: Literal["asset", "field_type"]
        ) -> bool: ...

    class AssetGroupInfo(proto.Message):
        asset_group: str
        asset_group_assets: MutableSequence[ExperimentArm.AssetGroupAssetInfo]
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            asset_group: str = ...,
            asset_group_assets: MutableSequence[
                ExperimentArm.AssetGroupAssetInfo
            ] = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self, key: Literal["asset_group", "asset_group_assets"]
        ) -> bool: ...

    class AssetTestingInfo(proto.Message):
        asset_variation_infos: MutableSequence[ExperimentArm.AssetVariationInfo]
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            asset_variation_infos: MutableSequence[
                ExperimentArm.AssetVariationInfo
            ] = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self, key: Literal["asset_variation_infos"]
        ) -> bool: ...

    class AssetVariationInfo(proto.Message):
        base_ad_group: str
        base_ad: str
        asset_details: MutableSequence[ExperimentArm.AssetDetail]
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            base_ad_group: str = ...,
            base_ad: str = ...,
            asset_details: MutableSequence[ExperimentArm.AssetDetail] = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self, key: Literal["base_ad_group", "base_ad", "asset_details"]
        ) -> bool: ...

    class ExperimentalPerformanceMaxCampaignSettings(proto.Message):
        budget_amount_micros: int
        target_roas: float
        target_cpa_micros: int
        bidding_strategy_type: BiddingStrategyTypeEnum.BiddingStrategyType
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            budget_amount_micros: int = ...,
            target_roas: float = ...,
            target_cpa_micros: int = ...,
            bidding_strategy_type: BiddingStrategyTypeEnum.BiddingStrategyType = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self,
            key: Literal[
                "budget_amount_micros",
                "target_roas",
                "target_cpa_micros",
                "bidding_strategy_type",
            ],
        ) -> bool: ...

    class PerformanceMaxExperimentArmInfo(proto.Message):
        experimental_performance_max_campaign_settings: (
            ExperimentArm.ExperimentalPerformanceMaxCampaignSettings
        )
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            experimental_performance_max_campaign_settings: ExperimentArm.ExperimentalPerformanceMaxCampaignSettings = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self, key: Literal["experimental_performance_max_campaign_settings"]
        ) -> bool: ...

    resource_name: str
    experiment: str
    name: str
    control: bool
    traffic_split: int
    campaigns: MutableSequence[str]
    in_design_campaigns: MutableSequence[str]
    asset_testing_info: ExperimentArm.AssetTestingInfo
    asset_groups: MutableSequence[ExperimentArm.AssetGroupInfo]
    performance_max_experiment_arm_info: ExperimentArm.PerformanceMaxExperimentArmInfo
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        experiment: str = ...,
        name: str = ...,
        control: bool = ...,
        traffic_split: int = ...,
        campaigns: MutableSequence[str] = ...,
        in_design_campaigns: MutableSequence[str] = ...,
        asset_testing_info: ExperimentArm.AssetTestingInfo = ...,
        asset_groups: MutableSequence[ExperimentArm.AssetGroupInfo] = ...,
        performance_max_experiment_arm_info: ExperimentArm.PerformanceMaxExperimentArmInfo = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "resource_name",
            "experiment",
            "name",
            "control",
            "traffic_split",
            "campaigns",
            "in_design_campaigns",
            "asset_testing_info",
            "asset_groups",
            "performance_max_experiment_arm_info",
        ],
    ) -> bool: ...
