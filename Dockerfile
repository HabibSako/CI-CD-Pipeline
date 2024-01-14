# pull official base image
FROM python:3.11

# set work directory
WORKDIR /app

# copy all files to work directory
COPY . /app

# install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# expose port
EXPOSE 5003

# command to run on container start
CMD ["python", "ornek.py"]
