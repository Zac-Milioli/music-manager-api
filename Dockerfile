FROM python:3.13-slim

WORKDIR /
COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000

CMD python main.py