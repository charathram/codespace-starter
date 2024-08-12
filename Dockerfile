FROM python:3.10-slim

ENV PYTHONUNBUFFERED 1

# Install PostgreSQL client and other dependencies
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends postgresql-client \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container
WORKDIR /workspace/src

# Copy the requirements file
COPY src/requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY src/ .

# Copy the entrypoint script
COPY entrypoint.sh /workspace/

# Expose the port the app runs on
EXPOSE 8000

# Set the entrypoint
ENTRYPOINT ["/workspace/entrypoint.sh"]