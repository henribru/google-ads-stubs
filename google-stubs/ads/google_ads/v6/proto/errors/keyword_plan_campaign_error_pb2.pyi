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

class KeywordPlanCampaignErrorEnum(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _KeywordPlanCampaignError(
        google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
            KeywordPlanCampaignError.V
        ],
        builtins.type,
    ):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED = KeywordPlanCampaignErrorEnum.KeywordPlanCampaignError.V(0)
        UNKNOWN = KeywordPlanCampaignErrorEnum.KeywordPlanCampaignError.V(1)
        INVALID_NAME = KeywordPlanCampaignErrorEnum.KeywordPlanCampaignError.V(2)
        INVALID_LANGUAGES = KeywordPlanCampaignErrorEnum.KeywordPlanCampaignError.V(3)
        INVALID_GEOS = KeywordPlanCampaignErrorEnum.KeywordPlanCampaignError.V(4)
        DUPLICATE_NAME = KeywordPlanCampaignErrorEnum.KeywordPlanCampaignError.V(5)
        MAX_GEOS_EXCEEDED = KeywordPlanCampaignErrorEnum.KeywordPlanCampaignError.V(6)
        MAX_LANGUAGES_EXCEEDED = (
            KeywordPlanCampaignErrorEnum.KeywordPlanCampaignError.V(7)
        )
    class KeywordPlanCampaignError(metaclass=_KeywordPlanCampaignError):
        V = typing.NewType("V", builtins.int)
    UNSPECIFIED = KeywordPlanCampaignErrorEnum.KeywordPlanCampaignError.V(0)
    UNKNOWN = KeywordPlanCampaignErrorEnum.KeywordPlanCampaignError.V(1)
    INVALID_NAME = KeywordPlanCampaignErrorEnum.KeywordPlanCampaignError.V(2)
    INVALID_LANGUAGES = KeywordPlanCampaignErrorEnum.KeywordPlanCampaignError.V(3)
    INVALID_GEOS = KeywordPlanCampaignErrorEnum.KeywordPlanCampaignError.V(4)
    DUPLICATE_NAME = KeywordPlanCampaignErrorEnum.KeywordPlanCampaignError.V(5)
    MAX_GEOS_EXCEEDED = KeywordPlanCampaignErrorEnum.KeywordPlanCampaignError.V(6)
    MAX_LANGUAGES_EXCEEDED = KeywordPlanCampaignErrorEnum.KeywordPlanCampaignError.V(7)
    def __init__(
        self,
    ) -> None: ...

global___KeywordPlanCampaignErrorEnum = KeywordPlanCampaignErrorEnum
