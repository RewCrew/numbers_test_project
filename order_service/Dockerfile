FROM python:3.7-slim

WORKDIR /app

ENV PATH=$PATH:/usr/bin

RUN pip install --upgrade pip

COPY ./setup.cfg .
COPY ./setup.py .

RUN pip install --no-cache-dir --upgrade -e '.[dev]'
COPY . ./order_service

COPY ./entrypoint_*.sh /usr/bin/

RUN chmod +x /usr/bin/entrypoint_*.sh

CMD [ "python", "order_service/run.py" ]