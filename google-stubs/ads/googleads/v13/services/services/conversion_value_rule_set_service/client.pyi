from typing import Dict, MutableSequence, Optional, Sequence, Tuple, Type, Union

from _typeshed import Incomplete
from google.api_core import (
    client_options as client_options_lib,
    gapic_v1,
    retry as retries,
)
from google.auth import credentials as ga_credentials

from google.ads.googleads.v13.services.types import conversion_value_rule_set_service

from .transports.base import ConversionValueRuleSetServiceTransport

class ConversionValueRuleSetServiceClientMeta(type):
    def get_transport_class(
        cls, label: Optional[str] = ...
    ) -> Type[ConversionValueRuleSetServiceTransport]: ...

class ConversionValueRuleSetServiceClient(
    metaclass=ConversionValueRuleSetServiceClientMeta
):
    DEFAULT_ENDPOINT: str
    DEFAULT_MTLS_ENDPOINT: Incomplete
    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs): ...
    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs): ...
    from_service_account_json = from_service_account_file
    @property
    def transport(self) -> ConversionValueRuleSetServiceTransport: ...
    def __enter__(self) -> ConversionValueRuleSetServiceClient: ...
    def __exit__(self, type, value, traceback) -> None: ...
    @staticmethod
    def campaign_path(customer_id: str, campaign_id: str) -> str: ...
    @staticmethod
    def parse_campaign_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def conversion_value_rule_path(
        customer_id: str, conversion_value_rule_id: str
    ) -> str: ...
    @staticmethod
    def parse_conversion_value_rule_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def conversion_value_rule_set_path(
        customer_id: str, conversion_value_rule_set_id: str
    ) -> str: ...
    @staticmethod
    def parse_conversion_value_rule_set_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def customer_path(customer_id: str) -> str: ...
    @staticmethod
    def parse_customer_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def common_billing_account_path(billing_account: str) -> str: ...
    @staticmethod
    def parse_common_billing_account_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def common_folder_path(folder: str) -> str: ...
    @staticmethod
    def parse_common_folder_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def common_organization_path(organization: str) -> str: ...
    @staticmethod
    def parse_common_organization_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def common_project_path(project: str) -> str: ...
    @staticmethod
    def parse_common_project_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def common_location_path(project: str, location: str) -> str: ...
    @staticmethod
    def parse_common_location_path(path: str) -> Dict[str, str]: ...
    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = ...,
        transport: Optional[Union[str, ConversionValueRuleSetServiceTransport]] = ...,
        client_options: Optional[Union[client_options_lib.ClientOptions, dict]] = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    def mutate_conversion_value_rule_sets(
        self,
        request: Optional[
            Union[
                conversion_value_rule_set_service.MutateConversionValueRuleSetsRequest,
                dict,
            ]
        ] = ...,
        *,
        customer_id: Optional[str] = ...,
        operations: Optional[
            MutableSequence[
                conversion_value_rule_set_service.ConversionValueRuleSetOperation
            ]
        ] = ...,
        retry: Union[retries.Retry, gapic_v1.method._MethodDefault] = ...,
        timeout: Union[float, object] = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> conversion_value_rule_set_service.MutateConversionValueRuleSetsResponse: ...
