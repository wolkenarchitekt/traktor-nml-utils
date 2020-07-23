FROM maven AS maven-builder
RUN mkdir -p /opt/workspace
WORKDIR /opt/workspace
COPY pom.xml .

COPY collection.nml collection.xml
RUN mvn \
    --batch-mode \
    --settings /usr/share/maven/ref/settings-docker.xml \
    dependency:resolve-plugins dependency:resolve \
    generate-sources \
    -DinputFile=collection.xml \
    -DoutputFile=collection.xsd

COPY history.nml history.xml
RUN mvn \
    --batch-mode \
    --settings /usr/share/maven/ref/settings-docker.xml \
    dependency:resolve-plugins dependency:resolve \
    generate-sources \
    -DinputFile=history.xml \
    -DoutputFile=history.xsd
