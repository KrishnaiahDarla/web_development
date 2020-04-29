# vim: set syntax=dockerfile:

FROM python:3.6-stretch

RUN set -ex; \
    apt-get update; \
    apt-get install --no-install-recommends -y \
        redis-server \
        netcat \
        postgresql \
        ca-certificates \
        # Add libraries for sasl
        libsasl2-2 \
        libsasl2-dev \
        libsasl2-modules \
        sasl2-bin \
        nginx \
        lighttpd \
        cron \
        supervisor \
        rsyslog \
    ; \
    ( apt-get clean && rm -rf /var/lib/apt/lists/* )

ENV FOREGO_URL "https://bin.equinox.io/a/69MotMTHnJ5/forego-20180217041714-linux-amd64.tar.gz"
ENV FOREGO_SHA256 "b104fa2f2bf9ea507b2bc3a3673084a67380b7a2d57dbdd457b9b5896e963d56"
RUN set -ex; \
    wget -O /usr/local/bin/forego.tar.gz ${FOREGO_URL}; \
    bash -c "sha256sum -c < <(echo '${FOREGO_SHA256} /usr/local/bin/forego.tar.gz')"; \
    tar xzvf /usr/local/bin/forego.tar.gz -C /usr/local/bin/; \
    rm /usr/local/bin/forego.tar.gz; \
    chmod +x /usr/local/bin/forego; \
    forego version

ENV PYTHON_PIP_VERSION 10.0.1
RUN set -ex; \
    wget -O get-pip.py 'https://bootstrap.pypa.io/get-pip.py';  \
    python3 get-pip.py \
        --disable-pip-version-check \
        --no-cache-dir \
        "pip==$PYTHON_PIP_VERSION" \
    ; \
    pip --version; \
    \
    find /usr/local -depth \
        \( \
            \( -type d -a \( -name test -o -name tests \) \) \
            -o \
            \( -type f -a \( -name '*.pyc' -o -name '*.pyo' \) \) \
        \) -exec rm -rf '{}' +; \
    rm -f get-pip.py;

# Setting env variable to avoid one of Airflow's dependencies to install a GPL dependency (unidecode)
RUN echo 'here'
ENV SLUGIFY_USES_TEXT_UNIDECODE yes
RUN echo 'HERE'
RUN set -ex; \
    pip install python-dotenv
RUN set -ex; \
    pip install --trusted-host prod-zync-docker01.zx --index-url http://prod-zync-docker01.zx:8080/ dc-core==1.39
RUN set -ex; \
    pip install --trusted-host prod-zync-docker01.zx --index-url http://prod-zync-docker01.zx:8080/ dc-activity-service==2.76

ADD files/pipe_file.py /app/scripts/pipe_file.py
RUN chmod ug+x /app/scripts/pipe_file.py
ADD start /start
ADD files/wsgi.py /app/wsgi.py
RUN chmod ug+x /app/wsgi.py
RUN mkdir -p /app/static
ADD files/activity-service.conf /etc/supervisor/conf.d/activity-service.conf
RUN chmod ug+x /start

ADD files/lighttpd.conf /tmp/lighttpd.conf

ADD files/root-crontab /tmp/root-crontab
RUN chown root:crontab /tmp/root-crontab
RUN chmod 0600 /tmp/root-crontab
RUN mkdir -p /var/log/gunicorn
RUN chmod 777 /var/log/gunicorn

ADD files/50-default.conf /etc/rsyslog.d/50-default.conf

RUN rm /etc/localtime
RUN ln -s /usr/share/zoneinfo/US/Pacific /etc/localtime

RUN apt-get clean

RUN echo "uwsgi_read_timeout 7200s;" > /etc/nginx/conf.d/custom_timeout.conf


CMD /start
