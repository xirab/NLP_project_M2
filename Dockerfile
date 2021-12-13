FROM python:3.10
WORKDIR /CODE 
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0 
COPY * ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt 
EXPOSE 5000 
CMD ["flask", "run"]
