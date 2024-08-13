FROM ubuntu:22.04

RUN apt-get update && apt-get install -y sudo coreutils openssh-server

RUN mkdir /var/run/sshd
RUN echo 'PermitRootLogin no' >> /etc/ssh/sshd_config
RUN echo 'PasswordAuthentication yes' >> /etc/ssh/sshd_config
RUN echo 'AllowUsers test' >> /etc/ssh/sshd_config
RUN useradd -ms /bin/bash test 
RUN mkdir -p /home/test/.ssh && chmod 700 /home/test/.ssh 
COPY authorized_keys /home/test/.ssh/
COPY flag.txt /home/test/
RUN chmod 400 /home/test/flag.txt
#RUN chattr +i /home/test/flag.txt
RUN echo 'test ALL=(ALL) NOPASSWD: /usr/bin/cut' > /etc/sudoers.d/test
RUN chmod 600 /home/test/.ssh/authorized_keys && chown -R test:test /home/test/.ssh
RUN chown root:root /home/test/.ssh/authorized_keys
RUN chmod 405 /home/test/.ssh/authorized_keys
RUN ssh-keygen -A
USER test
WORKDIR /home/test
user root
CMD ["/usr/sbin/sshd", "-D"]
