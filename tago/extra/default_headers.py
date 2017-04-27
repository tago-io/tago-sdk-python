import json

pkg = json.load(open('package.json'))
isBrowser = False

def default_headers(class_context):
    class_context = class_context or type('',(),{})()
    headers   = {}
    if hasattr(class_context, 'token'):
        headers['Token'] = class_context.token
    if not isBrowser:
        headers['User-Agent'] = 'Tago-Nodelib'+str(pkg[u'version'])
    return json.dumps(headers)
