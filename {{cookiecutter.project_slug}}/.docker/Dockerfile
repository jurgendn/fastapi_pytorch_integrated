# FROM python:some-version
# I recommend to use python-3.9.x-slim-bullseye
# Bullseye is the latest Debian version (Debian 11)
# Python < 3.10 for fully-compatible to older packages
# Python 3.10 makes change in abc -> BaseClass to abc.collections
FROM python:3.9.16-slim-bullseye

# Run this line image is Debian base: buster, bullseye
# If image is Alpine base, run this line instead
# RUN apk update
# However, I recommend to use Debian based if there is no restrict in computation resources

RUN apt-get update
RUN pip3 install pip --upgrade
# If there is any requirement for the project, install it here
# RUN apt-get install anyPackage

# Highly recommends requirements file to manage packages in the project
COPY requirements.txt .
RUN pip install -r requirements.txt

# Change to a non-root user and set working directory to user's home
RUN useradd -m working
USER working
WORKDIR /home/working/
COPY . .

# Set entrypoint if neccessary
# ENTRYPOINT ["command"]
# I will put command to a script file and run it via bash script instead of fixing it here
CMD ["/bin/bash", ".docker/entry.sh"]

