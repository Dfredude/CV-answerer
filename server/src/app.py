from flask import Flask, render_template, url_for, request, redirect
from flask_cors import CORS, cross_origin
from transformers import pipeline
import os

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
# url_for('static', filename='style.css')

@cross_origin()
@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        user_question = request.form['question']
        ai_answer = getAnswer(user_question)
        return render_template('index.html', question=user_question, answer=ai_answer)
    
@app.route("/about", methods=['GET'])
def about():
    user_question = request.args.get('question')
    print(user_question)
    return getAnswer(user_question)
        

def getAnswer(user_question):
    # Load pipeline
    nlp = pipeline("question-answering", "timpal0l/mdeberta-v3-base-squad2")

    # read context from about.txt
    f = open("about.txt", "r")
    context = f.read()
    result = nlp(question=user_question, context=context)

    return result['answer'].capitalize() + "."
            

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))