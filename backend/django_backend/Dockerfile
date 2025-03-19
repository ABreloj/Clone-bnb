FROM python:3.12.2-slim-bullseye

WORKDIR /usr/src/django_backend

ENV PYTHONDONTWRITTEBYCODE=1
ENV PYTHONUNBUFFERED=1


RUN pip install --upgrade pip
COPY ./requeriments.txt .
RUN pip install -r requeriments.txt

COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/django_backend/entrypoint.sh
RUN chmod +x /usr/src/django_backend/entrypoint.sh

COPY . .

ENTRYPOINT ["/usr/src/django_backend/entrypoint.sh"]