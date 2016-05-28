# rest-example using falcon framework

###### install memcached
apt-get install memcached
or
yum install memcached

###### download rabbitmq-server and install according to the diretions here
https://www.rabbitmq.com/download.html

###### if you want to see the rabbitmq server in action
sudo rabbitmq-plugins enable rabbitmq_management

###### install the miniconda distribution
wget https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh
bash Miniconda2-latest-Linux-x86_64.sh

answer yes to modifying the path in your .bashrc file

###### source your modified .bashrc file
source ~/.bashrc

###### execute the folloing conda commands to install the following packages
conda install gunicorn
conda install python-memcached
conda install --channel https://conda.anaconda.org/axiom-data-science falcon
conda install --channel https://conda.anaconda.org/axiom-data-science celery

###### if python pip not installed
wget https://bootstrap.pypa.io/get-pip.py
python get-pip.py

###### newest meinheld is not in conda, so we pip install it
pip install meinheld

###### start the celery backends
bin/runcelery

###### start the wsgi server
bin/runserver

###### unit testing
test.py
