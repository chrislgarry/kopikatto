# Adds third party libraries installed to lib to an app engine runtime environment deployment
from google.appengine.ext import vendor

# Add any libraries install in the "lib" folder.
vendor.add('lib')
