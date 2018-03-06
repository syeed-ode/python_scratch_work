"""
    The Flask object comes with an object called config, which
    contains some built-in variables, and which can be updated
    when you start your Flask app via your configuration objects.

    Flask uses a mechanism similar to Django in its confiugration
    approach.
"""
class Config:
    """
        There are two significant drawbacks when using Python
        modules as configuration files.

        1) Assuring the configuration files are managed separately
           from the code.
        2) If another team is in charge of managing the
           configuration file of your application, they will need
           to edit the Python code to do so. For instance, it's
           harder to make Puppet templates out of Python modules
           rather than flat, static configuration files.
    """
    DEBUG = False
    SQLURI = 'postgres://tarek:xxx@localhost/db'