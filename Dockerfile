# Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY ./agent_app/requirements.txt .
RUN pip install --no-cache-dir --upgrade pip -r requirements.txt

# Copy the application code
COPY ./agent_app ./agent_app
COPY ./main.py .
COPY ./seed_db.py . 

# The command to run when the container starts.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]