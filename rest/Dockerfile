FROM nginx
COPY . /code
workdir /code
RUN cp -r nginx/* /etc/nginx/

EXPOSE 80 8080
CMD ["nginx", "-g", "daemon off;"]
# RUN echo 'deb http://ftp.debian.org/debian stretch-backports main' >> /etc/apt/sources.list \
    # && apt-get update \
    # && apt-get install -y python-certbot-nginx -t stretch-backports \
    # && service nginx stop \
    # && certbot -i nginx -d "*.buglan.org" -d buglan.org --server https://acme-v02.api.letsencrypt.org/directory \
    # && service nginx start
