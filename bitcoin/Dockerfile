FROM python:3.6.3
ADD requirements.txt ./
RUN pip install -r requirements.txt
ADD mybitcoin.py ./

CMD ["python", "-u", "mybitcoin.py", "serve"]
