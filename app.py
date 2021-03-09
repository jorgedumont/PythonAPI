#!bin/python
from flask import Flask, jsonify, abort, request, make_response, url_for
from textblob import TextBlob
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/analisis2', methods=['POST'])
def textblob2():
    if not request.json or not 'frase' in request.json:
        abort(400)
    text = {
        "frase":request.json['frase']
    }
    analysis = TextBlob(request.json['frase']).translate(to='en')
    return jsonify({'Polaridad': analysis.polarity},{'Subjetividad': analysis.subjectivity})

if __name__ == '__main__':
    app.run(debug=True)

