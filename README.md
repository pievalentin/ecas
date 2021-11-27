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
Example of output:
```
Your status is: InProcess

The detail of your process is:
- We received your application for permanent residence  on December 10, 2020.
- We sent you correspondence acknowledging receipt of your application(s) on October 22, 2021.
- We started processing your application on October 22, 2021.
- We sent you correspondence on October 22, 2021. If you have not yet provided the information or the requested documents, please do so as soon as possible.  
Please wait until you receive the correspondence before sending us additional information, as the correspondence will outline all information that is required.
- We sent you medical instructions on November 25, 2021. To avoid delays, please provide us the information requested in the letter as soon as possible.  
Please consider delays in mail delivery before contacting us.
```

When everything was verified by ircc, your status will change to `DecisionMade` 

For more details, you can
```bash
ecas --help
```
## Find your country code

To find your country code, you can look it up [in this file](/country_code.csv)

## NB
Use this tool responsibly. Don't spam IRCC server :)
