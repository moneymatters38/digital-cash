FROM python:3.6.3
ADD requirements.txt ./
RUN pip install -r requirements.txt
ADD utils.py ./
ADD identities.py ./
ADD my_pow_syndacoin.py ./

CMD ["python", "-u", "my_pow_syndacoin.py", "serve"]
