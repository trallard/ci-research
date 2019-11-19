FROM python:3.6.4-stretch
LABEL maintainer="Tania Allard"

COPY ./requirements.txt /tmp/requirements.txt

RUN pip install /tmp/requirements.txt --no-cache \
    & mkdir ./bokeh

COPY ["./boston/", "./iris/", "./bokeh/"]

CMD /bin/bash