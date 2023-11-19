from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class CriterionErrorEnum(proto.Message):
    class CriterionError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        CONCRETE_TYPE_REQUIRED = 2
        INVALID_EXCLUDED_CATEGORY = 3
        INVALID_KEYWORD_TEXT = 4
        KEYWORD_TEXT_TOO_LONG = 5
        KEYWORD_HAS_TOO_MANY_WORDS = 6
        KEYWORD_HAS_INVALID_CHARS = 7
        INVALID_PLACEMENT_URL = 8
        INVALID_USER_LIST = 9
        INVALID_USER_INTEREST = 10
        INVALID_FORMAT_FOR_PLACEMENT_URL = 11
        PLACEMENT_URL_IS_TOO_LONG = 12
        PLACEMENT_URL_HAS_ILLEGAL_CHAR = 13
        PLACEMENT_URL_HAS_MULTIPLE_SITES_IN_LINE = 14
        PLACEMENT_IS_NOT_AVAILABLE_FOR_TARGETING_OR_EXCLUSION = 15
        INVALID_TOPIC_PATH = 16
        INVALID_YOUTUBE_CHANNEL_ID = 17
        INVALID_YOUTUBE_VIDEO_ID = 18
        YOUTUBE_VERTICAL_CHANNEL_DEPRECATED = 19
        YOUTUBE_DEMOGRAPHIC_CHANNEL_DEPRECATED = 20
        YOUTUBE_URL_UNSUPPORTED = 21
        CANNOT_EXCLUDE_CRITERIA_TYPE = 22
        CANNOT_ADD_CRITERIA_TYPE = 23
        CANNOT_EXCLUDE_SIMILAR_USER_LIST = 26
        CANNOT_ADD_CLOSED_USER_LIST = 27
        CANNOT_ADD_DISPLAY_ONLY_LISTS_TO_SEARCH_ONLY_CAMPAIGNS = 28
        CANNOT_ADD_DISPLAY_ONLY_LISTS_TO_SEARCH_CAMPAIGNS = 29
        CANNOT_ADD_DISPLAY_ONLY_LISTS_TO_SHOPPING_CAMPAIGNS = 30
        CANNOT_ADD_USER_INTERESTS_TO_SEARCH_CAMPAIGNS = 31
        CANNOT_SET_BIDS_ON_CRITERION_TYPE_IN_SEARCH_CAMPAIGNS = 32
        CANNOT_ADD_URLS_TO_CRITERION_TYPE_FOR_CAMPAIGN_TYPE = 33
        INVALID_COMBINED_AUDIENCE = 122
        INVALID_CUSTOM_AFFINITY = 96
        INVALID_CUSTOM_INTENT = 97
        INVALID_CUSTOM_AUDIENCE = 121
        INVALID_IP_ADDRESS = 34
        INVALID_IP_FORMAT = 35
        INVALID_MOBILE_APP = 36
        INVALID_MOBILE_APP_CATEGORY = 37
        INVALID_CRITERION_ID = 38
        CANNOT_TARGET_CRITERION = 39
        CANNOT_TARGET_OBSOLETE_CRITERION = 40
        CRITERION_ID_AND_TYPE_MISMATCH = 41
        INVALID_PROXIMITY_RADIUS = 42
        INVALID_PROXIMITY_RADIUS_UNITS = 43
        INVALID_STREETADDRESS_LENGTH = 44
        INVALID_CITYNAME_LENGTH = 45
        INVALID_REGIONCODE_LENGTH = 46
        INVALID_REGIONNAME_LENGTH = 47
        INVALID_POSTALCODE_LENGTH = 48
        INVALID_COUNTRY_CODE = 49
        INVALID_LATITUDE = 50
        INVALID_LONGITUDE = 51
        PROXIMITY_GEOPOINT_AND_ADDRESS_BOTH_CANNOT_BE_NULL = 52
        INVALID_PROXIMITY_ADDRESS = 53
        INVALID_USER_DOMAIN_NAME = 54
        CRITERION_PARAMETER_TOO_LONG = 55
        AD_SCHEDULE_TIME_INTERVALS_OVERLAP = 56
        AD_SCHEDULE_INTERVAL_CANNOT_SPAN_MULTIPLE_DAYS = 57
        AD_SCHEDULE_INVALID_TIME_INTERVAL = 58
        AD_SCHEDULE_EXCEEDED_INTERVALS_PER_DAY_LIMIT = 59
        AD_SCHEDULE_CRITERION_ID_MISMATCHING_FIELDS = 60
        CANNOT_BID_MODIFY_CRITERION_TYPE = 61
        CANNOT_BID_MODIFY_CRITERION_CAMPAIGN_OPTED_OUT = 62
        CANNOT_BID_MODIFY_NEGATIVE_CRITERION = 63
        BID_MODIFIER_ALREADY_EXISTS = 64
        FEED_ID_NOT_ALLOWED = 65
        ACCOUNT_INELIGIBLE_FOR_CRITERIA_TYPE = 66
        CRITERIA_TYPE_INVALID_FOR_BIDDING_STRATEGY = 67
        CANNOT_EXCLUDE_CRITERION = 68
        CANNOT_REMOVE_CRITERION = 69
        INVALID_PRODUCT_BIDDING_CATEGORY = 76
        MISSING_SHOPPING_SETTING = 77
        INVALID_MATCHING_FUNCTION = 78
        LOCATION_FILTER_NOT_ALLOWED = 79
        INVALID_FEED_FOR_LOCATION_FILTER = 98
        LOCATION_FILTER_INVALID = 80
        CANNOT_SET_GEO_TARGET_CONSTANTS_WITH_FEED_ITEM_SETS = 123
        CANNOT_SET_BOTH_ASSET_SET_AND_FEED = 140
        CANNOT_SET_FEED_OR_FEED_ITEM_SETS_FOR_CUSTOMER = 142
        CANNOT_SET_ASSET_SET_FIELD_FOR_CUSTOMER = 150
        CANNOT_SET_GEO_TARGET_CONSTANTS_WITH_ASSET_SETS = 143
        CANNOT_SET_ASSET_SETS_WITH_FEED_ITEM_SETS = 144
        INVALID_LOCATION_GROUP_ASSET_SET = 141
        INVALID_LOCATION_GROUP_RADIUS = 124
        INVALID_LOCATION_GROUP_RADIUS_UNIT = 125
        CANNOT_ATTACH_CRITERIA_AT_CAMPAIGN_AND_ADGROUP = 81
        HOTEL_LENGTH_OF_STAY_OVERLAPS_WITH_EXISTING_CRITERION = 82
        HOTEL_ADVANCE_BOOKING_WINDOW_OVERLAPS_WITH_EXISTING_CRITERION = 83
        FIELD_INCOMPATIBLE_WITH_NEGATIVE_TARGETING = 84
        INVALID_WEBPAGE_CONDITION = 85
        INVALID_WEBPAGE_CONDITION_URL = 86
        WEBPAGE_CONDITION_URL_CANNOT_BE_EMPTY = 87
        WEBPAGE_CONDITION_URL_UNSUPPORTED_PROTOCOL = 88
        WEBPAGE_CONDITION_URL_CANNOT_BE_IP_ADDRESS = 89
        WEBPAGE_CONDITION_URL_DOMAIN_NOT_CONSISTENT_WITH_CAMPAIGN_SETTING = 90
        WEBPAGE_CONDITION_URL_CANNOT_BE_PUBLIC_SUFFIX = 91
        WEBPAGE_CONDITION_URL_INVALID_PUBLIC_SUFFIX = 92
        WEBPAGE_CONDITION_URL_VALUE_TRACK_VALUE_NOT_SUPPORTED = 93
        WEBPAGE_CRITERION_URL_EQUALS_CAN_HAVE_ONLY_ONE_CONDITION = 94
        WEBPAGE_CRITERION_NOT_SUPPORTED_ON_NON_DSA_AD_GROUP = 95
        CANNOT_TARGET_USER_LIST_FOR_SMART_DISPLAY_CAMPAIGNS = 99
        CANNOT_TARGET_PLACEMENTS_FOR_SEARCH_CAMPAIGNS = 126
        LISTING_SCOPE_TOO_MANY_DIMENSION_TYPES = 100
        LISTING_SCOPE_TOO_MANY_IN_OPERATORS = 101
        LISTING_SCOPE_IN_OPERATOR_NOT_SUPPORTED = 102
        DUPLICATE_LISTING_DIMENSION_TYPE = 103
        DUPLICATE_LISTING_DIMENSION_VALUE = 104
        CANNOT_SET_BIDS_ON_LISTING_GROUP_SUBDIVISION = 105
        INVALID_LISTING_GROUP_HIERARCHY = 106
        LISTING_GROUP_UNIT_CANNOT_HAVE_CHILDREN = 107
        LISTING_GROUP_SUBDIVISION_REQUIRES_OTHERS_CASE = 108
        LISTING_GROUP_REQUIRES_SAME_DIMENSION_TYPE_AS_SIBLINGS = 109
        LISTING_GROUP_ALREADY_EXISTS = 110
        LISTING_GROUP_DOES_NOT_EXIST = 111
        LISTING_GROUP_CANNOT_BE_REMOVED = 112
        INVALID_LISTING_GROUP_TYPE = 113
        LISTING_GROUP_ADD_MAY_ONLY_USE_TEMP_ID = 114
        LISTING_SCOPE_TOO_LONG = 115
        LISTING_SCOPE_TOO_MANY_DIMENSIONS = 116
        LISTING_GROUP_TOO_LONG = 117
        LISTING_GROUP_TREE_TOO_DEEP = 118
        INVALID_LISTING_DIMENSION = 119
        INVALID_LISTING_DIMENSION_TYPE = 120
        ADVERTISER_NOT_ON_ALLOWLIST_FOR_COMBINED_AUDIENCE_ON_DISPLAY = 127
        CANNOT_TARGET_REMOVED_COMBINED_AUDIENCE = 128
        INVALID_COMBINED_AUDIENCE_ID = 129
        CANNOT_TARGET_REMOVED_CUSTOM_AUDIENCE = 130
        HOTEL_CHECK_IN_DATE_RANGE_OVERLAPS_WITH_EXISTING_CRITERION = 131
        HOTEL_CHECK_IN_DATE_RANGE_START_DATE_TOO_EARLY = 132
        HOTEL_CHECK_IN_DATE_RANGE_END_DATE_TOO_LATE = 133
        HOTEL_CHECK_IN_DATE_RANGE_REVERSED = 134
        BROAD_MATCH_MODIFIER_KEYWORD_NOT_ALLOWED = 135
        ONE_AUDIENCE_ALLOWED_PER_ASSET_GROUP = 136
        AUDIENCE_NOT_ELIGIBLE_FOR_CAMPAIGN_TYPE = 137
        AUDIENCE_NOT_ALLOWED_TO_ATTACH_WHEN_AUDIENCE_GROUPED_SET_TO_FALSE = 138
        CANNOT_TARGET_CUSTOMER_MATCH_USER_LIST = 139
        NEGATIVE_KEYWORD_SHARED_SET_DOES_NOT_EXIST = 145
        CANNOT_ADD_REMOVED_NEGATIVE_KEYWORD_SHARED_SET = 146
        CANNOT_HAVE_MULTIPLE_NEGATIVE_KEYWORD_LIST_PER_ACCOUNT = 147
        CUSTOMER_CANNOT_ADD_CRITERION_OF_THIS_TYPE = 149
        CANNOT_TARGET_SIMILAR_USER_LIST = 151
        CANNOT_ADD_AUDIENCE_SEGMENT_CRITERION_WHEN_AUDIENCE_GROUPED_IS_SET = 152
        ONE_AUDIENCE_ALLOWED_PER_AD_GROUP = 153
        INVALID_DETAILED_DEMOGRAPHIC = 154
        CANNOT_RECOGNIZE_BRAND = 155
        BRAND_SHARED_SET_DOES_NOT_EXIST = 156
        CANNOT_ADD_REMOVED_BRAND_SHARED_SET = 157
        ONLY_EXCLUSION_BRAND_LIST_ALLOWED_FOR_CAMPAIGN_TYPE = 158
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(self, key: NoReturn) -> bool: ...  # type: ignore[override]
