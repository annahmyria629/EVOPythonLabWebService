FROM python:3.8-alpine
COPY . /EVOPythonLabWebService
WORKDIR /EVOPythonLabWebService

RUN pip install -r requirements.txt


CMD ["gunicorn", "-b", "0.0.0.0:5000","wsgi:app"]
#ENTRYPOINT [ "python" ]

#CMD ["wsgi.py"]
#CMD ["gunicorn", "-b", "0.0.0.0:5000", " --chdir", "EVOPythonLabWebService/webservice", "wsgi:app"]
#CMD ["python", "webservice/app.py"]
