创建用户flink:flink
useradd -g flink flink
给用户flink添加docker执行权限
usermod -aG docker flink

编写Dockerfile文件

FROM flink:1.17

LABEL Author="Ayden"
RUN chown -R flink:flink /opt/flink
USER flink
COPY *.jar /opt/flink/lib/
RUN mkdir -p /opt/flink/upload/flink-web-upload
VOLUME ["/opt/flink/upload"]

编译镜像flinkcdc:latest
docker build -t flinkcdc:latest .

编写docker-compose

version: "2.2"
services:
  jobmanager:
    image: flinkcdc:latest
    security_opt:
      - seccomp=unconfined
    ports:
      - "127.0.0.1:8081:8081"
    command: "jobmanager"
    volumes:
      - /home/flink/flinkcdc/upload:/opt/flink/upload:Z
    environment:
      - |
        FLINK_PROPERTIES=
        jobmanager.rpc.address: jobmanager
        web.upload.dir: /opt/flink/upload
        jobmanager.memory.process.size: 4800m
  taskmanager:
    image: flinkcdc:latest
    security_opt:
      - seccomp=unconfined
    depends_on:
      - jobmanager
    command: taskmanager
    scale: 1
    environment:
      - |
        FLINK_PROPERTIES=
        jobmanager.rpc.address: jobmanager
        taskmanager.numberOfTaskSlots: 10

  sql-client:
    image: flinkcdc:latest
    command: bin/sql-client.sh
    security_opt:
      - seccomp=unconfined
    depends_on:
      - jobmanager
    environment:
      - |
        FLINK_PROPERTIES=
        jobmanager.rpc.address: jobmanager
        rest.address: jobmanager
        
        
        
创建映射卷目录
mkdir -p /home/flink/flinkcdc/upload/flink-web-upload
并将目录权限授权给flink:flink用户  
sudo chown -R flink:flink /home/flink/flinkcdc/upload/flink-web-upload
通过docker-compose运行
        
        
        