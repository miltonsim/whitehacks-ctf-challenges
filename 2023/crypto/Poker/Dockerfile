FROM python:3.8-slim-bullseye

RUN apt-get update
RUN apt-get install -y xinetd 
RUN useradd -m user

WORKDIR /home/user
COPY app.py .
COPY service /etc/xinetd.d/$userservice
COPY requirements.txt .
COPY flag.txt .

RUN pip3 install -r requirements.txt

RUN chown -R root:root .; \
    chmod 555 ./app.py;

EXPOSE 1337

USER user

ENTRYPOINT ["/usr/sbin/xinetd", "-dontfork"]