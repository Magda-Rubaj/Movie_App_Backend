from celery import shared_task
from .serializers import MovieSerializer
import requests

def save_to_db(data):
    for entry in data:
        serializer = MovieSerializer(data=entry)
        serializer.is_valid(raise_exception=True)
        serializer.save()

@shared_task
def call_api(url, *args, **kwargs):
    params = {"page":2}
    data = requests.get(url, params=params).json()["results"]
    data = [{
        "title": entry["title"], 
        "production_year": entry.get("release_date")[:4], 
        "description": entry["overview"],
        "added_by": 1
    } for entry in data if entry.get("release_date") is not None]
    save_to_db(data)
