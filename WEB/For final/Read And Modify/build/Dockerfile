FROM python:3.6-stretch

ENV PIP_INDEX_URL=https://pypi.tuna.tsinghua.edu.cn/simple

ADD flask-server /XSCTF
WORKDIR /XSCTF
RUN pip3 install -r requirements.txt
CMD ["python3", "app.py"]
