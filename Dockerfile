########################
FROM ubuntu:18.04
########################
RUN apt-get update
RUN apt-get install -y fortune fortunes
RUN apt-get install -y cowsay
RUN apt-get install -y python3.8
RUN apt-get install -y python3-pip
########################
ENV PATH=$PATH:/usr/games
ENV LC_ALL=C.UTF-6
ENV LANG=C.UTF-8
########################
