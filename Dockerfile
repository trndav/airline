FROM python:3
COPY . C:/Projects/airline/
WORKDIR C:/Projects/airline/
RUN pip install --upgrade pip
RUN pip freeze > requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
ENV DJANGO_SETTINGS_MODULE=airline.settings
# RUN pip install -r requirements.txt
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# docker-compose up, build
# docker build -t dockerbuildfile2 .