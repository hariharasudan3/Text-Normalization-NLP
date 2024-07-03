from flask import Flask, render_template, request
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

app = Flask(__name__)

nltk.download('punkt')
nltk.download('stopwords')

def normalize_text(text):
    # Lowercase the text
    text = text.lower()
    
    # Normalize text based on chosen option
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    
    return text

def remove_stopwords(text):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text)
    words = [word for word in words if word.lower() not in stop_words]
    text = ' '.join(words)
    return text

def tokenize_text(text, option):
    if option == "tokenize_words":
        tokens = word_tokenize(text)
        result = {"Tokenized Words": tokens}
    elif option == "tokenize_sentences":
        tokens = sent_tokenize(text)
        result = {"Tokenized Sentences": tokens}
    elif option == "tokenize_paragraphs":
        paragraphs = text.split('\n\n')  # Assuming paragraphs are separated by double newline
        result = {"Tokenized Paragraphs": paragraphs}
    else:
        result = {"error": "Invalid option"}

    return result

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    input_text = request.form["input_text"]
    option = request.form["option"]

    if option == "normalize":
        processed_text = normalize_text(input_text)
    elif option == "stopwords":
        processed_text = remove_stopwords(input_text)
    else:
        tokenized_result = tokenize_text(input_text, option)
        return render_template("result.html", tokenized_result=tokenized_result)

    return render_template("result.html", processed_text=processed_text)

if __name__ == "__main__":
    app.run(debug=True)
