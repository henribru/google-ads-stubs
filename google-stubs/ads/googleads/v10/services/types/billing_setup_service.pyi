import proto
from _typeshed import Incomplete

from google.ads.googleads.v10.resources.types import billing_setup as billing_setup

__protobuf__: Incomplete

class MutateBillingSetupRequest(proto.Message):
    customer_id: Incomplete
    operation: Incomplete

class BillingSetupOperation(proto.Message):
    create: Incomplete
    remove: Incomplete

class MutateBillingSetupResponse(proto.Message):
    result: Incomplete

class MutateBillingSetupResult(proto.Message):
    resource_name: Incomplete
