FROM python:3.11-bullseye


# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# install dependencies
WORKDIR /app/neurocage
COPY ./src/app/requirements.txt /app/neurocage
RUN pip install -r requirements.txt

# copy project
COPY ./ /app/neurocage