FROM python:3

RUN mkdir -p /usr/src/app && \
    apt-get update && \
    apt-get -y install whois && \
    rm -rf rm -rf /var/lib/apt/lists/*
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . /usr/src/app/

CMD python main.py
EXPOSE 8080
