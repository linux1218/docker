FROM ubuntu:20.04
RUN apt update && apt install -y python

# mkdir -> cd 
WORKDIR /home/python/workspace
COPY ["db_handle.py", "."]
CMD ["python", "-u", "-m", "db_handle.py"]