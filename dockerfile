FROM python:3.7
# COPY requirements.txt /tmp
# RUN pip install -r requirements.txt
# COPY . /tmp/myapp
# RUN pip install /tmp/myapp
# CMD invoke run


ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt

CMD ["python", "reproject/app.py"]


