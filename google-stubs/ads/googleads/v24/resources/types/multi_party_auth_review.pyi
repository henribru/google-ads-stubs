from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v24.enums.types.multi_party_auth_operation_type import (
    MultiPartyAuthOperationTypeEnum,
)
from google.ads.googleads.v24.enums.types.multi_party_auth_review_status import (
    MultiPartyAuthReviewStatusEnum,
)
from google.ads.googleads.v24.enums.types.multi_party_auth_review_target_resource import (
    MultiPartyAuthReviewTargetResourceEnum,
)
from google.ads.googleads.v24.resources.types.customer_user_access import (
    CustomerUserAccess,
)
from google.ads.googleads.v24.resources.types.customer_user_access_invitation import (
    CustomerUserAccessInvitation,
)

_M = TypeVar("_M")

class CustomerUserAccessInvitationReview(proto.Message):
    new_customer_user_access_invitation: CustomerUserAccessInvitation
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        new_customer_user_access_invitation: CustomerUserAccessInvitation = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["new_customer_user_access_invitation"]
    ) -> bool: ...

class CustomerUserAccessReview(proto.Message):
    old_customer_user_access: str
    new_customer_user_access: CustomerUserAccess
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        old_customer_user_access: str = ...,
        new_customer_user_access: CustomerUserAccess = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["old_customer_user_access", "new_customer_user_access"]
    ) -> bool: ...

class MultiPartyAuthReview(proto.Message):
    resource_name: str
    multi_party_auth_review_id: int
    creation_date_time: str
    review_status: MultiPartyAuthReviewStatusEnum.MultiPartyAuthReviewStatus
    approval_date_time: str
    justification: str
    request_user_email: str
    operation_type: MultiPartyAuthOperationTypeEnum.MultiPartyAuthOperationType
    target_resource: (
        MultiPartyAuthReviewTargetResourceEnum.MultiPartyAuthReviewTargetResource
    )
    customer_user_access_review: CustomerUserAccessReview
    customer_user_access_invitation_review: CustomerUserAccessInvitationReview
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        multi_party_auth_review_id: int = ...,
        creation_date_time: str = ...,
        review_status: MultiPartyAuthReviewStatusEnum.MultiPartyAuthReviewStatus = ...,
        approval_date_time: str = ...,
        justification: str = ...,
        request_user_email: str = ...,
        operation_type: MultiPartyAuthOperationTypeEnum.MultiPartyAuthOperationType = ...,
        target_resource: MultiPartyAuthReviewTargetResourceEnum.MultiPartyAuthReviewTargetResource = ...,
        customer_user_access_review: CustomerUserAccessReview = ...,
        customer_user_access_invitation_review: CustomerUserAccessInvitationReview = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "resource_name",
            "multi_party_auth_review_id",
            "creation_date_time",
            "review_status",
            "approval_date_time",
            "justification",
            "request_user_email",
            "operation_type",
            "target_resource",
            "customer_user_access_review",
            "customer_user_access_invitation_review",
        ],
    ) -> bool: ...
