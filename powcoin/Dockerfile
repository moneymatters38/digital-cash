FROM python:3.6.3
ADD requirements.txt ./
RUN pip install -r requirements.txt
ADD utils.py ./
ADD identities.py ./
ADD mypowcoin.py ./

CMD ["python", "-u", "mypowcoin.py", "serve"]
