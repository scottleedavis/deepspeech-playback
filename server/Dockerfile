FROM ubuntu:16.04
RUN apt-get -y update && \
    apt-get -y install \
        python3 \
        python3-dev \
        wget && \
#        build-essential && \
# Install ffmpeg
    apt-get -y install software-properties-common && \
    add-apt-repository ppa:jonathonf/ffmpeg-4 && \
    apt-get -y update && \
    apt-get -y install ffmpeg && \
# install python dependencies
    wget https://bootstrap.pypa.io/get-pip.py && \
    python3 get-pip.py && \
    rm get-pip.py

COPY . /app
WORKDIR /app
RUN mkdir /app/json
RUN pip install -r requirements.txt
RUN pip3 install deepspeech

CMD python3 app.py