<<<<<<< HEAD
# config-compliance-checker
[![CI](https://github.com/NilooNil/config-compliance-checker/actions/workflows/ci.yml/badge.svg)](https://github.com/NilooNil/config-compliance-checker/actions/workflows/ci.yml)
=======
# Config Compliance Checker

**Goal:** Validate a server config against baseline policy (YAML).

## What you'll demonstrate
- YAML parsing
- Rule evaluation
- Clear pass/fail output + exit code

## Run
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python src/check_compliance.py --config sample/config.yaml --policy baseline/policies.yaml
pytest -q
```
>>>>>>> 7da42e1 (feat: initial commit - config compliance checker)
