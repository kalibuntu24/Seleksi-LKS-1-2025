FROM ubuntu:latest

# Install socat
RUN apt update && apt install -y socat

# Copy only necessary files
COPY . /

# Set the working directory
WORKDIR /

# Expose the port that socat listens on
EXPOSE 9970

# Run socat when the container starts
CMD ["socat", "TCP-LISTEN:9970,nodelay,reuseaddr,fork", "EXEC:\"stdbuf -i0 -o0 -e0 ./chall\""]
