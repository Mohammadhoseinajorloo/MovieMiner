# Install python
FROM python:3.12


# Parent directory for project
WORKDIR /app


# Copy requirements file and install dependency
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


# Install mysql-client and copy all file in app directory
RUN apt-get update && apt-get install -y default-mysql-client vim
COPY . .


# Run python app in container
CMD ["python3", "main.py"]
