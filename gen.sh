#!/usr/bin/env bash

set -eou pipefail

# Manual: Clone https://github.com/googleads/google-ads-python
# Manual: Update google-ads-python dependency
# Manual: Update the following to match the API versions:
# - GoogleAdsFailure in errors.pyi
# - _V, imports and get_type default in client.pyi
# - _Request in exception_interceptor.pyi, logging_interceptor.pyi and metadata_inteceptor.pyi
cd google-ads-python
git restore .
git pull
rm __init__.py
shopt -s globstar
sed -i 's/: OptionalRetry/: Union\[retries\.Retry, gapic_v1\.method\._MethodDefault\]/' google/ads/googleads/**/*.py
cd ..
rm -rf google-stubs/ads/googleads/v*
uv run python stubgen.py
uv run python create_type_stubs.py
uv run python create_types_pyi.py
uv run create_enums.py
uv run create_service_overloads.py
./stubdefaulter.sh
mv .gitignore gitignore
uv run ruff check google-stubs --fix --unsafe-fixes
uv run ruff format google-stubs
mv gitignore .gitignore
sed -i 's/from typing/import types\nfrom typing/' google-stubs/ads/googleads/v*/**/client.pyi
sed -i 's/def operations_client(self) -> operations_v1\.OperationsClient: \.\.\./def operations_client(self) -> operations_v1\.OperationsClient: \.\.\.  # type: ignore\[override\]/' google-stubs/ads/googleads/v*/**/*.pyi
mv google-stubs google
uv run mypy --namespace-packages --explicit-package-bases google || true  # || true so we can move the folder back on failure.
mv google google-stubs
# Manual: Update version compatibility in README
