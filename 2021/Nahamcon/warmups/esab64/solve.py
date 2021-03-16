with open('esab64','rb') as file:
    todebase = file.readlines()

todebase = ['mxWYntnZiVjMxEjY0kDOhZWZ4cjYxIGZwQmY2ATMxEzNlFjNl13X']
todebase[0][::-1]

import base64
base64.b64decode(todebase[0][::-1])

print(base64.b64decode(todebase[0][::-1])[::-1])
