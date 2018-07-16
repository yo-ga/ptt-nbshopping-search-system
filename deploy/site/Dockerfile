FROM python:3.6

LABEL Name=proj Version=0.0.1

WORKDIR /app
ADD  ./src /app

RUN pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt
# CMD ["python3", "./main.py"]
