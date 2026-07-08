import os
import subprocess
from pathlib import Path


def main() -> None:
    root = "."
    project_dir = Path.cwd()

    for dirpath, _, filenames in os.walk(root):
        for filename in filenames:
            if filename.endswith(".jinja"):
                old_path = os.path.join(dirpath, filename)
                new_path = os.path.join(dirpath, filename[: -len(".jinja")])
                os.rename(old_path, new_path)

    if "{{ cookiecutter.make_http_requests }}" == "no":
        path = project_dir / "app" / "api" / "services" / "request.py"
        if path.exists():
            path.unlink()

    subprocess.run(["uv", "sync"], cwd=project_dir)


if __name__ == "__main__":
    main()
