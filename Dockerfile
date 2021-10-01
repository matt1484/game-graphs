FROM python:3.9

RUN apt update -y

ADD requirements.txt .
RUN python -m pip install --no-cache-dir -r requirements.txt
ADD . .

ENV APP_HOST 0.0.0.0
ENV APP_PORT 80
ADD https://github.com/krallin/tini/releases/download/v0.19.0/tini /tini
RUN chmod +x /tini
ENTRYPOINT ["/tini", "-s", "-g",  "--", "python", "main.py"]