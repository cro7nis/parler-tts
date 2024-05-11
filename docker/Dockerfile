FROM pytorch/pytorch:2.0.1-cuda11.7-cudnn8-runtime as build

LABEL maintainer="cro7 <cro7nis@gmail.com>"

ENV USER=cro7
ENV APP=parler-tts
ENV PORT=8051

ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update \
    && apt-get install -y \
        build-essential \
        ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
    && useradd -m $USER

FROM build as runtime

RUN mkdir -p /opt/$APP \
  && chown $USER:$USER /opt/$APP

WORKDIR /opt/$APP
RUN pip install poetry
COPY --chown=$USER:$USER pyproject.toml pyproject.toml
#COPY --chown=$USER:$USER poetry.lock  poetry.lock
RUN  poetry config virtualenvs.create false \
    && poetry install --with=dev --no-root --no-interaction \
    && rm -rf /root/.cache/pypoetry

USER $USER

# Copy nesessary files to docker
COPY --chown=$USER:$USER src/app.py app.py
COPY --chown=$USER:$USER src/tts.py tts.py
COPY --chown=$USER:$USER configs configs
COPY --chown=$USER:$USER assets assets
COPY --chown=$USER:$USER checkpoints checkpoints
COPY --chown=$USER:$USER .streamlit .streamlit
COPY --chown=$USER:$USER docker/start_ui.sh start_ui.sh

ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/conda/lib/python3.10/site-packages/torch/lib

ENTRYPOINT bash start_ui.sh