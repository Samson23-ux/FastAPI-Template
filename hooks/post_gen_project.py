import os
import re
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

    """Collapse 3+ consecutive blank lines down to a single blank line,
    in every text file under root."""
    for dirpath, _, filenames in os.walk(root):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
            except (UnicodeDecodeError, IsADirectoryError):
                # Skip binary files or anything unreadable as text
                continue

            cleaned = re.sub(r"\n{3,}", "\n\n", content)

            if cleaned != content:
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(cleaned)

    if "{{ cookiecutter.make_http_requests }}" == "no":
        path = project_dir / "app" / "api" / "services" / "request.py"
        if path.exists():
            path.unlink()

    if "{{ cookiecutter.auth_with_github }}" == "no" or "{{ cookiecutter.auth_with_google }}" == "no":
        path = project_dir / "app" / "util.py"
        if path.exists():
            path.unlink()

    subprocess.run(["uv", "sync"], cwd=project_dir)
    subprocess.run(["uvx", "black", "."], cwd=project_dir)


if __name__ == "__main__":
    main()
