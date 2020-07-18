FROM maven AS maven-builder
RUN mkdir -p /opt/workspace
WORKDIR /opt/workspace
COPY pom.xml .
COPY collection.nml collection.xml
RUN mvn -B -s /usr/share/maven/ref/settings-docker.xml dependency:resolve-plugins dependency:resolve generate-sources

FROM python:3.7.8-slim
WORKDIR /opt/workspace
COPY --from=maven-builder /opt/workspace/target/trang/collection.xsd .
RUN pip install xsdata
CMD xsdata /opt/workspace/xml_schema_gen/collection.xsd --package traktor_nml_utils.models