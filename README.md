# Text Normalization and Tokenization
This tool simplifies text preprocessing using Natural Language Processing (NLP) techniques. It helps standardize and break down text for easier analysis.

## Features

- **Text Normalization:** Convert text to lowercase and remove punctuation for consistency.
- **Remove Stopwords:** Filter out common words (e.g., "and", "the", "is") to focus on meaningful content.
- **Tokenize into Words:** Split text into individual words for detailed analysis.
- **Tokenize into Sentences:** Divide text into sentences to understand its structure.
- **Tokenize into Paragraphs:** Separate text into paragraphs for deeper document analysis.

## Usage
1. **Text Normalization:** Converts text to lowercase and removes punctuation marks.
2. **Remove Stopwords:** Filters out common words to highlight significant content.
3. **Tokenize into Words**
     - **Input:** "Tokenization is an important step."
     - **Output:** ["Tokenization", "is", "an", "important", "step", "."]
4. **Tokenize into Sentences**
     - **Input:** "Tokenization is important. It breaks down text."
     - **Output:** ["Tokenization is important.", "It breaks down text."]
5. **Tokenize into Paragraphs**
     - **Input:** "Tokenization is important. It involves breaking down text into units.\n\nAfter tokenization, further analysis is possible."
     - **Output:** ["Tokenization is important. It involves breaking down text into units.", "After tokenization, further analysis is possible."]

## Required Modules
- **NLTK:** A toolkit for NLP tasks like tokenization and stopwords removal.<br>
```pip install nltk```<br>
- **Download resources:**
  <br>
```nltk.download('stopwords')```
```nltk.download('punkt')```
- **Flask:** A web framework for creating Python web applications.<br>
```pip install Flask```

## Python version 3.10 - 3.11
Install modules by<br>
```pip install -r requirements.txt```
<br>

To run the application <br>
```python app.py```

## Web Page
![image](https://github.com/hariharasudan3/Text-Normalization-NLP/assets/145860861/8d6304f8-5cb7-4c1a-8e29-83fabd632a5f)

## Text Normalization
![image](https://github.com/hariharasudan3/Text-Normalization-NLP/assets/145860861/edac3933-f14f-4203-8a82-128df0bab869)

## Remove Stopwords
![image](https://github.com/hariharasudan3/Text-Normalization-NLP/assets/145860861/da1c6d1c-960a-4aec-a377-b7cd02b8b59d)

## Tokenize into Words
![image](https://github.com/hariharasudan3/Text-Normalization-NLP/assets/145860861/4ed0480b-0358-494f-9405-5106791a43bc)

## Tokenize into Sentences
![image](https://github.com/hariharasudan3/Text-Normalization-NLP/assets/145860861/b5367a92-d59b-4796-8024-cb69c9e9a2a7)

## Tokenize into Paragraphs
![image](https://github.com/hariharasudan3/Text-Normalization-NLP/assets/145860861/e36362d9-01f0-4023-92a1-f8284444ba82)


## 📃 License

This project follows the [MIT License](/LICENSE).
