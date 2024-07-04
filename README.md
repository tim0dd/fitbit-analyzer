## Frontend

## Backend

### Initial Setup

#### Prerequisites
- python (version 3.12 used but likely works with other verions, too)
- pip

Note that commands below were tested in bash and likely differ in a windows shell

#### Steps
1. Create venv
```
python -m venv ./venv
```
2. Activate venv
```
source ./venv/bin/activate
```
3. Install dependencies via pip
```
pip install -r ./backend/requirements.txt
```
4. Setup for module imports
```
pip install -e ./backend
```
### Running the backend
With the venv enabled, run:
```uvicorn --app-dir="./backend/app" main:app --reload --log-level=debug```
