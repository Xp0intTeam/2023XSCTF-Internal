FROM python:3.9

WORKDIR /app

COPY src/ /app

RUN pip install -r /app/requirements.txt

RUN echo "XSCTF{SsT1_MilKTea_m1LktEa!}" > /flag

CMD ["python", "app.py"]

EXPOSE 8080
