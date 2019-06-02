==========
Route53Dyn
==========

Development Environment
-----------------------

.. sourcecode:: bash

    git clone git@github.com:carlba/route53dyn.git
    virtualenv -p python3 venv && source venv/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt
    pip install -e .

Usage
-----

CLI
^^^

.. sourcecode:: bash

    route53dyn dahler.se hassio.dahler.se


Docker
^^^^^^
docker run -e ROUTE53DYN_DNS_NAME='dahler.se' -e ROUTE53DYN_HOST_NAMES='hassio.dahler.se' \
    -e AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID> \
    -e AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY> route53dyn



