import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.resources.types import billing_setup

__protobuf__: Incomplete

class MutateBillingSetupRequest(proto.Message):
    customer_id: str
    operation: BillingSetupOperation

class BillingSetupOperation(proto.Message):
    create: billing_setup.BillingSetup
    remove: str

class MutateBillingSetupResponse(proto.Message):
    result: MutateBillingSetupResult

class MutateBillingSetupResult(proto.Message):
    resource_name: str
