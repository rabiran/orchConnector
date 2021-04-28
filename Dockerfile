FROM python:3.6

#-alpine3.13

WORKDIR /usr/src/app

COPY . .

RUN apt-get update
RUN apt-get install -y gcc python-dev libkrb5-dev

#RUN apk update
#RUN apk add --update libkrb5-dev
# RUN echo "http://dl-4.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories
# RUN apk add --no-cache libkrb5-dev

#RUN apk update && apk add --no-cache python3-dev \
#                   gcc


RUN python3 -m pip install -r requirements.txt


EXPOSE 5000
CMD [ "python3", "index.py" ]