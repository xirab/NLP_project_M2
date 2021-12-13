FROM python:3.10
WORKDIR /app
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=127.0.0.1
COPY * ./
RUN pip install -r requirements.txt 
EXPOSE 5000 
CMD ["flask", "run"]