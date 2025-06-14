import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.resources.types import customer_sk_ad_network_conversion_value_schema
from google.rpc import status_pb2

__protobuf__: Incomplete

class CustomerSkAdNetworkConversionValueSchemaOperation(proto.Message):
    update: customer_sk_ad_network_conversion_value_schema.CustomerSkAdNetworkConversionValueSchema

class MutateCustomerSkAdNetworkConversionValueSchemaRequest(proto.Message):
    customer_id: str
    operation: CustomerSkAdNetworkConversionValueSchemaOperation
    validate_only: bool
    enable_warnings: bool

class MutateCustomerSkAdNetworkConversionValueSchemaResult(proto.Message):
    resource_name: str
    app_id: str

class MutateCustomerSkAdNetworkConversionValueSchemaResponse(proto.Message):
    result: MutateCustomerSkAdNetworkConversionValueSchemaResult
    warning: status_pb2.Status
