FROM rkaneko/xenial-python3:0.1.1
MAINTAINER rkaneko <kanek.o.dev@gmail.com>

RUN pip install -U setuptools

# install deps for Scrapy
RUN apt-get update && apt-get install -y --no-install-recommends \
        libssl-dev \
        libffi-dev

WORKDIR /usr/src/app
COPY ./app/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app .
CMD ["scrapy", "runspider", "spacenews_spider.py"]
