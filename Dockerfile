FROM python:latest
# 
WORKDIR /code
# 
COPY requirements.txt /code/requirements.txt
# 
RUN pip install --upgrade pip
RUN pip install -r /code/requirements.txt 
# 
COPY fast_api.py /code/fast_api.py 
#
COPY survival_pred.pkl /code/survival_pred.pkl
#
COPY load_model.py /code/load_model.py
#
CMD ["uvicorn", "fast_api:app", "--host", "0.0.0.0"]