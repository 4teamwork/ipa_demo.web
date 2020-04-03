Webdemo
=======

The ``ipa_demo.web`` package contains a standard website for demo
purposes and might be deployed to https://ipa_demo.4teamwork.ch/

.. contents:: Table of Contents

Installation local development-environment
------------------------------------------

.. code:: bash

    $ git clone git@github.com:4teamwork/ipa_demo.web.git
    $ cd ipa_demo.web
    $ ln -s development.cfg buildout.cfg
    $ python2.7 bootstrap.py
    $ bin/buildout
    $ bin/instance fg

Dev-Test-Release-Process
------------------------

If you want to develop features, you must follow this guide

First checkout the package and create a new branch from the master:

.. code:: bash

    $ git clone git@github.com:4teamwork/ipa_demo.web.git
    $ cd ipa_demo.web
    $ git checkout -b my-new-feature
    $ git push origin -u my-new-feature

If you are finnished and the feature is working fine,you can merge it into the
master branch after the quality-check:

.. code:: bash

    $ git checkout master
    $ git merge my-mew-feature
    $ git push

Now, the feature is available for other developers.


Deployment
----------

For the deployment we use the `git-deploy <https://github.com/mislav/git-deploy>`_.

To setup the push deployment do the following steps on your local repo:
.. code:: console

    # once you have to install the remotes (local)
    ./scripts/setup-git-remotes

    # deployment auf "production":
    git push production master

The push deployment will run builodut if necessary, installst plone updates and
restarts the instances.
If possible, the deployment will run without server downtime. Otherwise, it will
activate a maintenance-page.


Compatibility
-------------

Runs with `Plone <http://www.plone.org/>`_ `4.3.x`.


Links
-----

- Github: https://github.com/4teamwork/ipa_demo.web
- Issues: https://github.com/4teamwork/ipa_demo.web/issues
- Continuous integration: https://jenkins.4teamwork.ch/search?q=ipa_demo.web

Copyright
---------

This package is copyright by `4teamwork <http://www.4teamwork.ch/>`_.

``ipa_demo.web`` is licensed under GNU General Public License, version 2.
