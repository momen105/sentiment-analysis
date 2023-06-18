# sentiment-analysis
I used pre-trained sentiment model from here:
https://huggingface.co/StatsGary/setfit-ft-sentinent-eval
_____________________________________________________________________
## Input: 
The POST request payload should contain a JSON object with the following structure at /analyze/:
{
    "text": "Text to be analyzed"
}
## output: 
Return the sentiment analysis result as a JSON response with the following structure:
{
"sentiment": "positive/negative/neutral"
}



