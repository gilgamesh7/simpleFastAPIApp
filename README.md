# simpleFastAPIApp

# Links
- [FastAPI Documentation](https://fastapi.tiangolo.com/tutorial/first-steps/)
- [VDI Link for app](http://127.0.0.1:8000)
- [Swagger Link for app](http://127.0.0.1:8000/docs)
- [Redoc Link for app](http://127.0.0.1:8000/redoc)
- [Openapi Link for app](http://127.0.0.1:8000/openapi.json)

# Installation
## Intial setup
- Create virtual environment : python3 -m venv venv --upgrade-deps
- pip install pipenv
- pipenv install fastapi
- pipenv install "uvicorn[standard]"
## Deploy in new venv
- pipenv install --system --deploy --ignore-pipfile

# Run
- uvicorn app:app --reload
