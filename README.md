# 📰 Fake News Detection System

## 📌 Overview
This project is a Machine Learning-based system that classifies news articles as Real or Fake using Natural Language Processing (NLP) techniques. It analyzes textual content and predicts authenticity using a trained model.

## 🎯 Problem Statement
With the rapid spread of misinformation online, detecting fake news has become crucial. This project builds a classification model that identifies whether a news article is genuine or misleading.

## 🛠️ Tech Stack
Python, Pandas, NumPy, Scikit-learn, NLP (TF-IDF Vectorization)

## ⚙️ Project Structure
fake-news-detector/
│── main.py
│── model.py
│── train.py
│── requirements.txt
│── README.md
│── data/   (you must create this folder)

## 🚀 Setup and Execution Guide

### 1. Prerequisites
Ensure you have Python 3.8 or higher and pip installed.

Check:
python --version  
pip --version  

---

### 2. Clone the Repository
git clone https://github.com/your-username/fake-news-detector  
cd fake-news-detector  

---

### 3. Create Virtual Environment (Recommended)
python -m venv venv  

Activate:

Windows:
venv\Scripts\activate  

macOS/Linux:
source venv/bin/activate  

---

### 4. Install Dependencies
pip install -r requirements.txt  

---

### 5. Dataset Setup (IMPORTANT)

Since dataset files are large, they are not included in this repository.

Follow these steps:

1. Go to the dataset link:  
https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset  

2. Download the dataset as a ZIP file  

3. Extract (unzip) the downloaded file  

4. You will get:
   - Fake.csv  
   - True.csv  

5. Create a folder named `data` inside the project directory  

6. Place both files inside:
data/
│── Fake.csv  
│── True.csv  

---

### 6. Train the Model
python train.py  

This step will:
- Load dataset  
- Train the model  
- Save model.pkl and vectorizer.pkl  

---

### 7. Run the Application
python main.py  

---

### 8. Provide Input
Enter any news text when prompted.

Example:
Enter news text:
Government announces new economic reforms...

Output:
Prediction: Real News  

---

## 💡 How It Works
The dataset is labeled (Real = 1, Fake = 0). Text data is converted into numerical form using TF-IDF vectorization. A Logistic Regression model is trained and used to predict whether input news is real or fake.

---

## 📊 Model Performance
The model is evaluated using accuracy on test data (printed in train.py).

---

## 🔍 Features
- NLP-based fake news detection  
- TF-IDF vectorization  
- Logistic Regression classifier  
- Command-line interface (CLI)  
- Easy to set up and run  

---

## ⚠️ Limitations
- Depends on dataset quality  
- May not generalize to all news sources  
- Detects patterns, not factual truth  

---

## 🚀 Future Improvements
- Add deep learning models (LSTM, BERT)  
- Build a web interface (Streamlit)  
- Improve preprocessing  
- Use larger datasets  

---

## 👨‍💻 Author
Abhijeet Mukherjee
25BAI10476

---

## 📜 License
This project is for educational purposes only.
