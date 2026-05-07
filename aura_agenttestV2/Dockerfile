FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
RUN playwright install chromium
EXPOSE 8501
CMD ["streamlit", "run", "ai_core/web_app.py", "--server.address=0.0.0.0"]