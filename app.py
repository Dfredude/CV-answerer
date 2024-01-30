from flask import Flask, render_template, url_for, request, redirect
from transformers import pipeline

app = Flask(__name__)
# url_for('static', filename='style.css')

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        user_question = request.form['question']
        ai_answer = getAnswer(user_question)
        return render_template('index.html', question=user_question, answer=ai_answer)
    
def getAnswer(user_question):
    # Load pipeline
    nlp = pipeline("question-answering", "bert-large-uncased-whole-word-masking-finetuned-squad")

    # read context from about.txt
    f = open("about.txt", "r")
    context = f.read()
    result = nlp(question=user_question, context=context)

    return result['answer'].capitalize() + "."
