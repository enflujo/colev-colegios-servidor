FROM python:3.8

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . /code/api

ENV PYTHONPATH /code/api

CMD ["uvicorn", "api.server:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]
