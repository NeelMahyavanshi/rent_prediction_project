import os

def create_project_structure(base_dir):
    # Define the folder structure
    folders = [
        f"{base_dir}/backend/app/routes",
        f"{base_dir}/backend/app/schemas",
        f"{base_dir}/backend/app/utils",
        f"{base_dir}/backend/app/models",
        f"{base_dir}/backend/data/raw",
        f"{base_dir}/backend/data/processed",
        f"{base_dir}/backend/logs",
        f"{base_dir}/backend/tests",
        f"{base_dir}/frontend/static/css",
        f"{base_dir}/frontend/static/js",
        f"{base_dir}/frontend/templates"
    ]

    # Define the files to create
    files = [
        f"{base_dir}/backend/app/__init__.py",
        f"{base_dir}/backend/app/main.py",
        f"{base_dir}/backend/app/routes/__init__.py",
        f"{base_dir}/backend/app/routes/predict.py",
        f"{base_dir}/backend/app/routes/health.py",
        f"{base_dir}/backend/app/schemas/__init__.py",
        f"{base_dir}/backend/app/schemas/request.py",
        f"{base_dir}/backend/app/utils/__init__.py",
        f"{base_dir}/backend/app/utils/preprocess.py",
        f"{base_dir}/backend/app/utils/logger.py",
        f"{base_dir}/backend/app/models/rent_model.pkl",
        f"{base_dir}/backend/data/README.md",
        f"{base_dir}/backend/requirements.txt",
        f"{base_dir}/backend/.env",
        f"{base_dir}/backend/Dockerfile",
        f"{base_dir}/backend/logs/app.log",
        f"{base_dir}/frontend/app.py",
        f"{base_dir}/frontend/forms.py",
        f"{base_dir}/frontend/templates/base.html",
        f"{base_dir}/frontend/templates/index.html",
        f"{base_dir}/frontend/templates/results.html",
        f"{base_dir}/frontend/templates/error.html",
        f"{base_dir}/frontend/requirements.txt",
        f"{base_dir}/frontend/.env",
        f"{base_dir}/frontend/Dockerfile",
        f"{base_dir}/docker-compose.yml",
        f"{base_dir}/README.md"
    ]

    # Create folders
    for folder in folders:
        os.makedirs(folder, exist_ok=True)

    # Create files
    for file in files:
        with open(file, "w") as f:
            pass

    # Add a default logging configuration file
    logging_config = '''import logging
import os

def setup_logger(name, log_file, level=logging.INFO):
    """Function to setup a logger"""
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

# Example usage
if not os.path.exists("logs"):
    os.makedirs("logs")

app_logger = setup_logger("app_logger", "logs/app.log")
app_logger.info("Logger initialized")
'''

    with open(f"{base_dir}/backend/app/utils/logger.py", "w") as f:
        f.write(logging_config)

if __name__ == "__main__":
    base_directory = "rent_prediction_project"  # Change as needed
    create_project_structure(base_directory)
    print(f"Project structure created under {base_directory}!")
