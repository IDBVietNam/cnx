FROM python:3.12

RUN apt update && apt install -y pkg-config gcc \
    default-libmysqlclient-dev pkg-config

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY . /code
WORKDIR /code

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]