FROM python:3.8-alpine
WORKDIR /EVOPythonLabWebService
COPY . /EVOPythonLabWebService
RUN pip install -r requirements.txt
CMD ["python", "webservice/app.py"]
EXPOSE 5000