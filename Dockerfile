FROM python:3.8.10
WORKDIR /CODE 
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0 
COPY * ./
RUN pip install -r requirements.txt 
