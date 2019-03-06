FROM python:3

ADD test1.py /

CMD [ "python", "-u", "./test1.py" ]
