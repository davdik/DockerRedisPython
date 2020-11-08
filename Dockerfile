FROM python:3.8-alpine
ADD . /code
WORKDIR /code
RUN pip install flask
RUN pip install redis
RUN chmod 755 score.py
CMD ["python3.8", "score.py"]
