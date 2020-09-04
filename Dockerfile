# Dockerfile has three Arguments: base, tag, branch
# base - base image (default: debian)
# tag - tag for base mage (default: stable-slim)
# branch - user repository branch to clone (default: master)
#
# To build the image:
# $ docker build -t <dockerhub_user>/<dockerhub_repo> --build-arg arg=value .
# or using default args:
# $ docker build -t <dockerhub_user>/<dockerhub_repo> .

# set the base image. default is debian, optional ubuntu 
ARG base=debian
# set the tag (e.g. latest, stable, stable-slim : for debian)
ARG tag=stable-slim
# set the erlang otp version to build/run 
ARG otp_v=23.0

# Build image, e.g. erlang:23.0
FROM erlang:${otp_v}

# Set build working directory
RUN mkdir /buildroot
WORKDIR /buildroot

# Copy our Erlang application and build the release
COPY . app
WORKDIR /buildroot/app
RUN rebar3 as prod release

# Base image, e.g. alpine:latest
FROM ${base}:${tag}

LABEL maintainer='Borja Esteban'

# Which user and group to use 
ARG user=application
ARG group=standard

# Set environments
ENV LANG C.UTF-8

# Install system updates and tools
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends \
# Install system updates and tools
        ca-certificates \
        git && \
# Clean up & back to dialog front end
    apt-get autoremove -y && \
    apt-get clean -y && \
    rm -rf /var/lib/apt/lists/*
ENV DEBIAN_FRONTEND=dialog

# Install user app:
COPY --from=0 /buildroot/app/_build/prod/rel/cicd_relx /app
WORKDIR /app

# Ports to expose
EXPOSE 8443
EXPOSE 8080

# Change user context and drop root privileges
RUN groupadd -r ${group} && \
    useradd --no-log-init -r -d /app -g ${group} ${user} && \
    chown -R ${user} . 
USER ${user}

# Start default script
ENTRYPOINT [ "/app/bin/cicd_relx" ]
CMD [ "foreground" ]

