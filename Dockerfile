# Docker image for drone to deploy package to pypi 

FROM python
COPY ./upload.py /bin/upload
WORKDIR /drone/src
ENTRYPOINT ["/bin/upload"]
