FROM python:latest
ENV TZ=Asia/Shanghai

WORKDIR /opt
COPY ./flask /opt/flask
RUN apt update && apt install vim nginx -y
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade pip --user
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple requests --user
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r ./flask/requirements.txt

COPY ./dist /var/www/html
RUN rm -f /etc/nginx/nginx.conf
COPY ./nginx.conf /etc/nginx/nginx.conf
ENTRYPOINT nginx && cd flask && gunicorn -w 4 -b 0.0.0.0:5000 app:app





 
