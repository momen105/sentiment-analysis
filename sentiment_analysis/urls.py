from django.urls import path
from sentiment_analysis.views import sentiment_analysis

urlpatterns = [
    path("analyze/", sentiment_analysis, name="sentiment-analysis"),
]
