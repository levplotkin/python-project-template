FROM python:3.8 AS builder
RUN python -m pip install --upgrade pip

COPY requirements.txt .
RUN pip install --user -r requirements.txt


FROM python:3.8-slim

COPY --from=builder /root/.local /root/.local
COPY . .
RUN  python -m pytest ./tests
ENV PATH=/root/.local:$PATH
WORKDIR /demo_app
CMD [ "python", "-m" , "demo_app" ]
