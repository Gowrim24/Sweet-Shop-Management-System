import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.path.join(BASE_DIR, 'database.db')

SECRET_KEY = "your-secret-key"  # Replace with your own secret in production

SQLALCHEMY_DATABASE_URI = f"sqlite:///{DATABASE}"
SQLALCHEMY_TRACK_MODIFICATIONS = False
