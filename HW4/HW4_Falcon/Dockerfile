FROM python:3.8-slim-buster
LABEL maintainer = "ssmirnov"
WORKDIR /HW4
COPY requirements.txt requirements.txt
COPY __init__.py __init__.py
COPY hw4_server.py hw4_server.py
COPY road.jpg road.jpg
RUN pip install -r requirements.txt
RUN pip install opencv-python
RUN pip install gunicorn
RUN mkdir server_config
COPY server_config/config.json server_config/config.json
CMD ("gunicorn" "--reload" "hw4_server")
EXPOSE 8000

