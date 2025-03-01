FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY mother_api.py .

CMD ["uvicorn", "mother_api:app", "--host", "0.0.0.0", "--port", "8000"]