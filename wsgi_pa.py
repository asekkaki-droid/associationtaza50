import sys
import os

# This file is used by PythonAnywhere to start your Flask application.

# 1. Path to your project folder
# Replace 'YOUR_USERNAME' with your actual PythonAnywhere username
path = '/home/YOUR_USERNAME/assosiation-taza'
if path not in sys.path:
    sys.path.append(path)

# 2. Environment Variables
# You can set your secret key here or in the PythonAnywhere 'Web' tab
os.environ['SECRET_KEY'] = 'dev-secret-key-taza-association'
os.environ['DATABASE_URL'] = 'sqlite:////home/YOUR_USERNAME/assosiation-taza/instance/site.db'

# 3. Import the app initialization
from main import app as application

