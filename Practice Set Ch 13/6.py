# Steps to Create a Virtual Environment Based on System Interpreter's Packages

# 1. Run pip freeze for the System Interpreter
# Open your terminal or command prompt and execute the following command:
# type: ignore
pip freeze > system_packages.txt

# This command saves the list of all packages installed in the system interpreter to a file named "system_packages.txt".

# 2. Create a Virtual Environment
# Step 1: Create a new virtual environment
python -m venv new_env

# Step 2: Activate the virtual environment
# On Windows:
# new_env\Scripts\activate
# On macOS/Linux:
# source new_env/bin/activate

# 3. Install the Same Packages in the Virtual Environment
pip install -r system_packages.txt

# 4. Verify the Setup
# To confirm that the packages have been installed correctly in the virtual environment, run:
pip list
