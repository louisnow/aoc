# Advent of Code

See https://adventofcode.com/

## Running

The code has no external dependencies so it will work without having to install additional libraries. The `requirements.txt` contains linting and formatting dependencies.

Format

`python3 <year>/<day>/<day>-<part>.py`

Example

`python3 2020/05/05-2.py`

## Editor

If VS Code is your editor

- Copy `.vscode/settings.json.default` to `.vscode/settings.json`

- Create a local python environment and install dependencies for linting and autoformatting

```
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

If you want to use an editor of your choice, I use [black](https://github.com/psf/black) for formatting and [mypy](https://github.com/python/mypy) for linting
