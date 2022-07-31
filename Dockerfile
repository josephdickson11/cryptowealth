FROM python:3.9

WORKDIR /bolddapi

COPY . /bolddapi/

RUN pip install --no-cache-dir --upgrade -r /bolddapi/requirements/commonreq.txt
RUN pip install -r /bolddapi/requirements/env_sql.txt

CMD [ "uvicorn", "main:app", "--reload", "--host","0.0.0.0", "--port", "80"]
