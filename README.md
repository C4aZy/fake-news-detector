# 📰 Fake News Detection System

## 📌 Overview
This project is a Machine Learning-based system that classifies news articles as Real or Fake using Natural Language Processing (NLP) techniques. It analyzes textual content and predicts authenticity using a trained model.

## 🎯 Problem Statement
With the rapid spread of misinformation online, detecting fake news has become crucial. This project builds a classification model that identifies whether a news article is genuine or misleading.

## 🛠️ Tech Stack
Python, Pandas, NumPy, Scikit-learn, NLP (TF-IDF Vectorization)

## 📂 Dataset
The dataset contains real and fake news articles:
- Fake.csv
- True.csv
Each file includes title and text content.

## ⚙️ Project Structure
fake-news-detector/
│── main.py
│── model.py
│── train.py
│── requirements.txt
│── README.md
│── data/
    │── Fake.csv
    │── True.csv

## 🚀 Setup and Execution Guide

### 1. Prerequisites
Ensure you have Python 3.8 or higher and pip installed.
Check using:
python --version
pip --version

### 2. Clone the Repository
git clone https://github.com/your-username/fake-news-detector
cd fake-news-detector

### 3. Create Virtual Environment (Recommended)
python -m venv venv

Activate:
Windows:
venv\Scripts\activate
macOS/Linux:
source venv/bin/activate

### 4. Install Dependencies
pip install -r requirements.txt

### 5. Dataset Setup
Download Fake.csv and True.csv files.
Create a folder named data in the project root and place files inside:
data/
│── Fake.csv
│── True.csv

### 6. Train the Model
python train.py
This will process the dataset, train the model, and save model.pkl and vectorizer.pkl.

### 7. Run the Application
python main.py

### 8. Provide Input
Enter any news text when prompted.
Example:
Enter news text:
Government announces new economic reforms...

Output:
Prediction: Real News

## 💡 How It Works
The dataset is loaded and labeled (Real = 1, Fake = 0). Text data is converted into numerical form using TF-IDF vectorization. A Logistic Regression model is trained on this data. The trained model predicts whether new input news is real or fake.

## 📊 Model Performance
The model is evaluated using accuracy on test data. Accuracy can be printed inside train.py.

## 🔍 Features
- NLP-based fake news detection  
- TF-IDF vectorization  
- Logistic Regression classifier  
- Command-line interface (CLI)  
- Easy to set up and run  

## ⚠️ Limitations
- Depends on dataset quality  
- May not generalize to all news sources  
- Detects patterns, not factual truth  

## 🚀 Future Improvements
- Add deep learning models (LSTM, BERT)  
- Build a web interface (Streamlit)  
- Improve preprocessing  
- Use larger datasets  

## 👨‍💻 Author
Your Name

## 📜 License
This project is for educational purposes only.