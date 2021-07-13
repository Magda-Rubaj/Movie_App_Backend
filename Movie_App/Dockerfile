FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /movies
COPY requirements.txt /movies/
RUN pip install -r requirements.txt
COPY . /movies/