# From Base Image
FROM python:3.9-slim

# Work Dir
WORKDIR /app

# Copy from src/ to /dest
COPY . .

# Requirements
RUN pip install --no-cache-dir -r requirements.txt

# Command 
CMD ["python", "app.py" ]

