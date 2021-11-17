# pull official base image
FROM python:3.9.6-alpine

COPY ./requirements.txt /app/requirements.txt
# set work directory
WORKDIR /app
COPY . /app
RUN apk add --no-cache gcc musl-dev build-base postgresql-dev
RUN pip install -r requirements.txt
#RUN python ./build_database.py
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

CMD [ "python", "./server.py" ]
