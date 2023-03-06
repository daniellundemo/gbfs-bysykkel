FROM python:3.9-slim
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app ./app
EXPOSE 8000
CMD ["uvicorn", "app.server:app"]