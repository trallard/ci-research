LABEL maintainer="Tania Allard"

FROM python:3.6.4-strecth 

COPY ./requirements.txt /tmp/requirements.txt

RUN pip install /tmp/requirements.txt --no-cache \
    & mkdir ./bokeh

COPY ["./boston/", "./iris/", "./bokeh/"]

CMD /bin/bash