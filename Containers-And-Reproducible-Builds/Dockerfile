FROM ubuntu
# enviroment variable
ENV PYTHONBUFFER = 1

# Install our tools
RUN apt update && \
apt upgrade -y && \
apt install python3 python3-pip curl -y && \
pip3 install numpy pandas
