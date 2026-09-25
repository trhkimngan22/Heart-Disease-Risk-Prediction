# Heart Disease Risk Prediction

A machine learning project for predicting heart disease risk, presented in a Jupyter Notebook.

## Before you start

- Install Python. Python 3.12 was used in the notebook.
- Install VS Code with the **Python** and **Jupyter** extensions.
- Connect to the internet. The setup script will download the required libraries for you.

## 1. Run `setup_env.py` to set up the environment and install libraries

Run this script once before using the notebook. You do not need to create a virtual environment or install each library manually.

1. Open the project folder in VS Code.
2. Open **Terminal -> New Terminal**.
3. Make sure the terminal is in the project folder containing `setup_env.py` and `requirements.txt`.
4. Run the command for your operating system below.

**macOS / Linux:**

```bash
python3 setup_env.py
```

On Windows, if Python 3.12 is installed, use:

```powershell
py -3.12 setup_env.py
```

The script automatically:

- Creates a separate Python environment in `.venv`.
- Installs all libraries listed in `requirements.txt` into that environment.
- Checks for dependency conflicts.
- Registers the notebook kernel **Python (Heart Disease Risk Prediction)**.

The first run may take a few minutes while the libraries download. Wait until you see `Setup complete`, then select the kernel using the steps below. You do not need to activate `.venv` to run the setup script.

If setup fails, check the error in the terminal, fix the issue, and run the same command again.

## 2. Select the kernel

1. Open `src/notebook.ipynb`.
2. Click **Select Kernel** in the top-right corner.
3. Choose **Python (Heart Disease Risk Prediction)**. You may need to select **Select Another Kernel…** first.

Under **Python Environments**, the environment may appear as `.venv` instead of the kernel name. Select the `.venv` inside this project.

The setup script does not change the kernel of an already open notebook.

### If the environment is missing

1. Open the Command Palette with **Cmd + Shift + P** on macOS or **Ctrl + Shift + P** on Windows/Linux.
2. Run **Python: Select Interpreter**.
3. Choose **Enter interpreter path…** and select the Python file inside this project:
   - macOS/Linux: `.venv/bin/python`
   - Windows: `.venv\Scripts\python.exe`
4. Return to the notebook and select this environment under **Select Kernel** → **Python Environments**.

If it still does not appear, run **Developer: Reload Window** from the Command Palette and try again.

## 3. Run the notebook

Run the cells from top to bottom. The notebook expects its working directory to be `src`, so it can load the dataset from:

```text
../data/heart_statlog_cleveland_hungary_final.csv
```

If you get a `FileNotFoundError`, check the working directory and make sure the CSV file is in the project's `data` folder.

> Note: This notebook was originally developed and run on Kaggle Notebooks. If you run it locally using the CPU of a personal computer or laptop, your results and execution time may differ from the saved Kaggle outputs because of differences in hardware, library versions, or numerical computations.

## Updating the environment

Run `setup_env.py` again after adding libraries to `requirements.txt`. Library versions are not currently pinned, so new installations may use different versions.

If you move the project to another location, recreate `.venv` and run the setup script again.
