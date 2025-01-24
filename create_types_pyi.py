import importlib
from pathlib import Path

from google.ads.googleads import client

for version in client._VALID_API_VERSIONS:
    version_package = importlib.import_module(f"google.ads.googleads.{version}")
    with open(Path("google-stubs/ads/googleads/", version, "__init__.pyi"), "w") as f:
        for (
            type_name,
            package_path,
        ) in version_package._lazy_type_to_package_map.items():
            f.write(f"from {package_path} import {type_name} as {type_name}\n")

        # f.write("__all__ = [\n")
        # for type_name in module._lazy_type_to_package_map:
        #     f.write(f'    "{type_name}",\n')
        # f.write("]\n")
