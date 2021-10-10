from typing import Any

import proto

from google.ads.googleads.v8.enums.types import (
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

__protobuf__: Any

class SimilarUserListInfo(proto.Message):
    seed_user_list: Any

class CrmBasedUserListInfo(proto.Message):
    app_id: Any
    upload_key_type: Any
    data_source_type: Any

class UserListRuleInfo(proto.Message):
    rule_type: Any
    rule_item_groups: Any

class UserListRuleItemGroupInfo(proto.Message):
    rule_items: Any

class UserListRuleItemInfo(proto.Message):
    name: Any
    number_rule_item: Any
    string_rule_item: Any
    date_rule_item: Any

class UserListDateRuleItemInfo(proto.Message):
    operator: Any
    value: Any
    offset_in_days: Any

class UserListNumberRuleItemInfo(proto.Message):
    operator: Any
    value: Any

class UserListStringRuleItemInfo(proto.Message):
    operator: Any
    value: Any

class CombinedRuleUserListInfo(proto.Message):
    left_operand: Any
    right_operand: Any
    rule_operator: Any

class DateSpecificRuleUserListInfo(proto.Message):
    rule: Any
    start_date: Any
    end_date: Any

class ExpressionRuleUserListInfo(proto.Message):
    rule: Any

class RuleBasedUserListInfo(proto.Message):
    prepopulation_status: Any
    combined_rule_user_list: Any
    date_specific_rule_user_list: Any
    expression_rule_user_list: Any

class LogicalUserListInfo(proto.Message):
    rules: Any

class UserListLogicalRuleInfo(proto.Message):
    operator: Any
    rule_operands: Any

class LogicalUserListOperandInfo(proto.Message):
    user_list: Any

class BasicUserListInfo(proto.Message):
    actions: Any

class UserListActionInfo(proto.Message):
    conversion_action: Any
    remarketing_action: Any
