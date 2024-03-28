FROM python:3.10.6-slim-bullseye

WORKDIR /usr/src/app

RUN apt-get update \
	&& apt-get install -y \
		curl

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .
CMD ["python","-u","run.py"]