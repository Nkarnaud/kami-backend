FROM python:3.11.5-bookworm AS builder
ENV PYTHONUNBUFFERED=1
ENV PIP_DISABLE_PIP_VERSION_CHECK=on
ENV PIP_DEFAULT_TIMEOUT=100
ENV POETRY_NO_INTERACTION=1
ENV POETRY_VERSION=1.8.3
ENV VIRTUAL_ENV="/home/pythonrunner/.venv"
ENV PATH="/home/pythonrunner/.local/bin:${VIRTUAL_ENV}/bin:${PATH}"

LABEL authors="Arnaud Tsombeng"

RUN useradd -ms /bin/bash pythonrunner

WORKDIR /app

RUN apt-get update && \
    apt-get install -y \
    python3-dev \
    libpq-dev \
    wget \
    iputils-ping \
    vim \
    libnss3 \
    libnspr4 \
    libdbus-1-3 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libatspi2.0-0 \
    libxcomposite1 \
    libxdamage1 \
    libxfixes3 \
    libxrandr2 \
    libgbm1 \
    libdrm2 \
    libxkbcommon0 \
    libasound2 \
    x11vnc \
    xvfb \
    procps

RUN pip install poetry==${POETRY_VERSION}

COPY --chown=pythonrunner:pythonrunner poetry.lock pyproject.toml /app/

RUN python -m venv $VIRTUAL_ENV
RUN poetry install --no-root --no-cache

COPY --chown=pythonrunner:pythonrunner kami /app/kami

WORKDIR /app/kami
USER pythonrunner


CMD ["bash"]
