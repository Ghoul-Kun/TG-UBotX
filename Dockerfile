# We're using Alpine Edge
FROM archlinux:latest

#
# Updating Arch
#
RUN pacman -Syu --noconfirm

#
# Installing Packages
#
RUN pacman -Syu --noconfirm \
    coreutils \
    bash \
    base-devel \
    bzip2 \
    curl \
    figlet \
    gcc \
    clang \
    git \
    sudo \
    aria2 \
    util-linux \
    libevent \
    libffi \
    libwebp \
    libxml2 \
    libxslt \
    linux \
    linux-headers \
    musl \
    neofetch \
    postgresql \
    postgresql-client \
    postgresql-libs \
    openssl \
    pv \
    jq \
    wget \
    python \
    readline \
    sqlite \
    ffmpeg \
    sqlite \
    sudo \
    chromium \
    zlib \
    jpeg-archive \
    zip


RUN python3 -m ensurepip \
    && pip3 install --upgrade pip setuptools \
    && rm -r /usr/lib/python*/ensurepip && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    rm -r /root/.cache

#
# Clone repo and prepare working directory
#
RUN git clone 'https://github.com/HitaloKun/TG-UBotX.git' /root/userbot
RUN mkdir /root/userbot/bin/
WORKDIR /root/userbot/

#
# Copies session and config (if it exists)
#
COPY ./sample_config.env ./userbot.session* ./config.env* /root/userbot/

#
# Install requirements
#
RUN pip3 install -r requirements.txt
RUN pip list --outdated --format=freeze | grep -v '^\-e' | cut -d = -f 1 | xargs -n1 pip install -U
CMD ["python3","-m","userbot"]
