# Using official python image
FROM python:3.8

# Setting the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container at /app
COPY requirements.txt /app/

# Install the Python dependencies from requirements.txt
RUN pip install -r requirements.txt

# Install uvicorn with standard dependencies
RUN pip install uvicorn[standard]

# Copy the rest of your application code into the container
COPY . /app/

# Exposing the port
EXPOSE 8000

# Run command
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
