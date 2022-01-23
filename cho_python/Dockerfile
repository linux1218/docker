FROM ubuntu:20.04
RUN apt update && apt install -y python3

WORKDIR /home/cho
COPY ["db_handle.py", "."]
# CMD ["python", "-u", "-m", "db_handle.py"]

# docker build --tag py_v1 .
# docker run -it -d --name py_1 py_v1 --network cho_net 
# docker exec -it py_1 /bin/bash
# docker logs py_1

# docker stop py_1
# docker rm py_1
# docker rmi py_v1