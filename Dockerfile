FROM python:3.10.2
WORKDIR /app
COPY . /app
RUN pip-install --no-cache django
RUN python manage.py makemigrations
RUN python manage.py migrate
EXPOSE 8000


ENV DJANGO_SETTINGS_MODULE=online_judge.settings
ENV PYTHONBUFFERED=1
CMD [ "python","manage.py","runserver","0.0.0.0:8000"]