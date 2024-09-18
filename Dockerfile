FROM python:3.7.9-slim-stretch

WORKDIR /

COPY requirements.txt ./

COPY app.py ./

RUN pip install flask

EXPOSE 5000

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
