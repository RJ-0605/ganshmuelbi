FROM ubuntu:18.04

ENV MYSQL_ROOT_PASSWORD='secret12'

RUN apt update -y
RUN apt install -y mysql-server

VOLUME /etc/mysql/conf.d
VOLUME /var/lib/mysql

RUN mkdir /data

COPY ./my.cnf /etc/mysql/conf.d/my.cnf
COPY ./billingdb.sql /data/billingdb.sql
COPY ./entry_point.sh /entry_point.sh

RUN chmod +x /entry_point.sh

CMD ["/entry_point.sh"]