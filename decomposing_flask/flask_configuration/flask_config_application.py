"""
    This module loads the configuration specified
    in prod_settings.py. It displays the full
    configuration object once loaded.

    It also uses the Konfig project, a small layer
     (https://github.com/mozilla-services/konfig)
    on top of ConfigParser, which automates the
    conversion of simple types like integers and
    Booleans.
"""
from flask import Flask
from konfig import Config

'''
    Adds prod_settings configuration to Flask's 
    configuration object. The values have been 
    stored in app.config.py.json
'''
app = Flask(__name__)
app.config.from_object('prod_settings.Config')
print(app.config)

'''
        Since Flask exposes its configuration via app.config, it's 
        pretty simple to load additional options from a YAML file, 
        or any other text-based file. (see prod_settings.ini)
        
        Many Flask extensions exist to load the configuration from 
        an INI file, but using the standard library ConfigParser is 
        trivial. 
        
        There's one major caveat from using INI files: variables 
        values are all strings, and your application needs to 
        take care of converting them to the right type.
'''
c = Config('prod_setting.ini')
app.config.update(c.get_map('flask'))
print(app.config)
