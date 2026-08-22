# Setting up the environment
(Linux)
> sudo apt update
> sudo apt install python3.13 python3.13-venv python3-pip
> python3 -m venv .venv
> source .venv/bin/activate

(Windows)
> winget install Python.Python.3.13
> py -m venv .venv
> .\.venv\Scripts\Activate.ps1

# Installing dev-tools
(Linux / Windows)
> python -m pip install --upgrade pip
> pip install -r requirements-dev.txt

# Testing the code
(Linux / Windows)
> pytest

# Running the code
(Linux / Windows)
> python Main.py