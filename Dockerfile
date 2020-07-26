FROM python:3.8-slim

RUN pip install twine
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

ENV APP_HOME /app
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

COPY ./ ./

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN rm -r /root/.cache

CMD exec py.test