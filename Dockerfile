FROM python:3.9-buster

# Set the working directory in the container
WORKDIR /app

# Copy the files into the container
COPY Crawler.py /app/
COPY DataIngestion.py /app/
COPY run.py /app/
COPY database_schema.sql /app/
COPY requirements.txt /app/

RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt


# Expose port
EXPOSE 3306

# Run the run.py script to generate data.json, then run the ingestion script
CMD ["python", "./run.py"]



