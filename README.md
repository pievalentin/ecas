# Ecas RP automation script
This tool has been written to check the status of your PR application in ECAS automatically. This avoid multiple click and form filling. You can set alert using a system like cron.

## Getting started
### From PyPI
```bash
pip3 install ecas
```
### From Source
1. Get poetry

On Linux & MacOS
```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```
On Windows with powershell
```
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python -
```
2. Get the code
```bash
git clone git@github.com:pievalentin/ecas.git && cd ecas
```
3. Build it
```bash
poetry build
```
The previous command will create a dist folder. Now run:
```
pip3 install dist/ecas*.whl
```
Restart your terminal so that `ecas` is available.
## Usage

```bash
ecas lastname iuc_number birthday birth_country_code
```

For example for France:
```bash
ecas Dupont 112245589 "2001-01-31" 022
```

For more details, you can
```bash
ecas --help
```
## Find your country code

To find your country code, you can look it up [in this file](/country_code.csv)

## NB
Use this tool responsibly. Don't spam IRCC server :)
