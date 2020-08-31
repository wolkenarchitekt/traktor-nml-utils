FROM maven:3.6.3-openjdk-14-slim
ARG inputfile
RUN mkdir -p /opt/workspace
WORKDIR /opt/workspace
COPY ${inputfile} schema.xml
COPY pom.xml .
RUN mvn exec:java
CMD cat /opt/workspace/schema0.xsd
