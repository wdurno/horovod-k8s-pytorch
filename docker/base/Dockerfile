FROM ubuntu 

ENV HOROVOD_WITH_PYTORCH=1 \
    PYTHONPATH=/app/src/python 

ADD app /app

RUN apt-get install -y \
        gcc \
        libopenmpi && \
    apt install -y \
        python3-pip && \
    pip3 install horovod[pytorch] 
