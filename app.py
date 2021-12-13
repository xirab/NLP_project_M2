from flask import Flask, request, render_template
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
import nltk

nltk.download('stopwords')

set(stopwords.words('english'))
app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    stop_words = stopwords.words('english')
    sentence = request.form['user_text']
    text = sentence.lower()

    processed_text = ' '.join([word for word in text.split() if word not in stop_words])

    sa = SentimentIntensityAnalyzer()
    dd = sa.polarity_scores(text=processed_text)
    #compound = round((1 + dd['compound'])/2, 2)
    neg = round(dd['neg']*100)
    neu = round(dd['neu']*100)
    pos = round(dd['pos']*100)
    sent = max(dd, key=dd.get)

    return render_template('index.html', score=[neg, neu, pos], text=sentence, sentiment=sent)

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)