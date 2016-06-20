# -*- coding: utf-8 -*-

import os
import config
from tracker.errors import ConfigVarNotFoundError
"""Set up config variables.

If environment variable APP_SETTINGS is set to dev and the config/dev.py
file exists then use that file as config settings, otherwise pull in settings from the production environment
"""

if os.environ.get('ENVIRONMENT') == 'dev':
    try:
        import config.dev as config  # config/dev.py
    except:
        raise EnvironmentError('Please create config/dev.py')
else:
    # production server environment variables
    import config.prod as config  # config/prod.py
    config.DEBUG = False

required_config_vars = [
    config.APP_SECRET_KEY,
    config.DEBUG,
    config.PORT,
    config.LOGGING_ON
]

try:
    any(required_config_vars) is None
except Exception as e:
    missing_var = e.message.split()[-1]
    raise ConfigVarNotFoundError(missing_var)
