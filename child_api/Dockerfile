FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY child_api.py .

CMD ["uvicorn", "child_api:app", "--host", "0.0.0.0", "--port", "8001"]