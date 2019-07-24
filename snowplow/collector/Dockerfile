FROM snowplow-docker-registry.bintray.io/snowplow/base-alpine:0.2.0
LABEL maintainer="ander.pp@gmail.com"

# Important:
# This is a copy from https://github.com/snowplow/snowplow-docker/blob/develop/scala-stream-collector/0.15.0/kinesis/Dockerfile.
# It should be used to test unrelesed versions.

# The version of the collector to download.
ENV COLLECTOR_VERSION="0.15.0"

# The targeted platform
ENV PLATFORM="kinesis"

# The name of the archive to download.
ENV ARCHIVE="snowplow_scala_stream_collector_${PLATFORM}_${COLLECTOR_VERSION}.zip"

# Install the Scala Stream Collector.
COPY snowplow-stream-collector-kinesis-0.15.0.jar ${SNOWPLOW_BIN_PATH}

# Port used by the collector.
EXPOSE 8080

# Defines an entrypoint script delegating the lauching of the collector to the snowplow user.
# The script uses dumb-init as the top-level process.
COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh
ENTRYPOINT [ "docker-entrypoint.sh" ]

CMD [ "--help" ]

