FROM python:3.7

WORKDIR /app

COPY . .

ENTRYPOINT ["python"]

RUN pip install -r requirements.txt

CMD ["python","main.py"]
