FROM ubuntu
RUN apt update && apt install -y python3 python3-pip
WORKDIR /Faas/
COPY tf_funcion.py .
COPY requirements.txt .
RUN pwd
RUN pip3 install -r requirements.txt
