from typing import Any

import proto

from google.ads.googleads.v11.enums.types.customer_match_upload_key_type import (
    CustomerMatchUploadKeyTypeEnum,
)
from google.ads.googleads.v11.enums.types.user_list_combined_rule_operator import (
    UserListCombinedRuleOperatorEnum,
)
from google.ads.googleads.v11.enums.types.user_list_crm_data_source_type import (
    UserListCrmDataSourceTypeEnum,
)
from google.ads.googleads.v11.enums.types.user_list_date_rule_item_operator import (
    UserListDateRuleItemOperatorEnum,
)
from google.ads.googleads.v11.enums.types.user_list_flexible_rule_operator import (
    UserListFlexibleRuleOperatorEnum,
)
from google.ads.googleads.v11.enums.types.user_list_logical_rule_operator import (
    UserListLogicalRuleOperatorEnum,
)
from google.ads.googleads.v11.enums.types.user_list_number_rule_item_operator import (
    UserListNumberRuleItemOperatorEnum,
)
from google.ads.googleads.v11.enums.types.user_list_prepopulation_status import (
    UserListPrepopulationStatusEnum,
)
from google.ads.googleads.v11.enums.types.user_list_rule_type import (
    UserListRuleTypeEnum,
)
from google.ads.googleads.v11.enums.types.user_list_string_rule_item_operator import (
    UserListStringRuleItemOperatorEnum,
)

class BasicUserListInfo(proto.Message):
    actions: list[UserListActionInfo]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        actions: list[UserListActionInfo] = ...
    ) -> None: ...

class CombinedRuleUserListInfo(proto.Message):
    left_operand: UserListRuleInfo
    right_operand: UserListRuleInfo
    rule_operator: UserListCombinedRuleOperatorEnum.UserListCombinedRuleOperator
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        left_operand: UserListRuleInfo = ...,
        right_operand: UserListRuleInfo = ...,
        rule_operator: UserListCombinedRuleOperatorEnum.UserListCombinedRuleOperator = ...
    ) -> None: ...

class CrmBasedUserListInfo(proto.Message):
    app_id: str
    upload_key_type: CustomerMatchUploadKeyTypeEnum.CustomerMatchUploadKeyType
    data_source_type: UserListCrmDataSourceTypeEnum.UserListCrmDataSourceType
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        app_id: str = ...,
        upload_key_type: CustomerMatchUploadKeyTypeEnum.CustomerMatchUploadKeyType = ...,
        data_source_type: UserListCrmDataSourceTypeEnum.UserListCrmDataSourceType = ...
    ) -> None: ...

class ExpressionRuleUserListInfo(proto.Message):
    rule: UserListRuleInfo
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        rule: UserListRuleInfo = ...
    ) -> None: ...

class FlexibleRuleOperandInfo(proto.Message):
    rule: UserListRuleInfo
    lookback_window_days: int
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        rule: UserListRuleInfo = ...,
        lookback_window_days: int = ...
    ) -> None: ...

class FlexibleRuleUserListInfo(proto.Message):
    inclusive_rule_operator: UserListFlexibleRuleOperatorEnum.UserListFlexibleRuleOperator
    inclusive_operands: list[FlexibleRuleOperandInfo]
    exclusive_operands: list[FlexibleRuleOperandInfo]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        inclusive_rule_operator: UserListFlexibleRuleOperatorEnum.UserListFlexibleRuleOperator = ...,
        inclusive_operands: list[FlexibleRuleOperandInfo] = ...,
        exclusive_operands: list[FlexibleRuleOperandInfo] = ...
    ) -> None: ...

class LogicalUserListInfo(proto.Message):
    rules: list[UserListLogicalRuleInfo]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        rules: list[UserListLogicalRuleInfo] = ...
    ) -> None: ...

class LogicalUserListOperandInfo(proto.Message):
    user_list: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        user_list: str = ...
    ) -> None: ...

class RuleBasedUserListInfo(proto.Message):
    prepopulation_status: UserListPrepopulationStatusEnum.UserListPrepopulationStatus
    flexible_rule_user_list: FlexibleRuleUserListInfo
    combined_rule_user_list: CombinedRuleUserListInfo
    expression_rule_user_list: ExpressionRuleUserListInfo
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        prepopulation_status: UserListPrepopulationStatusEnum.UserListPrepopulationStatus = ...,
        flexible_rule_user_list: FlexibleRuleUserListInfo = ...,
        combined_rule_user_list: CombinedRuleUserListInfo = ...,
        expression_rule_user_list: ExpressionRuleUserListInfo = ...
    ) -> None: ...

class SimilarUserListInfo(proto.Message):
    seed_user_list: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        seed_user_list: str = ...
    ) -> None: ...

class UserListActionInfo(proto.Message):
    conversion_action: str
    remarketing_action: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        conversion_action: str = ...,
        remarketing_action: str = ...
    ) -> None: ...

class UserListDateRuleItemInfo(proto.Message):
    operator: UserListDateRuleItemOperatorEnum.UserListDateRuleItemOperator
    value: str
    offset_in_days: int
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        operator: UserListDateRuleItemOperatorEnum.UserListDateRuleItemOperator = ...,
        value: str = ...,
        offset_in_days: int = ...
    ) -> None: ...

class UserListLogicalRuleInfo(proto.Message):
    operator: UserListLogicalRuleOperatorEnum.UserListLogicalRuleOperator
    rule_operands: list[LogicalUserListOperandInfo]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        operator: UserListLogicalRuleOperatorEnum.UserListLogicalRuleOperator = ...,
        rule_operands: list[LogicalUserListOperandInfo] = ...
    ) -> None: ...

class UserListNumberRuleItemInfo(proto.Message):
    operator: UserListNumberRuleItemOperatorEnum.UserListNumberRuleItemOperator
    value: float
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        operator: UserListNumberRuleItemOperatorEnum.UserListNumberRuleItemOperator = ...,
        value: float = ...
    ) -> None: ...

class UserListRuleInfo(proto.Message):
    rule_type: UserListRuleTypeEnum.UserListRuleType
    rule_item_groups: list[UserListRuleItemGroupInfo]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        rule_type: UserListRuleTypeEnum.UserListRuleType = ...,
        rule_item_groups: list[UserListRuleItemGroupInfo] = ...
    ) -> None: ...

class UserListRuleItemGroupInfo(proto.Message):
    rule_items: list[UserListRuleItemInfo]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        rule_items: list[UserListRuleItemInfo] = ...
    ) -> None: ...

class UserListRuleItemInfo(proto.Message):
    name: str
    number_rule_item: UserListNumberRuleItemInfo
    string_rule_item: UserListStringRuleItemInfo
    date_rule_item: UserListDateRuleItemInfo
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        name: str = ...,
        number_rule_item: UserListNumberRuleItemInfo = ...,
        string_rule_item: UserListStringRuleItemInfo = ...,
        date_rule_item: UserListDateRuleItemInfo = ...
    ) -> None: ...

class UserListStringRuleItemInfo(proto.Message):
    operator: UserListStringRuleItemOperatorEnum.UserListStringRuleItemOperator
    value: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        operator: UserListStringRuleItemOperatorEnum.UserListStringRuleItemOperator = ...,
        value: str = ...
    ) -> None: ...
