===========================
Contribution to balancr_rtd
===========================

Every team member is encouraged to contribute to the Read the Docs technical documentation. The source code is hosted on GitHub in the repository called balancr_rtd. 

Creating a new version should be done as soon as possible and may involve:

- correcting the documentation

    - updating a value
    - fixing a mistake
    
- extending the documentation

    - adding a missing piece of information in an existing section
    - creating a new section.

Development
===========

To contribute to the technical documentation's source code, do as follows:

1. Clone the repository `balancr_rtd <https://github.com/swissbalancr/balancr_rtd/>`_ to your computer

    - :bash:`git clone git@github.com:swissbalancr/balancr_rtd.git`

2. Create a virtual environment & activate it

    - :bash:`virtualenv -p /usr/bin/python3 balancr_rtd`
    - :bash:`source ~/.virtualenvs/balancr_rtd/bin/activate`

3. Install Python packages

    - :bash:`pip install sphinx`
    - :bash:`pip install sphinx_rtd_theme`
    - :bash:`pip install sphinx-autobuild`

4. Open the source code in VS code & add the extension called "reStructuredText Syntax highlighting" to provide syntax highlighting for reStructuredText
5. Build HTML pages in the build directory & start a web server that listens on the IP address 127.0.0.1 and port 8000

    - :bash:`sphinx-autobuild -b html source/ build/`

6. Open a web browser and go to the URL `http://127.0.0.1:8000/ <http://127.0.0.1:8000/>`_
7. Make changes to the source code following the Git branching strategy described in :ref:`Pull request workflow`; Each time you save a file in the project, the `build` folder is automatically updated

This workflow was tested on Ubuntu 20.04.

CI/CD
=====

Each time a pull request on GitHub is accepted and a branch is merged into `master`, 

- an automatic build takes place (CI); See its progress on `this web page <https://readthedocs.org/projects/balancr-rtd/>`_
- an automatic deployment of the web application takes place after a successful build (CD); Open your web browser and send a request to `this URL <https://balancr-rtd.readthedocs.io/en/latest/>`_