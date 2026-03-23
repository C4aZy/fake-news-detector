import pickle

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

def predict_news(text):
    text_vec = vectorizer.transform([text])
    prediction = model.predict(text_vec)[0]
    
    if prediction == 1:
        return "Real News"
    else:
        return "Fake News"