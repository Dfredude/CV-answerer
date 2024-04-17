FROM python:3.11.7

WORKDIR /app

COPY src/ ./


RUN pip install --no-cache-dir -r requirements.txt

ENV PORT 8080

CMD exec gunicorn --bind :$PORT --workers 2 --threads 8 app:app

# CMD [ "flask", "run" ]