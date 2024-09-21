FROM python:3.12.6-bullseye

WORKDIR /usr/src/app

COPY ./requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . . 

CMD ["fastapi", "run", "main.py", "--port", "8080"]