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

class AppCampaignBiddingStrategyGoalTypeEnum(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _AppCampaignBiddingStrategyGoalType(
        google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
            AppCampaignBiddingStrategyGoalType.V
        ],
        builtins.type,
    ):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED = (
            AppCampaignBiddingStrategyGoalTypeEnum.AppCampaignBiddingStrategyGoalType.V(
                0
            )
        )
        UNKNOWN = (
            AppCampaignBiddingStrategyGoalTypeEnum.AppCampaignBiddingStrategyGoalType.V(
                1
            )
        )
        OPTIMIZE_INSTALLS_TARGET_INSTALL_COST = (
            AppCampaignBiddingStrategyGoalTypeEnum.AppCampaignBiddingStrategyGoalType.V(
                2
            )
        )
        OPTIMIZE_IN_APP_CONVERSIONS_TARGET_INSTALL_COST = (
            AppCampaignBiddingStrategyGoalTypeEnum.AppCampaignBiddingStrategyGoalType.V(
                3
            )
        )
        OPTIMIZE_IN_APP_CONVERSIONS_TARGET_CONVERSION_COST = (
            AppCampaignBiddingStrategyGoalTypeEnum.AppCampaignBiddingStrategyGoalType.V(
                4
            )
        )
        OPTIMIZE_RETURN_ON_ADVERTISING_SPEND = (
            AppCampaignBiddingStrategyGoalTypeEnum.AppCampaignBiddingStrategyGoalType.V(
                5
            )
        )
    class AppCampaignBiddingStrategyGoalType(
        metaclass=_AppCampaignBiddingStrategyGoalType
    ):
        V = typing.NewType("V", builtins.int)
    UNSPECIFIED = (
        AppCampaignBiddingStrategyGoalTypeEnum.AppCampaignBiddingStrategyGoalType.V(0)
    )
    UNKNOWN = (
        AppCampaignBiddingStrategyGoalTypeEnum.AppCampaignBiddingStrategyGoalType.V(1)
    )
    OPTIMIZE_INSTALLS_TARGET_INSTALL_COST = (
        AppCampaignBiddingStrategyGoalTypeEnum.AppCampaignBiddingStrategyGoalType.V(2)
    )
    OPTIMIZE_IN_APP_CONVERSIONS_TARGET_INSTALL_COST = (
        AppCampaignBiddingStrategyGoalTypeEnum.AppCampaignBiddingStrategyGoalType.V(3)
    )
    OPTIMIZE_IN_APP_CONVERSIONS_TARGET_CONVERSION_COST = (
        AppCampaignBiddingStrategyGoalTypeEnum.AppCampaignBiddingStrategyGoalType.V(4)
    )
    OPTIMIZE_RETURN_ON_ADVERTISING_SPEND = (
        AppCampaignBiddingStrategyGoalTypeEnum.AppCampaignBiddingStrategyGoalType.V(5)
    )
    def __init__(
        self,
    ) -> None: ...

global___AppCampaignBiddingStrategyGoalTypeEnum = AppCampaignBiddingStrategyGoalTypeEnum
