# Advent Of Code 2019

My solutions for the [Advent of Code 2019](https://adventofcode.com/2019).

Written in Python 3.7 using [VSCode](https://code.visualstudio.com/), with occational help from [`mypy`](http://mypy-lang.org/) and [`pylint`](https://www.pylint.org/).

## Solutions

Solutions are found within their day directories: 1 - 31

Each day contains `solution.py`, which contains the methods `solve_a` and `solve_b`, which solve part A and B of the problem.

There will also be a `PART.EXT` file, containing my input for that part of the problem, in either a `txt`, `json`, or `csv` file.

Each solution also contains a `__version__` variable, denoting the version of the solution - of which all start at `1.0.0`

## Additionals

The `template.py` file is a base template of all `solution.py` files, while `utils.py` generates the `template.py` file for the next day and exposes a `load_input` method.

`load_input` allows a solution to be passed the input of the current problem without having to manually open the file and parse the text, JSON, or CSV file.

## Docs

Besides this `README.md`, there is also a [`CHANGELOG.md`](./CHANGELOG.md), which documents all the changes made to the project.
