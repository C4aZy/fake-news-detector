from model import predict_news

def main():
    print("=== Fake News Detector ===")
    text = input("Enter news text:\n")
    
    result = predict_news(text)
    print("\nPrediction:", result)

if __name__ == "__main__":
    main()