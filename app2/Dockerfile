FROM python:3.10-slim-bullseye

ENV PYTHONUNBUFFERED 1
ENV FLASK_APP=app2.py

RUN mkdir /app2
WORKDIR /app2
COPY . /app2

RUN pip install -r requirements.txt

CMD [ "python", "-m", "flask", "run", "--host=0.0.0.0", "--port=5001" ]