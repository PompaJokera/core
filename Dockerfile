FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
RUN apt-get -qy update
RUN apt install -y mysql-server*
RUN pip install peewee pymysql sqlalchemy sqlalchemy_utils requests
RUN echo "172.19.0.2       db" >> /etc/hosts
COPY . /app/