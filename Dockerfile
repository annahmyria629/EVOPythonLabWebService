FROM python:3.8-alpine
WORKDIR /EVOPythonLabWebService
COPY . /EVOPythonLabWebService
RUN pip install -r requirements.txt
WORKDIR webservice/
CMD ["gunicorn", "-b", "0.0.0.0:5000", "--log-level=debug", "wsgi:app"]
#CMD ["python", "webservice/app.py"]
EXPOSE 5000