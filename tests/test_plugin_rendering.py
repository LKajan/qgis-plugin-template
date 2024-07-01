from __future__ import annotations

import copy
from typing import TYPE_CHECKING

import pytest
from pytest_copier import CopierFixture

if TYPE_CHECKING:
    from pathlib import Path
    from typing import Any, Sequence

    from pytest_copier.plugin import CopierProject


@pytest.fixture(scope="session")
def copier_template_paths() -> Sequence[str]:
    return (
        "plugin_template",
        "includes",
        "copier.yml",
    )


@pytest.fixture(scope="session")
def copier_defaults() -> dict[str, Any]:
    return {
        "plugin_name": "My QGIS plugin",
        "plugin_package": "plugin",
        "license": "GPL2",
    }


SUPPORTED_COMBINATIONS = [
    {},  # test with default values
    {"license": "GPL3"},
]


@pytest.fixture(scope="session")
def session_copier(copier_template: Path, copier_defaults: dict[str, Any]) -> CopierFixture:
    return CopierFixture(template=copier_template, defaults=copier_defaults, monkeypatch=None)


@pytest.fixture
def context(session_context: dict[str, str]):
    return copy.deepcopy(session_context)


def _fixture_id(ctx: dict[str, str]):
    """Helper to get a user friendly test name from the parametrized context."""
    if not ctx:
        return "default"
    return "-".join(f"{key}:{value}" for key, value in ctx.items())


@pytest.fixture(scope="session", params=SUPPORTED_COMBINATIONS, ids=_fixture_id)
def copied_project(
    session_copier: CopierFixture,
    request: pytest.FixtureRequest,
    tmp_path_factory: pytest.TempPathFactory,
) -> CopierProject:
    context_override = request.param

    plugin_path = tmp_path_factory.mktemp("plugin")

    return session_copier.copy(dst=plugin_path, **context_override)


def test_rendered_project(copied_project: CopierProject):
    assert copied_project.path.is_dir()
    assert (copied_project.path / "src" / copied_project.answers["plugin_package"]).exists()
