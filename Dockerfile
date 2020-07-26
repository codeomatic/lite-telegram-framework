FROM python:3.8-slim

#RUN pip3 install twine
COPY requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt

ENV APP_HOME /app
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

COPY ./milligram ./milligram
COPY ./tests ./tests
COPY ./pypi.sh ./

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN rm -r /root/.cache

CMD exec py.test