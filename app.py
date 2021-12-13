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
    text = request.form['user_text'].lower()

    trained_model = load_model("./model/best_model.hdf5")

    with open('./model/tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)    

    encoded = tokenizer.texts_to_sequences([text])
    padded = pad_sequences(encoded, maxlen=200)

    # print(tokenizer.word_index)
    # print(text)
    # print(encoded)
    # print(padded)
    prediction = trained_model.predict(padded)
    # print(prediction)

    return render_template('index.html', score=(prediction[0]), text=text)

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)