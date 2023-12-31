FROM python:3.8

# Set the working directory to /app
WORKDIR /app

COPY . /app

# Install needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8080 available to the world outside this container
EXPOSE 8080

ENV NAME World

CMD ["python", "app.py"]