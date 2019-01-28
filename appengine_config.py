# [START vendor]
#googlearchive/appengine-flask-skeleton. (2019). Retrieved from https://github.com/googlearchive/appengine-flask-skeleton/blob/master/appengine_config.py
from google.appengine.ext import vendor

# Add any libraries installed in the "lib" folder.
vendor.add('lib')
# [END vendor]