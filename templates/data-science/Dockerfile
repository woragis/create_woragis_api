FROM python:3.13.3-slim

WORKDIR /worker

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "main.py" ]
