from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v16.enums.types.customer_match_upload_key_type import (
    CustomerMatchUploadKeyTypeEnum,
)
from google.ads.googleads.v16.enums.types.lookalike_expansion_level import (
    LookalikeExpansionLevelEnum,
)
from google.ads.googleads.v16.enums.types.user_list_crm_data_source_type import (
    UserListCrmDataSourceTypeEnum,
)
from google.ads.googleads.v16.enums.types.user_list_date_rule_item_operator import (
    UserListDateRuleItemOperatorEnum,
)
from google.ads.googleads.v16.enums.types.user_list_flexible_rule_operator import (
    UserListFlexibleRuleOperatorEnum,
)
from google.ads.googleads.v16.enums.types.user_list_logical_rule_operator import (
    UserListLogicalRuleOperatorEnum,
)
from google.ads.googleads.v16.enums.types.user_list_number_rule_item_operator import (
    UserListNumberRuleItemOperatorEnum,
)
from google.ads.googleads.v16.enums.types.user_list_prepopulation_status import (
    UserListPrepopulationStatusEnum,
)
from google.ads.googleads.v16.enums.types.user_list_rule_type import (
    UserListRuleTypeEnum,
)
from google.ads.googleads.v16.enums.types.user_list_string_rule_item_operator import (
    UserListStringRuleItemOperatorEnum,
)

_M = TypeVar("_M")

class BasicUserListInfo(proto.Message):
    actions: MutableSequence[UserListActionInfo]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        actions: MutableSequence[UserListActionInfo] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["actions"]
    ) -> bool: ...

class CrmBasedUserListInfo(proto.Message):
    app_id: str
    upload_key_type: CustomerMatchUploadKeyTypeEnum.CustomerMatchUploadKeyType
    data_source_type: UserListCrmDataSourceTypeEnum.UserListCrmDataSourceType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        app_id: str = ...,
        upload_key_type: CustomerMatchUploadKeyTypeEnum.CustomerMatchUploadKeyType = ...,
        data_source_type: UserListCrmDataSourceTypeEnum.UserListCrmDataSourceType = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["app_id", "upload_key_type", "data_source_type"]
    ) -> bool: ...

class FlexibleRuleOperandInfo(proto.Message):
    rule: UserListRuleInfo
    lookback_window_days: int
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        rule: UserListRuleInfo = ...,
        lookback_window_days: int = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["rule", "lookback_window_days"]
    ) -> bool: ...

class FlexibleRuleUserListInfo(proto.Message):
    inclusive_rule_operator: (
        UserListFlexibleRuleOperatorEnum.UserListFlexibleRuleOperator
    )
    inclusive_operands: MutableSequence[FlexibleRuleOperandInfo]
    exclusive_operands: MutableSequence[FlexibleRuleOperandInfo]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        inclusive_rule_operator: UserListFlexibleRuleOperatorEnum.UserListFlexibleRuleOperator = ...,
        inclusive_operands: MutableSequence[FlexibleRuleOperandInfo] = ...,
        exclusive_operands: MutableSequence[FlexibleRuleOperandInfo] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "inclusive_rule_operator", "inclusive_operands", "exclusive_operands"
        ],
    ) -> bool: ...

class LogicalUserListInfo(proto.Message):
    rules: MutableSequence[UserListLogicalRuleInfo]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        rules: MutableSequence[UserListLogicalRuleInfo] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["rules"]
    ) -> bool: ...

class LogicalUserListOperandInfo(proto.Message):
    user_list: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        user_list: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["user_list"]
    ) -> bool: ...

class LookalikeUserListInfo(proto.Message):
    seed_user_list_ids: MutableSequence[int]
    expansion_level: LookalikeExpansionLevelEnum.LookalikeExpansionLevel
    country_codes: MutableSequence[str]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        seed_user_list_ids: MutableSequence[int] = ...,
        expansion_level: LookalikeExpansionLevelEnum.LookalikeExpansionLevel = ...,
        country_codes: MutableSequence[str] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["seed_user_list_ids", "expansion_level", "country_codes"]
    ) -> bool: ...

class RuleBasedUserListInfo(proto.Message):
    prepopulation_status: UserListPrepopulationStatusEnum.UserListPrepopulationStatus
    flexible_rule_user_list: FlexibleRuleUserListInfo
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        prepopulation_status: UserListPrepopulationStatusEnum.UserListPrepopulationStatus = ...,
        flexible_rule_user_list: FlexibleRuleUserListInfo = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["prepopulation_status", "flexible_rule_user_list"]
    ) -> bool: ...

class SimilarUserListInfo(proto.Message):
    seed_user_list: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        seed_user_list: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["seed_user_list"]
    ) -> bool: ...

class UserListActionInfo(proto.Message):
    conversion_action: str
    remarketing_action: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        conversion_action: str = ...,
        remarketing_action: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["conversion_action", "remarketing_action"]
    ) -> bool: ...

class UserListDateRuleItemInfo(proto.Message):
    operator: UserListDateRuleItemOperatorEnum.UserListDateRuleItemOperator
    value: str
    offset_in_days: int
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        operator: UserListDateRuleItemOperatorEnum.UserListDateRuleItemOperator = ...,
        value: str = ...,
        offset_in_days: int = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["operator", "value", "offset_in_days"]
    ) -> bool: ...

class UserListLogicalRuleInfo(proto.Message):
    operator: UserListLogicalRuleOperatorEnum.UserListLogicalRuleOperator
    rule_operands: MutableSequence[LogicalUserListOperandInfo]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        operator: UserListLogicalRuleOperatorEnum.UserListLogicalRuleOperator = ...,
        rule_operands: MutableSequence[LogicalUserListOperandInfo] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["operator", "rule_operands"]
    ) -> bool: ...

class UserListNumberRuleItemInfo(proto.Message):
    operator: UserListNumberRuleItemOperatorEnum.UserListNumberRuleItemOperator
    value: float
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        operator: UserListNumberRuleItemOperatorEnum.UserListNumberRuleItemOperator = ...,
        value: float = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["operator", "value"]
    ) -> bool: ...

class UserListRuleInfo(proto.Message):
    rule_type: UserListRuleTypeEnum.UserListRuleType
    rule_item_groups: MutableSequence[UserListRuleItemGroupInfo]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        rule_type: UserListRuleTypeEnum.UserListRuleType = ...,
        rule_item_groups: MutableSequence[UserListRuleItemGroupInfo] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["rule_type", "rule_item_groups"]
    ) -> bool: ...

class UserListRuleItemGroupInfo(proto.Message):
    rule_items: MutableSequence[UserListRuleItemInfo]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        rule_items: MutableSequence[UserListRuleItemInfo] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["rule_items"]
    ) -> bool: ...

class UserListRuleItemInfo(proto.Message):
    name: str
    number_rule_item: UserListNumberRuleItemInfo
    string_rule_item: UserListStringRuleItemInfo
    date_rule_item: UserListDateRuleItemInfo
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        name: str = ...,
        number_rule_item: UserListNumberRuleItemInfo = ...,
        string_rule_item: UserListStringRuleItemInfo = ...,
        date_rule_item: UserListDateRuleItemInfo = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal["name", "number_rule_item", "string_rule_item", "date_rule_item"],
    ) -> bool: ...

class UserListStringRuleItemInfo(proto.Message):
    operator: UserListStringRuleItemOperatorEnum.UserListStringRuleItemOperator
    value: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        operator: UserListStringRuleItemOperatorEnum.UserListStringRuleItemOperator = ...,
        value: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["operator", "value"]
    ) -> bool: ...
