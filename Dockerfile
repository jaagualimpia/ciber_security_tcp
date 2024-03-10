FROM python:3.9

COPY requirements.txt requirements.txt
COPY AES_Encrypter.py AES_Encrypter.py

RUN pip3 install -r requirements.txt
RUN alias py=python

COPY programita.py programita.py

CMD ["python"]
