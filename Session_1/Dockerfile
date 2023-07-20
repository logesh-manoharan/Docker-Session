FROM ubuntu
RUN apt-get update -y
RUN apt-get install apache2 -y
COPY index.html /var/www/html/index.html
COPY script.sh /root/script.sh
RUN chmod 777 /root/script.sh
Expose 80
ENTRYPOINT "/root/script.sh"; "bin/bash"