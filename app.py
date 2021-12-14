from flask import Flask, request, render_template
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    # get the text from the form
    sentence = request.form['user_text'].lower()

    # loading the best model pretrained and saved in the model directory
    trained_model = load_model("./model/best_model.hdf5")

    # loading the tokenizer from the model directory to preprocessed the user's text before predicting the sentiment
    with open('./model/tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)    

    # we encode and preprocessed the text 
    encoded = tokenizer.texts_to_sequences([sentence])
    padded = pad_sequences(encoded, maxlen=200)

    # print(tokenizer.word_index)
    # print(text)
    # print(encoded)
    # print(padded)

    # and then predict the sentiment
    # the output is the percentage of each sentiment in the text. So we have 3 output saved in an array
    # the overall sentiment will be the sentiment with the bigger percentage
    prediction = trained_model.predict(padded)
    # print(prediction)

    neg = round(prediction[0][2]*100)
    neu = round(prediction[0][0]*100)
    pos = round(prediction[0][1]*100)

    dic = {
        'neg' : neg,
        'neu' : neu,
        'pos' : pos
    }

    sent = max(dic, key=dic.get)
    
    return render_template('index.html', score=[neg, neu, pos], text=sentence, sentiment=sent)

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)