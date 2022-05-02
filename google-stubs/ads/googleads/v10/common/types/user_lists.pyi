import proto
from _typeshed import Incomplete

from google.ads.googleads.v10.enums.types import (
    customer_match_upload_key_type as customer_match_upload_key_type,
    user_list_combined_rule_operator as user_list_combined_rule_operator,
    user_list_crm_data_source_type as user_list_crm_data_source_type,
    user_list_date_rule_item_operator as user_list_date_rule_item_operator,
    user_list_logical_rule_operator as user_list_logical_rule_operator,
    user_list_number_rule_item_operator as user_list_number_rule_item_operator,
    user_list_prepopulation_status as user_list_prepopulation_status,
    user_list_rule_type as user_list_rule_type,
    user_list_string_rule_item_operator as user_list_string_rule_item_operator,
)

__protobuf__: Incomplete

class SimilarUserListInfo(proto.Message):
    seed_user_list: Incomplete

class CrmBasedUserListInfo(proto.Message):
    app_id: Incomplete
    upload_key_type: Incomplete
    data_source_type: Incomplete

class UserListRuleInfo(proto.Message):
    rule_type: Incomplete
    rule_item_groups: Incomplete

class UserListRuleItemGroupInfo(proto.Message):
    rule_items: Incomplete

class UserListRuleItemInfo(proto.Message):
    name: Incomplete
    number_rule_item: Incomplete
    string_rule_item: Incomplete
    date_rule_item: Incomplete

class UserListDateRuleItemInfo(proto.Message):
    operator: Incomplete
    value: Incomplete
    offset_in_days: Incomplete

class UserListNumberRuleItemInfo(proto.Message):
    operator: Incomplete
    value: Incomplete

class UserListStringRuleItemInfo(proto.Message):
    operator: Incomplete
    value: Incomplete

class CombinedRuleUserListInfo(proto.Message):
    left_operand: Incomplete
    right_operand: Incomplete
    rule_operator: Incomplete

class DateSpecificRuleUserListInfo(proto.Message):
    rule: Incomplete
    start_date: Incomplete
    end_date: Incomplete

class ExpressionRuleUserListInfo(proto.Message):
    rule: Incomplete

class RuleBasedUserListInfo(proto.Message):
    prepopulation_status: Incomplete
    combined_rule_user_list: Incomplete
    date_specific_rule_user_list: Incomplete
    expression_rule_user_list: Incomplete

class LogicalUserListInfo(proto.Message):
    rules: Incomplete

class UserListLogicalRuleInfo(proto.Message):
    operator: Incomplete
    rule_operands: Incomplete

class LogicalUserListOperandInfo(proto.Message):
    user_list: Incomplete

class BasicUserListInfo(proto.Message):
    actions: Incomplete

class UserListActionInfo(proto.Message):
    conversion_action: Incomplete
    remarketing_action: Incomplete
