import subprocess
from pathlib import Path


def main() -> None:
    project_dir = Path.cwd()

    if "{{ cookiecutter.make_http_requests }}" == "no":
        path = project_dir / "app" / "api" / "services" / "request.py"
        if path.exists():
            path.unlink()

    subprocess.run(["uv", "sync"], cwd=project_dir)


if __name__ == "__main__":
    main()
