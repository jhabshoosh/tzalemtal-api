from flask import Flask, request, render_template
from flask_cors import CORS, cross_origin
import spacy
import os
import requests

nlp = spacy.load("en_core_web_md")

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

ANSWER_URL = 'https://github.com/jhabshoosh/tzalemtal-assets/blob/master/answer.json?raw=true'


@app.post('/score')
@cross_origin()
def handle_score():
  guess = request.get_json(force=True).get('guess')
  score = calculate_score(test=guess)
  return {
      "guess": guess,
      "score": score
  }


def calculate_score(test: str):
  answer_nlp = nlp(answer)
  test_nlp = nlp(test.lower())

  return answer_nlp.similarity(test_nlp) * 100


def get_answer():
  r = requests.get(url=ANSWER_URL)
  data = r.json()
  return data.get('answer')


if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  answer = get_answer()
  app.run(debug=True, host='0.0.0.0', port=port)