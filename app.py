from flask import Flask, request, render_template
from flask_cors import CORS, cross_origin
import spacy
import os

nlp = spacy.load("en_core_web_md")

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
@cross_origin()
def hello():
  return "Hello World!"


@app.post('/score')
@cross_origin()
def handle_score():
    guess = request.get_json(force=True).get('guess')
    score = calculate_score(os.environ.get('ANSWER'), guess)
    return {
        "guess": guess,
        "score": score
    }



def calculate_score(answer: str, test: str):
    answer_nlp = nlp(answer.lower())
    test_nlp = nlp(test.lower())

    return answer_nlp.similarity(test_nlp) * 100


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)