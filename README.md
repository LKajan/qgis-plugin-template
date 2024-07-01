# QGIS Plugin Template

[![Copier](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-purple.json)](https://github.com/copier-org/copier)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![image](https://img.shields.io/github/license/lkajan/qgis-plugin-template)](https://github.com/LKajan/qgis-plugin-template?tab=MIT-1-ov-file)
[![Tests & Style checks](https://github.com/LKajan/qgis-plugin-template/actions/workflows/tests.yml/badge.svg)](https://github.com/LKajan/qgis-plugin-template/actions/workflows/tests.yml)

[Copier](https://copier.readthedocs.io/en/stable/) template for [QGIS](https://qgis.org/) plugins.

This template makes it easy to create a new QGIS plugin project with a modern development environment.

## Usage

### Prerequisites

A tool called [Copier](https://copier.readthedocs.io/en/stable/) is needed to create a plugin project from this template, so you must have it installed. Here are two ways to install Copier:

#### Install Copier with pipx

The recommended way to install Copier (like any other Python cli tools) is to install it with [pipx](https://pypa.github.io/pipx/). Pipx will install the application in a isolated environment and make it available as a command line utility. To install `pipx` follow the instructions from https://github.com/pypa/pipx#install-pipx.

```console
pipx install copier
```

#### Alternatively install Copier to your current python environment

```console
pip install copier
```

### Create a new plugin project

Creating a new plugin project with Copier creates a new folder for the project so navigate to the desired parent directory and use the following command. Pass the folder name as the last argument.

```console
copier copy --trust "gh:GispoCoding/qgis-plugin-template" <path-to-project>
```

### License

This project is licensed under the terms of the MIT license - see the [LICENSE](LICENSE) file for details.
