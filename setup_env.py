"""Create the project environment, install dependencies, and register its kernel."""

from pathlib import Path
import os
import subprocess
import sys
import venv


ROOT = Path(__file__).resolve().parent
ENV_DIR = ROOT / ".venv"
KERNEL_NAME = "heart-disease-risk-prediction"
KERNEL_LABEL = "Python (Heart Disease Risk Prediction)"


def main():
    python = ENV_DIR / ("Scripts/python.exe" if os.name == "nt" else "bin/python")
    if not python.exists():
        print(f"Creating virtual environment: {ENV_DIR}", flush=True)
        venv.EnvBuilder(with_pip=True).create(ENV_DIR)

    commands = [
        [str(python), "-m", "pip", "install", "--upgrade", "pip"],
        [str(python), "-m", "pip", "install", "-r", str(ROOT / "requirements.txt")],
        [str(python), "-m", "pip", "check"],
        [str(python), "-m", "ipykernel", "install", "--user",
         "--name", KERNEL_NAME, "--display-name", KERNEL_LABEL],
    ]
    for command in commands:
        subprocess.run(command, cwd=ROOT, check=True)

    print(f"\nSetup complete. Open src/notebook.ipynb and select: {KERNEL_LABEL}")
    print(f"In VS Code, you can also select the Python interpreter: {python}")


if __name__ == "__main__":
    try:
        main()
    except (subprocess.CalledProcessError, OSError) as error:
        print(f"\nSetup failed: {error}\nFix the error above and rerun this script.", file=sys.stderr)
        sys.exit(1)
