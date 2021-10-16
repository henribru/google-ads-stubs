from typing import Any

import proto

from google.ads.googleads.v8.resources.types import billing_setup as billing_setup

__protobuf__: Any

class GetBillingSetupRequest(proto.Message):
    resource_name: Any

class MutateBillingSetupRequest(proto.Message):
    customer_id: Any
    operation: Any

class BillingSetupOperation(proto.Message):
    create: Any
    remove: Any

class MutateBillingSetupResponse(proto.Message):
    result: Any

class MutateBillingSetupResult(proto.Message):
    resource_name: Any
