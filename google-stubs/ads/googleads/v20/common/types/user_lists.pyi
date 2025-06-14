import proto
from _typeshed import Incomplete
from google.ads.googleads.v20.enums.types import customer_match_upload_key_type, lookalike_expansion_level, user_list_crm_data_source_type, user_list_date_rule_item_operator, user_list_flexible_rule_operator, user_list_logical_rule_operator, user_list_number_rule_item_operator, user_list_prepopulation_status, user_list_rule_type, user_list_string_rule_item_operator
from typing import MutableSequence

__protobuf__: Incomplete

class LookalikeUserListInfo(proto.Message):
    seed_user_list_ids: MutableSequence[int]
    expansion_level: lookalike_expansion_level.LookalikeExpansionLevelEnum.LookalikeExpansionLevel
    country_codes: MutableSequence[str]

class SimilarUserListInfo(proto.Message):
    seed_user_list: str

class CrmBasedUserListInfo(proto.Message):
    app_id: str
    upload_key_type: customer_match_upload_key_type.CustomerMatchUploadKeyTypeEnum.CustomerMatchUploadKeyType
    data_source_type: user_list_crm_data_source_type.UserListCrmDataSourceTypeEnum.UserListCrmDataSourceType

class UserListRuleInfo(proto.Message):
    rule_type: user_list_rule_type.UserListRuleTypeEnum.UserListRuleType
    rule_item_groups: MutableSequence['UserListRuleItemGroupInfo']

class UserListRuleItemGroupInfo(proto.Message):
    rule_items: MutableSequence['UserListRuleItemInfo']

class UserListRuleItemInfo(proto.Message):
    name: str
    number_rule_item: UserListNumberRuleItemInfo
    string_rule_item: UserListStringRuleItemInfo
    date_rule_item: UserListDateRuleItemInfo

class UserListDateRuleItemInfo(proto.Message):
    operator: user_list_date_rule_item_operator.UserListDateRuleItemOperatorEnum.UserListDateRuleItemOperator
    value: str
    offset_in_days: int

class UserListNumberRuleItemInfo(proto.Message):
    operator: user_list_number_rule_item_operator.UserListNumberRuleItemOperatorEnum.UserListNumberRuleItemOperator
    value: float

class UserListStringRuleItemInfo(proto.Message):
    operator: user_list_string_rule_item_operator.UserListStringRuleItemOperatorEnum.UserListStringRuleItemOperator
    value: str

class FlexibleRuleOperandInfo(proto.Message):
    rule: UserListRuleInfo
    lookback_window_days: int

class FlexibleRuleUserListInfo(proto.Message):
    inclusive_rule_operator: user_list_flexible_rule_operator.UserListFlexibleRuleOperatorEnum.UserListFlexibleRuleOperator
    inclusive_operands: MutableSequence['FlexibleRuleOperandInfo']
    exclusive_operands: MutableSequence['FlexibleRuleOperandInfo']

class RuleBasedUserListInfo(proto.Message):
    prepopulation_status: user_list_prepopulation_status.UserListPrepopulationStatusEnum.UserListPrepopulationStatus
    flexible_rule_user_list: FlexibleRuleUserListInfo

class LogicalUserListInfo(proto.Message):
    rules: MutableSequence['UserListLogicalRuleInfo']

class UserListLogicalRuleInfo(proto.Message):
    operator: user_list_logical_rule_operator.UserListLogicalRuleOperatorEnum.UserListLogicalRuleOperator
    rule_operands: MutableSequence['LogicalUserListOperandInfo']

class LogicalUserListOperandInfo(proto.Message):
    user_list: str

class BasicUserListInfo(proto.Message):
    actions: MutableSequence['UserListActionInfo']

class UserListActionInfo(proto.Message):
    conversion_action: str
    remarketing_action: str
