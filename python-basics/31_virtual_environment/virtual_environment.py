# =============================================================
# PYTHON VIRTUAL ENVIRONMENTS
# =============================================================

# A virtual environment is an isolated Python environment.
# It has its own Python interpreter and its own packages –
# completely separate from the system Python and other projects.
#
# Why use virtual environments?
#   - Project A needs Django 4.0, Project B needs Django 5.0
#     → without venv they would conflict.
#   - Keeps the system Python clean.
#   - Makes projects reproducible (requirements.txt).
#   - Standard practice for all Python projects.

# NOTE: Virtual environments are created and managed in the TERMINAL,
#       not inside a Python script.
#       This file documents the commands and explains each step.

# =============================================================
# CREATING A VIRTUAL ENVIRONMENT  (venv – built-in, Python 3.3+)
# =============================================================

# Command (run in your project folder):
#
#   python3 -m venv venv
#
# Breakdown:
#   python3 -m venv  – run the venv module
#   venv             – name of the folder to create (convention: "venv" or ".venv")
#
# This creates a folder called "venv/" containing:
#   venv/
#   ├── bin/          (mac/linux) or Scripts/ (windows)
#   │   ├── python    – isolated Python interpreter
#   │   ├── pip       – isolated pip
#   │   └── activate  – script to activate the environment
#   ├── include/
#   └── lib/
#       └── python3.x/
#           └── site-packages/   ← your installed packages go here

# =============================================================
# ACTIVATING THE VIRTUAL ENVIRONMENT
# =============================================================

# macOS / Linux:
#   source venv/bin/activate
#
# Windows CMD:
#   venv\Scripts\activate.bat
#
# Windows PowerShell:
#   venv\Scripts\Activate.ps1
#
# After activation, your prompt changes:
#   (venv) user@machine:~/myproject$
#
# Now "python" and "pip" refer to the VENV versions, not the system ones.

# =============================================================
# DEACTIVATING THE VIRTUAL ENVIRONMENT
# =============================================================

# Simply run:
#   deactivate
#
# Your prompt returns to normal.

# =============================================================
# INSTALLING PACKAGES INSIDE A VENV
# =============================================================

# With the venv activated:
#   pip install requests
#   pip install numpy pandas matplotlib
#   pip install django==5.0
#   pip install "flask>=2.0,<3.0"

# =============================================================
# requirements.txt  – freeze and share dependencies
# =============================================================

# Save all currently installed packages and their exact versions:
#   pip freeze > requirements.txt
#
# Example requirements.txt content:
#   Django==5.0.1
#   numpy==1.26.4
#   pandas==2.2.1
#   requests==2.31.0
#
# Re-create the same environment on another machine (or after cloning a repo):
#   python3 -m venv venv
#   source venv/bin/activate
#   pip install -r requirements.txt

# =============================================================
# .gitignore – exclude the venv folder from git
# =============================================================

# The venv/ folder is large and machine-specific. Never commit it.
# Add to .gitignore:
#
#   venv/
#   .venv/
#   __pycache__/
#   *.pyc
#   *.pyo
#   .env

# =============================================================
# CHECKING WHAT'S INSTALLED
# =============================================================

#   pip list                  – list all installed packages
#   pip show requests         – show info about a specific package
#   pip install --upgrade pip – upgrade pip itself

# =============================================================
# FULL PROJECT SETUP WORKFLOW  (step by step)
# =============================================================

# 1. Create your project folder
#       mkdir my_project && cd my_project
#
# 2. Create a virtual environment
#       python3 -m venv venv
#
# 3. Activate it
#       source venv/bin/activate          # mac/linux
#       venv\Scripts\activate             # windows
#
# 4. Install packages
#       pip install requests flask
#
# 5. Write your code
#       touch main.py
#
# 6. Freeze dependencies
#       pip freeze > requirements.txt
#
# 7. Add .gitignore
#       echo "venv/" >> .gitignore
#
# 8. Commit to git
#       git init && git add . && git commit -m "Initial commit"
#
# When someone clones your repo:
#   git clone <url>
#   cd my_project
#   python3 -m venv venv
#   source venv/bin/activate
#   pip install -r requirements.txt

# =============================================================
# ALTERNATIVE TOOLS
# =============================================================

# conda       – popular in data science, manages both packages and Python versions
#               conda create -n myenv python=3.11
#               conda activate myenv
#               conda install numpy pandas
#
# pipenv      – combines pip + venv automatically
#               pipenv install requests
#               pipenv shell
#
# poetry      – modern dependency management + packaging
#               poetry new my_project
#               poetry add requests
#               poetry shell
#
# pyenv       – manage multiple Python VERSION installations
#               pyenv install 3.11.0
#               pyenv local 3.11.0
#
# uv          – extremely fast pip + venv replacement (written in Rust, 2024+)
#               uv venv
#               uv pip install requests

# =============================================================
# INSPECT YOUR CURRENT ENVIRONMENT FROM PYTHON
# =============================================================

import sys
import os

print(f"Python:     {sys.version}")
print(f"Executable: {sys.executable}")
print(f"Prefix:     {sys.prefix}")

# Check if we are inside a virtual environment
in_venv = (
    hasattr(sys, "real_prefix")                              # virtualenv
    or sys.base_prefix != sys.prefix                         # venv
    or os.environ.get("VIRTUAL_ENV") is not None             # activated
    or os.environ.get("CONDA_DEFAULT_ENV") is not None       # conda
)
print(f"In venv:    {in_venv}")

# List installed packages programmatically
try:
    from importlib.metadata import packages_distributions
    pkgs = sorted(packages_distributions().keys())
    print(f"\nInstalled packages ({len(pkgs)}):")
    for pkg in pkgs[:10]:
        print(f"  {pkg}")
    if len(pkgs) > 10:
        print(f"  ... and {len(pkgs) - 10} more")
except ImportError:
    import pkg_resources
    pkgs = sorted([p.project_name for p in pkg_resources.working_set])
    for pkg in pkgs[:10]:
        print(f"  {pkg}")
