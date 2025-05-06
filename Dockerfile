# Base image with python
FROM python:3.10-slim
# Set the working directory inside the container
WORKDIR /app
# Copy all files from the project folder to the container directory 
COPY . /app
# Install the required python packages
RUN pip install --no-cache-dir -r requirements.txt
# Ports needed for fastapi(8000) and streamlit(8501)
EXPOSE 8000
EXPOSE 8501
# 6. Command to run both FastAPI and Streamlit
CMD uvicorn main:app --host 0.0.0.0 --port 8000 & \
    streamlit run my_app.py --server.port 8501