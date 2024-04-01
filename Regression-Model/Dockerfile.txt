FROM python:3.11

# Creating the user who will run the app
RUN adduser --disabled-password --gecos '' ml-api-user

WORKDIR /opt/ces-api

ARG PIP_EXTRA_INDEX_URL

# Installing requirements, pulling from Gemfury
ADD ./ces-api /opt/ces-api/
RUN pip install --upgrade pip
RUN pip install -r /opt/ces-api/requirements.txt

RUN chmod +x /opt/ces-api/run.sh
RUN chown -R ml-api-user:ml-api-user ./

USER ml-api-user

EXPOSE 8001

CMD ["bash", "./run.sh"]
