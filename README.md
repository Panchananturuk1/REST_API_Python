REST API CRUD Operations with Python-Flask and MySQL (Version-1)
For video tutorial SUBSCRIBE to, TechFryDay

Download and setup
Step-1: Creating & activating venv Windows:

  python -m venv venv
  ./venv/Scripts/activate
Linux:

  python -m venv venv
  source venv/bin/activate
Step-2: Installing Dependencies

  pip install -r requirements.txt
Step-3: Running application Windows:

  > $env:PYTHONDONTWRITEBYTECODE=1;$env:FLASK_APP="app";$env:FLASK_ENV = "development"
  > flask run
Linux:

  > export PYTHONDONTWRITEBYTECODE=1 FLASK_APP="app" FLASK_ENV="development"
  > flask run
Installing Dependencies
  pip install -r requirements.txt
Common Issues
Creating pycache files Windows-powershell-Solution:
  $env:PYTHONDONTWRITEBYTECODE=1
Linux:

export PYTHONDONTWRITEBYTECODE=1
Common Errors
While activating venv this error occures in Windows:

    + CategoryInfo          : SecurityError: (:) [], PSSecurityException
    + FullyQualifiedErrorId : UnauthorizedAccess
Solution: Execute this command and retry activating venv.

  Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
