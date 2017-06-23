FROM ubuntu:16.04
MAINTAINER rkaneko <kanek.o.dev@gmail.com>

# ensure local python is preferred over distribution python
ENV PATH /usr/bin:$PATH
ENV PATH /usr/local/bin:$PATH

# Japanese
RUN apt-get update && apt-get install -y --no-install-recommends \
        language-pack-ja-base \
        language-pack-ja \
        ibus-mozc \
        man

RUN update-locale LANG=ja_JP UTF-8 LANGUAGE=ja_JP:ja LC_ALL=ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LC_ALL ja_JP.UTF-8
ENV LC_CTYPE ja_JP.UTF-8
RUN ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime

# sudo
RUN apt-get update && apt-get install -y --no-install-recommends sudo

# Python3
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        python3 \
        python3-dev \
        python3-pip

# change the default python version
RUN cd "$(dirname $(which python3))" \
        && ln -s pydoc3 pydoc \
        && ln -s python3 python \
        && ln -s python3-config python-config \
        && ln -s pip3 pip

RUN which python
RUN which pip

RUN python -V
RUN pip -V

RUN pip install -U pip

CMD ["bash"]
