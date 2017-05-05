import json

def default_headers(class_context):
    class_context = class_context or type('',(),{})()
    headers   = {}
    if hasattr(class_context, 'token'):
        headers['Token'] = class_context.token
    return json.dumps(headers)
