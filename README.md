# Ecas RP automation script

## Getting started
First get this code on your machine with
```bash
git clone git@github.com:pievalentin/ecas.git && cd ecas
```

Run this command to install the dependencies:
```bash
pip3 install .
```

Restart your terminal, you can now:

```bash
ecas Lastname iuc_number Birthday<YYYY-MM-DD> birth_country_code<xxx>
```

For example for france:
```bash
ecas Dupont 112245589 "2001-01-01" 022
```

## Find your country code

To find your country code, you can look it up [in this file](/country_code.html)