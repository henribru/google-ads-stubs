#!/usr/bin/env bash

set -eou pipefail
shopt -s globstar

uv remove google-ads && uv add google-ads
git clone https://github.com/googleads/google-ads-python.git || true
cd google-ads-python
git restore .
git pull
rm __init__.py
sed -i 's/: OptionalRetry/: Union\[retries\.Retry, gapic_v1\.method\._MethodDefault, None\]/' google/ads/googleads/**/{client,pagers}.py
sed -i 's/: OptionalAsyncRetry/: Union\[retries_async\.AsyncRetry, gapic_v1\.method\._MethodDefault, None\]/' google/ads/googleads/**/pagers.py
sed -i 's/: OptionalRetry/: Union\[retries\.AsyncRetry, gapic_v1\.method\._MethodDefault, None\]/' google/ads/googleads/**/async_client.py
sed -i 's/: OptionalRetry/: Union\[retries\.Retry, gapic_v1\.method\._MethodDefault, None\]/' google/ads/googleads/v*/services/services/you_tube_video_upload_service/transports/rest_resumable.py
cd ..
rm -rf google-stubs/ads/googleads/v*
uv run python stubgen.py
uv run python create_type_stubs.py
uv run python create_enums.py
uv run python create_service_overloads.py
uv run python fixup_versions.py
./stubdefaulter.sh
mv .gitignore gitignore  # Workaround for ruff's handling of gitignore files with whitelisting.
uv run ruff check google-stubs --fix --unsafe-fixes
uv run ruff format google-stubs
mv gitignore .gitignore
sed -i 's/def operations_client(self) -> operations_v1\.OperationsClient: \.\.\./def operations_client(self) -> operations_v1\.OperationsClient: \.\.\.  # type: ignore\[override\]/' google-stubs/ads/googleads/v*/**/*.pyi
sed -i 's/def operations_client(self) -> operations_v1\.OperationsAsyncClient: \.\.\./def operations_client(self) -> operations_v1\.OperationsAsyncClient: \.\.\.  # type: ignore\[override\]/' google-stubs/ads/googleads/v*/**/*.pyi
sed -i 's/from grpc.experimental import aio/from grpc.experimental import aio  # type: ignore[attr-defined]/' google-stubs/ads/googleads/**/*.pyi
sed -i 's/def time_remaining(self) -> float | None: \.\.\./def time_remaining(self) -> float | None: ...  # type: ignore\[override\]/' google-stubs/ads/googleads/v*/services/services/you_tube_video_upload_service/transports/resumable_upload_error_adapter.pyi
sed -i 's/def add_callback(self, callback: Any) -> None: \.\.\./def add_callback(self, callback: Any) -> None: ...  # type: ignore\[override\]/g' google-stubs/ads/googleads/v*/services/services/you_tube_video_upload_service/transports/resumable_upload_error_adapter.pyi
mv google-stubs google
uv run mypy --namespace-packages --explicit-package-bases google || true  # || true so we can move the folder back on failure.
mv google google-stubs
echo "Remember to update version compatibility in README"
