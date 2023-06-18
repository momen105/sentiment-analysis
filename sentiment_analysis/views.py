from rest_framework.decorators import api_view
from rest_framework.response import Response
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_name = "StatsGary/setfit-ft-sentinent-eval"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

@api_view(['POST'])
def sentiment_analysis(request):
    text = request.data.get('text')

    if not text:
        return Response({'error': 'No text provided'}, status=400)

    # Tokenize the input text
    encoding = tokenizer.encode_plus(text, return_tensors="pt", padding=True, truncation=True)
    input_ids = encoding["input_ids"]
    attention_mask = encoding["attention_mask"]

    # Perform sentiment analysis using the loaded model
    with torch.no_grad():
        outputs = model(input_ids, attention_mask=attention_mask)

    predicted_sentiment = torch.argmax(outputs.logits, dim=1).item()

    # Map the sentiment prediction to human-readable labels
    sentiment_mapping = {0: "negative", 1: "neutral", 2: "positive"}
    result = {"sentiment": sentiment_mapping[predicted_sentiment]}

    return Response(result, status=200)
