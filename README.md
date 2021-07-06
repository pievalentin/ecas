# Ecas RP automation script
This tool has been written to check the status of your PR application in ECAS automatically. This avoid multiple click and form filling. You can set alert using a system like cron.
## Getting started
### From PyPI
```bash
pip3 install ecas
```
### From Source
1. Get the code

First get this code on your machine with
```bash
git clone git@github.com:pievalentin/ecas.git && cd ecas
```
2. Install the tool

Run this command to install the tool:
```bash
pip3 install .
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

To find your country code, you can look it up [in this file](/country_code.html)

## NB
Use this tool responsibly. Don't spam IRCC server :)
