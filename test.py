import os
for key, value in os.environ.items():
    print('{0} = "{1}"'.format(key, value))
