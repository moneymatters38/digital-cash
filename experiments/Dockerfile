FROM python:3.6.3
ADD requirements.txt ./
RUN pip install -r requirements.txt
ADD alternating.py ./

CMD ["python", "alternating.py", "serve"]
