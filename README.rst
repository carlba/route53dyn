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
-----------------------

.. sourcecode:: bash

    route53dyn dahler.se hassio.dahler.se
