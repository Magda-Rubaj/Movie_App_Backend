from celery import shared_task
from .serializers import MovieSerializer
import requests
import random
import math

def save_to_db(data):
    for entry in data:
        serializer = MovieSerializer(data=entry)
        serializer.is_valid(raise_exception=True)
        serializer.save()

def get_pages(url, limit):
    data = requests.get(url).json()
    total_results = data["total_results"]
    total_pages = data["total_pages"]
    per_page = math.ceil(total_results / total_pages)
    number_of_pages = math.ceil(limit/per_page)
    return random.sample((1, total_pages), number_of_pages)

def get_data(url, limit):
    pages = get_pages(url, limit)
    data = []
    for page in pages:
        params = {"page": page}
        data += requests.get(url, params=params).json()["results"]
    return data[:limit]

@shared_task
def call_api(url, limit, user, *args, **kwargs):
    data = get_data(url, limit)
    mapped_data = [{
        "title": entry["title"], 
        "production_year": entry.get("release_date")[:4], 
        "description": entry.get("overview"),
        "added_by": user
    } for entry in data if entry.get("release_date") is not None]
    save_to_db(mapped_data)
