FROM python:3.10.6

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN python -m spacy download en_core_web_lg

COPY . .

CMD ["python", "app.py"]