import os
import subprocess
from pathlib import Path

if "{{ cookiecutter.make_http_requests }}" == "no":
    path = (
        Path(__file__).parent.parent
        / "{{ cookiecutter.project_name }}"
        / "app"
        / "api"
        / "services"
        / "request.py"
    )
    os.remove(path)

subprocess.run(["uv", "sync"])
