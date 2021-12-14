# FROM python:3.8
# WORKDIR /app
# ENV FLASK_APP=app.py
# ENV FLASK_RUN_HOST=127.0.0.1
# COPY * ./
# RUN pip install -r requirements.txt 
# EXPOSE 5000 
# CMD ["flask", "run"]


# STEP 1: Install base image. Optimized for Python.
FROM python:3.7-slim-buster

# Step 2: Add requirements.txt file 
COPY requirements.txt /requirements.txt

# Step 3:  Install required pyhton dependencies from requirements file
RUN pip install -r requirements.txt

# Step 4: Copy source code in the current directory to the container
ADD . /app

# Step 5: Set working directory to previously added app directory
WORKDIR /app

# Step 6: Expose the port Flask is running on
EXPOSE 5000

# Step 9: Run Flask
CMD ["flask", "run", "--host", "127.0.0.1", "--port=5000"]
