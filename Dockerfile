############################################################
# Dockerfile to run SolidFire's pythonCLI inside
# Using Alpine's Latest Release
############################################################

# Set the base image to Ubuntu
FROM alpine:latest

# File Author / Maintainer
MAINTAINER Chris Cochran

################## BEGIN INSTALLATION ######################
# Install Dependencies.
RUN apk add --no-cache \
		python3 \
		python3-dev \
    	py3-pip \
    	build-base \
		libc-dev \
		linux-headers \
		bash && \
    pip3 install --upgrade pip setuptools && \
    rm -r /root/.cache


#Installing the CLI
RUN pip3 install solidfire-cli

CMD bin/sh

##################### INSTALLATION END #####################
# TO KEEP RUNNING:
# After creating image call run this way:
# 	docker run -d -t <IMAGENAME> bin/bash
# To enter the docker to use the CLI:
# 	docker exec -i -t <IMAGEID> bin/bash