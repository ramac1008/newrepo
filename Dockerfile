FROM python:alpine3.16

RUN apk add musl-dev libpq-dev gcc

RUN python -m venv /opt/venv

ENV PATH- "/opt/venv/bin:$PATH"

COPY requirements.txt .

COPY . /app

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT [ "python" ]

CMD ["main.py"]