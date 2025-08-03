# Use official slim Python image as base (lightweight and fast)
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy all project files into the container
COPY . /app

# Install required Python packages from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set the default command to run the email scraper script
# You can change this to "hunter.py" if needed
CMD ["python", "scraper.py"]
