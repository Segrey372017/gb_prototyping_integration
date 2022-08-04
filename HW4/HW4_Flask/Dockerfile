FROM python:3.8-slim-buster
LABEL maintainer = "ssmirnov"
WORKDIR /HW4
COPY requirements.txt requirements.txt
COPY hw4_server.py hw4_server.py
COPY road.jpg road.jpg
RUN pip install -r requirements.txt
RUN pip install opencv-python
RUN pip install opencv-python-headless
RUN mkdir server_config
COPY server_config/server_config.json server_config/server_config.json
CMD ("python3" "hw4_server.py")
EXPOSE 8889

