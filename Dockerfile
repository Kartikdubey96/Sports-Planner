# 1. Use the official slim image
FROM python:3.11-slim

# 2. Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on

# 3. Create a non-privileged user for security
RUN groupadd -r appuser && useradd -r -g appuser appuser

# 4. Set working directory
WORKDIR /app

# 5. Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copy application code and change ownership to the new user
COPY --chown=appuser:appuser . .

# 7. Switch to the non-root user
USER appuser

# 8. Expose port
EXPOSE 8501

# 9. Add a Healthcheck (checks if the Streamlit port is responding)
HEALTHCHECK --interval=30s --timeout=3s \
  CMD curl -f http://localhost:8501/_stcore/health || exit 1

# 10. Start Streamlit
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0", "--server.headless=true"]