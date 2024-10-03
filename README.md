File & Folder Management System
This is a simple File & Folder Management System API built with FastAPI and MySQL. The system allows you to create folders and files, organize them hierarchically (parent-child relationships), and automatically delete related subfolders and files when a folder is removed.

Features
Create folders and files.
Nest folders and organize files within them.
Automatically delete all files and subfolders when a parent folder is deleted.
Separate logic for folders and files for better code organization and reusability.
Why FastAPI and MySQL?
FastAPI: It's fast, modern, and comes with automatic interactive API docs. Perfect for quickly building APIs with Python.
MySQL: A robust and widely-used relational database. Ideal for managing structured data like folders and files, and scalable for production environments.
Project Setup
Clone the repo:

bash
Copy code
git clone https://github.com/your-username/folder-file-management.git
cd folder-file-management
Create a virtual environment:

bash
Copy code
python -m venv env
source env/bin/activate  # Linux/macOS
# or
env\Scripts\activate  # Windows
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Update MySQL connection settings in database.py:

python
Copy code
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://username:password@localhost/db_name"
Create the database tables:

bash
Copy code
python -c "from app.database import Base, engine; Base.metadata.create_all(bind=engine)"
Run the app:

bash
Copy code
uvicorn app.main:app --reload
The API will be accessible at http://127.0.0.1:8000.

API Endpoints
Create Folder: POST /folders/
Create File: POST /files/
Delete Folder: DELETE /folders/{folder_id} (also deletes subfolders and files)
Explore the API docs at /docs for detailed usage.

Future Improvements
Add authentication.
Use pagination for listing files/folders.
