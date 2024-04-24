FROM python:3.9

RUN mkdir /videomaker

WORKDIR /videomaker

RUN mkdir /videomaker/media

COPY reqs.txt .

RUN pip install --upgrade pip

RUN pip install -r reqs.txt

COPY . .