from amazonlinux:latest
RUN yum update -y && \
yum install -y python3 python3-devel

WORKDIR /app
COPY . /app

RUN pip3 --no-cache-dir install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

EXPOSE 5000

ENTRYPOINT ["python3"]
CMD ["app.py"]
