FROM ubuntu

RUN apt -qq update
RUN apt -q install -y gcc gdb make python3-pip

WORKDIR /app/

COPY requirements.txt /app/
RUN pip3 install -qr ./requirements.txt

COPY Makefile *.c /app/
RUN rm -f chat ; make chat

# CMD python3 -m ipdb nosy_orig.py
# RUN gcc -g -o chat chat.c

