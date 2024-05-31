FROM python:3.12.3-bookworm

ENV USERNAME=flask-app
ENV WORKING_DIR=/home/flask-app

WORKDIR ${WORKING_DIR}

COPY requirements.txt requirements.txt
COPY ./.docker/entrypoint.sh entrypoint.sh

COPY . .

RUN groupadd ${USERNAME} && \
    useradd -g ${USERNAME} ${USERNAME}

RUN chown -R ${USERNAME}:${USERNAME} ${WORKING_DIR}
RUN chmod -R u=rwx,g=rwx ${WORKING_DIR}

USER ${USERNAME}
ENV PATH "$PATH:/home/${USERNAME}/.local/bin"

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5000

RUN chmod +x entrypoint.sh

ENV FLASK_APP=run.py
ENV FLASK_RUN_HOST=0.0.0.0

RUN flask db init

ENTRYPOINT [ "./entrypoint.sh" ]