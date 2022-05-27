# inflam

![Continuous Integration build in GitHub Actions](https://github.com/nickynicolson/python-intermediate-inflammation/workflows/CI/badge.svg?branch=main)

Inflam is a data management system written in Python that manages trial data used in clinical inflammation studies.

## Main features

Here are some key features of Inflam:

- Provide basic statistical analyses over clinical trial data
- Ability to work on trial data in Comma-Separated Value (CSV) format
- Generate plots of trial data
- Analytical functions and views can be easily extended based on its Model-View-Controller architecture

## Prerequisites

Inflam requires the following Python packages:

- [NumPy](https://www.numpy.org/) - makes use of NumPy's statistical functions
- [Matplotlib](https://matplotlib.org/stable/index.html) - uses Matplotlib to generate statistical plots

The following optional packages are required to run Inflam's unit tests:

- [pytest](https://docs.pytest.org/en/stable/) - Inflam's unit tests are written using pytest
- [pytest-cov](https://pypi.org/project/pytest-cov/) - Adds test coverage stats to unit testing

## Installation/deployment

It is recommended to use a virtual environment to run and develop this software.

```
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
```

## Basic usage

```
$ python inflammation-analysis.py --help
usage: inflammation-analysis.py [-h] [--view {visualize,record}] [--format {text,json}] [--patient PATIENT]
                                infiles [infiles ...]

A basic patient inflammation data management system

positional arguments:
  infiles               Input CSV(s) containing inflammation series for each patient

optional arguments:
  -h, --help            show this help message and exit
  --view {visualize,record}
                        Which view should be used?
  --format {text,json}  Which data format should be used?
  --patient PATIENT     Which patient should be displayed?
```

## Contributing

Bug reports and feature requests are welcome - please use the [github issue tracker](https://github.com/carpentries-incubator/python-intermediate-inflammation/issues)

## Contact information

- [Nicky Nicolson](https://github.com/nickynicolson)

## Credits

Thanks to the [Software Sustainability Institute](https://software.ac.uk/) for including the course [Python intermediate development](https://carpentries-incubator.github.io/python-intermediate-development/) in their "research camp" [Next steps in coding](https://www.software.ac.uk/RSCamp-next-steps-coding) in May 2022.

 
## Citation

TBC

## Licence

TBC