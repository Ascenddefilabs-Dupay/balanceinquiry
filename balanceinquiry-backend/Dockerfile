FROM python:3.11-slim

WORKDIR /balanceinquiry-backend

COPY requirements.txt /balanceinquiry-backend/
RUN pip3 install -r /balanceinquiry-backend/requirements.txt

COPY . .


CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]
