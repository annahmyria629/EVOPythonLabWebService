FROM python:3.8-alpine
WORKDIR /webservice
ADD . /webservice
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
EXPOSE 5000