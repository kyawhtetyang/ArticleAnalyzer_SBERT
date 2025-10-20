console.log("  v8 scripts loaded - blue theme active");

# v7/docker/Dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]

# v7/docker/docker-compose.yml
version: "3.9"
services:
  app:
    build: ..
    ports:
      - "5000:5000"
    volumes:
      - ../:/app
    environment:
      - FLASK_APP=app/routes.py
      - FLASK_ENV=development

