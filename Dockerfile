FROM python:3.10.6

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

RUN python -m spacy download en_core_web_lg

CMD ["python", "app.py"]