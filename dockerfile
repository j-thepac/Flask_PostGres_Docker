FROM python:3.10-slim
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install flask
RUN pip install psycopg2-binary
RUN pip install Flask-SQLAlchemy
COPY $PWD /home/apps
WORKDIR /home/apps
CMD python Test.py