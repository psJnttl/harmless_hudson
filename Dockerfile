FROM alpine:latest

# Install python and pip
RUN apk add --no-cache --update python3 py3-pip bash
ADD ./app/requirements.txt /tmp/requirements.txt

# Install dependencies
RUN pip3 install --no-cache-dir -q -r /tmp/requirements.txt

# Add code
ADD ./app/*.py /opt/webapp/
WORKDIR /opt/webapp

# Run the image as a non-root user
RUN adduser -D myuser
USER myuser

# Don't use overly popular port 8080.
EXPOSE 8090
ENTRYPOINT [ "gunicorn", "--bind", "0.0.0.0:8090", "wsgi" ]
