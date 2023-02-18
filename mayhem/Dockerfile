FROM fuzzers/atheris:2.0.7-python3.9

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

ADD . /src
WORKDIR /src

RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install stegano
RUN chmod +x /src/mayhem/fuzz-stegano.py

CMD ["python3 -m coverage run /src/mayhem/fuzz-stegano.py /src/testsuite/*"]
