FROM python:3.10-slim-bullseye

ENV PYTHONUNBUFFERED 1
ENV FLASK_APP=app1.py

RUN mkdir /app1
WORKDIR /app1
COPY . /app1

RUN pip install -r requirements.txt

CMD [ "python", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000" ]