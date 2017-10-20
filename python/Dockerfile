FROM python:3

COPY requirements.txt /tmp/

RUN pip install --no-cache-dir -r /tmp/requirements.txt \
    && rm -rf /tmp/requirements.txt

COPY ./python.py ./

EXPOSE 5000

CMD [ "python", "python.py" ]
