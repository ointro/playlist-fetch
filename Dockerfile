FROM registry.access.redhat.com/ubi8/ubi:8.2

RUN mkdir /tmp/src &&\
  mkdir -p /var/opt &&\
  mkdir -p /var/opt/playlist-fetch/ &&\
  chmod 777 /var/opt/playlist-fetch/ &&\
  ls -al /var/opt/ &&\
  yum install -y python3 &&\
  pip3 install requests &&\
  pip3 install lxml &&\
  pip3 install bs4

COPY ./fetch.py /tmp/src

RUN chmod a+rx /tmp/src/fetch.py

WORKDIR /tmp/src

ENTRYPOINT ["python3", "fetch.py"]