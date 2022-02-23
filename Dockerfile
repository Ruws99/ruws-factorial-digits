# Specify base image
FROM python:3

# Add the script
ADD main.py .

# install library dependencies
RUN pip install numpy

# specify entrypoint to receive external arguments to be passed into script
ENTRYPOINT [ "python", "./main.py"]
