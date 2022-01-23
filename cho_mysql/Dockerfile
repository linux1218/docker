FROM mysql:5.7

ENV MYSQL_ROOT_PASSWORD password
ENV MYSQL_USER cho
ENV MYSQL_PASSWORD Qwer1234!
ENV MYSQL_DATABASE cho_db

COPY ["init_db.sh", "/"]
COPY ["cre_tb.sql", "/"]
# CMD ["/bin/bash", "mysql -u cho -pQwer1234! cho_db < /cre_tb.sql"]

# docker build --tag mysql_v1 .
# docker run -it -d --name mysql_1 mysql_v1
# docker exec -it mysql_1 /bin/bash
# docker logs mysql_1

# docker stop mysql_1
# docker rm mysql_1
# docker rmi mysql_v1