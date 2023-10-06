# 使用 Python 3.9 镜像作为基础镜像
FROM python:3.9

# 将应用程序代码复制到容器中
COPY src /app

# 安装应用程序依赖
RUN     groupadd -r appgroup && \
	useradd -r -g appgroup appuser && \
	chown -R appuser:appgroup /app && \
	chmod -R 500 /app && \
	pip install -r /app/requirements.txt -i https://mirrors.aliyun.com/pypi/simple/ && \
	echo "XSCTF{SsT1_MilKTea_m1LktEa!}" > /flag

USER appuser

CMD ["python", "/app/app.py"]

EXPOSE 8080
