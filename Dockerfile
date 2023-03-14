FROM python:latest 

WORKDIR /app

RUN pip install discord && pip install python-dotenv

COPY . .

CMD {"python3", "Main.py"}