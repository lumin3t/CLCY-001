FROM node:18-alpine

# Install Python, pip, and required dependencies
RUN apk add --no-cache python3 py3-pip && \
    pip3 install watchdog requests

WORKDIR /docker1
COPY . .

# Make sure the Python script is executable (if needed)
RUN chmod +x monitor_and_upload.py

# Run both Node.js and Python scripts (using a shell script)
CMD ["sh", "-c", "node hello.js & python3 monitor_and_upload.py"]