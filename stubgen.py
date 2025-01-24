import os
import shutil
import subprocess
from pathlib import Path


def copytree(src, dst, symlinks=False, ignore=None, overwrite=True):
    if not os.path.exists(dst):
        os.makedirs(dst)
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            copytree(s, d, symlinks, ignore, overwrite)
        else:
            if not os.path.exists(d) or (
                overwrite and os.stat(s).st_mtime - os.stat(d).st_mtime > 1
            ):
                shutil.copy2(s, d)


# TODO: Explore options? E.g. --include-docstrings
subprocess.run(["stubgen", "google", "-o", ".."], cwd="google-ads-python", check=True)
copytree("googleads", "google-stubs/ads/googleads/", overwrite=False)
shutil.rmtree("googleads")
for dir, _, _ in os.walk("google-stubs/ads/googleads"):
    Path(dir, "__init__.pyi").touch()
