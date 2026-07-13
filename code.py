from transformers import pipeline

# Load a pre-trained sentiment analysis pipeline
classifier = pipeline("sentiment-analysis")

# Example texts
texts = [
    "I love using transformers! It's so easy.",
    "This movie was terrible and boring."
]

# Run inference
results = classifier(texts)

# Print results
for text, result in zip(texts, results):
    print(f"Text: {text}")
    print(f"Label: {result['label']}, Score: {result['score']:.4f}\n")