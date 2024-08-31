# pull python base image
FROM python:3.10
# copy application files
ADD . /credit_model_api/
# update pip
RUN pip install --upgrade pip
# install dependencies
RUN pip install fastapi uvicorn
# expose port for application
EXPOSE 8001
# start fastapi application
CMD ["python", "credit_model_api/main.py"]