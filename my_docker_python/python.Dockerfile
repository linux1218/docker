FROM ubuntu:20.04
RUN apt update && apt install -y python && apt-get install -y pip && pip install pymysql


# mkdir -> cd 
WORKDIR /home/python/workspace
COPY ["db_handle.py", "."]
CMD ["python", "-u", "-m", "db_handle.py"]