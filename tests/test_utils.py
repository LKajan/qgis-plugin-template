from __future__ import annotations

import subprocess

import pytest


def run_cli_command(args: list[str], cwd: str):
    try:
        subprocess.check_output(
            args,
            cwd=cwd,
            timeout=20,
            universal_newlines=True,
            stderr=subprocess.STDOUT,
        )
    except subprocess.CalledProcessError as exc:
        pytest.fail(exc.output)
    except subprocess.TimeoutExpired:
        pytest.fail("Command timeouted")
