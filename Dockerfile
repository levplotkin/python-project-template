FROM python:3.8 AS builder
RUN python -m pip install --upgrade pip

COPY requirements.txt .
RUN pip install --user -r requirements.txt


FROM python:3.8-slim
WORKDIR /app

COPY --from=builder /root/.local /root/.local
COPY ./src .

ENV PATH=/root/.local:$PATH
CMD [ "python", "./demo-app.py" ]
