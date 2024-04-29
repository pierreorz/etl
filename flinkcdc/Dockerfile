FROM flink:1.17

LABEL Author="Ayden"
RUN chown -R flink:flink /opt/flink
USER flink
COPY *.jar /opt/flink/lib/
RUN mkdir -p /opt/flink/upload/flink-web-upload
VOLUME ["/opt/flink/upload"]
