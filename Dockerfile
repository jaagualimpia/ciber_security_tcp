FROM python:3.9-slim

COPY requirements.txt requirements.txt
COPY AES_Encrypter.py AES_Encrypter.py

RUN pip3 install -r requirements.txt

COPY programita.py programita.py

RUN echo 'alias py=python' >> ~/.bashrc

CMD ["python"]
