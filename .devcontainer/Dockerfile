FROM python:3.11

# RUN chmod +x /workspaces/advent_of_code_2023

RUN apt-get update && apt-get install -y --no-install-recommends  \
    git \
    python3-pip

RUN git config --global user.name schneiderjan
RUN git config --global user.email schneider.janniklas@gmail.com

RUN pip install pre-commit
COPY .pre-commit-config.yaml .
RUN git init . && pre-commit install-hooks

COPY requirements.txt .
RUN pip install -r requirements.txt