# Steps to Create Two Python Virtual Environments and Replicate Packages

# 1. Create the First Virtual Environment
# Open your terminal or command prompt and execute the following commands:

# Step 1: Create the first virtual environment
# type: ignore
python -m venv env1 

# Step 2: Activate the virtual environment
# On Windows:
# env1\Scripts\activate
# On macOS/Linux:
# source env1/bin/activate

# Step 3: Install some packages in this environment
pip install numpy pandas requests

# Step 4: Save the list of installed packages
pip freeze > requirements.txt

# 2. Create the Second Virtual Environment
# Deactivate the first environment and create a new one.

# Step 1: Deactivate the first environment
deactivate

# Step 2: Create the second virtual environment
python -m venv env2

# Step 3: Activate the second virtual environment
# On Windows:
# env2\Scripts\activate
# On macOS/Linux:
# source env2/bin/activate

# Step 4: Install the same packages in this environment using the saved requirements file
pip install -r requirements.txt

# 3. Verify the Setup
# To confirm that the packages have been installed correctly in the second environment, run:
pip list
