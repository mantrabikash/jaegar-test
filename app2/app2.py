import json
import opentracing
import jaeger_client
from flask import Flask, jsonify, request

app = Flask(__name__)

# Create a Jaeger tracer
config = jaeger_client.Config(
config={
'sampler': {
'type': 'const',
'param': 1,
},
'logging': True,
},
service_name='app2',
)
tracer = config.initialize_tracer()

@app.route('/bar')
def bar():
# Extract the span context from the HTTP headers
    headers = dict(request.headers)
    span_ctx = opentracing.tracer.extract(opentracing.Format.HTTP_HEADERS, headers)
    # Start a new span
    with tracer.start_span('app2-bar', child_of=span_ctx) as span:
    # Do some processing
        data = {'message': 'Hello, World!'}
        # Add some tags to the span
        span.set_tag('http.method', 'GET')
        span.set_tag('http.url', request.url)
        span.set_tag('http.status_code', 200)
    return jsonify(data)

if __name__ == '__main__':
    app.run(port=5001)