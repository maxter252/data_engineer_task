# Notes For Improvement
- Implement more widespread use Pydantic validators in order to increase data validation. Currently this is only implemented for the UserInput validation type.
- Should have used the set data type instead of dict type for constant time look ups, but does not affect the functionality of the script
- If N is the number of users and M is the number of venues, this algorithm will run in O(N x M) time. (Assuming that the number of foods and drinks specified for each venue and each user can be assumed small relative to M and N)
- Additional tests should be created to test for edge and corner cases.
- Current behavoir of script is to raise a validation error if any user preference data is not specified correctly, however this could be adapted to pass poorly formed data and proceed with the remaining data whilst logging the problematic data.

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