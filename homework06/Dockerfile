FROM python:3.9

RUN mkdir /data
WORKDIR /data
COPY requirements.txt /data/requirements.txt
RUN pip install -r /data/requirements.txt
COPY . /data

ENTRYPOINT ["python"]
CMD ["app.py"]
