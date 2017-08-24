import os
for key, value in os.environ.items():
    print('{0} = "{1}"'.format(key, value))

TRAVIS_FORK_PULL_REQUEST = False
if ('TRAVIS_PULL_REQUEST_SLUG' in os.environ
    and os.environ['TRAVIS_PULL_REQUEST_SLUG']):
    if os.environ['TRAVIS_REPO_SLUG'] != os.environ['TRAVIS_PULL_REQUEST_SLUG']:
        TRAVIS_FORK_PULL_REQUEST = True
print('TRAVIS_FORK_PULL_REQUEST', TRAVIS_FORK_PULL_REQUEST)
