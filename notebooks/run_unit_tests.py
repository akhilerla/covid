# Databricks notebook source
# MAGIC %md Test runner for `pytest`

# COMMAND ----------


%pip install -r attrs==21.4.0
cycler==0.11.0
fonttools==4.33.3
iniconfig==1.1.1
kiwisolver==1.4.2
matplotlib==3.5.1
numpy==1.22.3
packaging==21.3
pandas==1.4.2
pillow==9.3.0
pluggy==1.0.0
py==1.11.0
py4j==0.10.9.5
pyarrow==7.0.0
pyparsing==3.0.8
pyspark==3.2.2
pytest==7.2.0
python-dateutil==2.8.2
pytz==2022.1
six==1.16.0
tomli==2.0.1
wget==3.2

# COMMAND ----------

# pytest.main runs our tests directly in the notebook environment, providing
# fidelity for Spark and other configuration variables.
#
# A limitation of this approach is that changes to the test will be
# cache by Python's import caching mechanism.
#
# To iterate on tests during development, we restart the Python process 
# and thus clear the import cache to pick up changes.
dbutils.library.restartPython()

import pytest
import os
import sys

# Run all tests in the repository root.
notebook_path = dbutils.notebook.entry_point.getDbutils().notebook().getContext().notebookPath().get()
repo_root = os.path.dirname(os.path.dirname(notebook_path))
os.chdir(f'/Workspace/{repo_root}')
%pwd

# Skip writing pyc files on a readonly filesystem.
sys.dont_write_bytecode = True

retcode = pytest.main([".", "-p", "no:cacheprovider"])

# Fail the cell execution if we have any test failures.
assert retcode == 0, 'The pytest invocation failed. See the log above for details.'
