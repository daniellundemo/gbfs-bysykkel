# code challenge
I decided to use Pydantic + FastAPI as it comes with swagger OpenAPI schemas out of the box.

## How to start it locally
``# pip install -r requirements.txt`` \
``# uvicorn app.server:app``

## Or use the provided Dockerfile
``# docker build -t bysykkel:latest .`` \
``# docker run -d -p 8000:8000 bysykkel:latest``

Navigate to http://localhost:8000/docs to view the swagger API docs.
