FROM python:3.11-slim-buster
WORKDIR /backend
COPY ./requirements.txt /backend
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
ENV FLASK_APP=app.py
CMD ["flask", "run", "--host", "0.0.0.0"]