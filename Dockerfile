FROM python:3.8 AS builder
RUN python -m pip install --upgrade pip

COPY requirements.txt .
RUN pip install --user -r requirements.txt


FROM python:3.8-slim
WORKDIR /demo-app

COPY --from=builder /root/.local /root/.local
COPY ./test ./test
COPY ./src ./src
RUN  python -m pytest ./test
ENV PATH=/root/.local:$PATH
CMD [ "python", "./src/demo_app.py" ]
