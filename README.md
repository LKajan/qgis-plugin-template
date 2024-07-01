# QGIS Plugin Template

[Copier](https://copier.readthedocs.io/en/stable/) template for [QGIS](https://qgis.org/) plugins.

This template makes it easy to create a new QGIS plugin project with a modern development environment.

## Usage

### Prerequisites

The template is built using [Copier](https://copier.readthedocs.io/en/stable/), so you must have it installed.

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
