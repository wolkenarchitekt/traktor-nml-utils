FROM maven AS maven-builder
ARG package
ARG inputfile
RUN mkdir -p /opt/workspace
WORKDIR /opt/workspace
COPY pom.xml .
COPY ${inputfile} input.xml
RUN mvn \
    --batch-mode \
    --settings /usr/share/maven/ref/settings-docker.xml \
    dependency:resolve-plugins dependency:resolve \
    generate-sources \
    -DinputFile=input.xml \
    -DoutputFile=schema.xsd

FROM python:3.7.8-slim AS xsdata
RUN apt-get update && apt-get install -y vim
ARG package
ARG inputfile
ENV package=$package
ENV inputfile=$inputfile
WORKDIR /opt/workspace
COPY --from=maven-builder /opt/workspace/target/trang/schema.xsd /schema.xsd
RUN pip install xsdata ipdb
CMD cp /schema.xsd xml_schema_gen/${inputfile}.xsd && xsdata /schema.xsd --package ${package}
#CMD ls /schema.xsd