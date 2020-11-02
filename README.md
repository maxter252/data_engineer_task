# Set Up and Run Instructions
Change directory to the root directory of the repo once you have cloned it.
The following commands are for MacOS, please substitute the appropriate command for Windows / Linux where necessary. 
You may then need to set your python path to the following:
```
export PYTHONPATH="$PWD/src"
```


To run this pipeline first create a local environment
```bash
python -m venv .venv
```

activate the local env
```bash
source .venv/bin/activate
```
Then install the requirements
```bash
pip install requirements.txt
```

Now run the code. 
```bash
python src/scripts/select_venue.py
```

The tests can be run using pytest with the command
```bash
pytest
```
from the root directory.
and for coverage data
```bash
pytest -v --cov=src/scripts --cov-report term-missing
```
For linting use
```bash
flake8 ./src --count --max-complexity=10 --max-line-length=127 --statistics
```