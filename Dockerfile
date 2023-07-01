FROM python:latest
WORKDIR /root/Projects/Docker
COPY . .
RUN pip install --upgrade pip
RUN pip install joblib

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
CMD ["python", "/root/Projects/Docker/load_model.py"]