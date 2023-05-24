import requests
import opentracing
import jaeger_client
from flask import Flask

app = Flask(__name__)



# Create a Jaeger tracer
config = jaeger_client.Config(config={
'sampler': {
'type': 'const',
'param': 1,
},
'logging': True,
},
service_name='app1',
)
tracer = config.initialize_tracer()

@app.route('/foo')
def foo():
# Start a new span
    with tracer.start_span('app1-foo') as span:
    # Inject the span context into the HTTP headers
        headers = {}
        opentracing.tracer.inject(span, opentracing.Format.HTTP_HEADERS, headers)
        # Send an HTTP request to app2 with the span context in the headers
       
        url = 'http://app2:5001/bar'
        response = requests.get(url, verify=False, headers=headers)
        # Add some tags to the span
        span.set_tag('http.method', 'GET')
        span.set_tag('http.url', url)
        span.set_tag('http.status_code', response.status_code)
    return response.text

if __name__ == '__main__':
    app.run(port=5000)