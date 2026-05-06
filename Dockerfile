FROM python:3.11-slim

# ... (Previous ENV vars)
ENV PYTHONUNBUFFERED=1

# 1. Create the user AND their home directory specifically
RUN groupadd -r appuser && useradd -r -g appuser -m -d /home/appuser appuser

WORKDIR /app

# 2. Install dependencies as root (standard)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 3. Copy code and ensure appuser owns the /app directory
COPY --chown=appuser:appuser . .

# 4. Set an environment variable so Streamlit knows where to write config
ENV STREAMLIT_CONFIG_DIR=/home/appuser/.streamlit

# 5. Switch to the user
USER appuser

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0", "--server.headless=true"]