# vim: set syntax=dockerfile:

FROM python:3.6-stretch

RUN set -ex; \
    apt-get update; \
    apt-get install --no-install-recommends -y \
        nginx \
        lighttpd \
        cron \
        supervisor \
        rsyslog \
    ; \
    ( apt-get clean && rm -rf /var/lib/apt/lists/* )


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

RUN set -ex; \
    pip install python-dotenv
RUN set -ex; \
    pip install --trusted-host prod-zync-docker01.zx --index-url http://prod-zync-docker01.zx:8080/ flask_web_app==2.76

ADD start /start
ADD files/wsgi.py /app/wsgi.py
RUN chmod ug+x /app/wsgi.py
RUN mkdir -p /app/static
ADD files/flask_web_app.conf /etc/supervisor/conf.d/flask_web_app.conf
RUN chmod ug+x /start

ADD files/lighttpd.conf /tmp/lighttpd.conf

RUN mkdir -p /var/log/gunicorn
RUN chmod 777 /var/log/gunicorn

RUN apt-get clean

CMD /start
