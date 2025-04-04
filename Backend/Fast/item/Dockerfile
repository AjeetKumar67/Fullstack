FROM python:3.10-slim

WORKDIR /item

# Copy the requirements file
COPY requirements.txt /item/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /item/

# Set the PYTHONPATH environment variable
ENV PYTHONPATH=/item

# Command to run the service
CMD ["python", "-m", "main"]
