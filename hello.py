def wsgi_application(environ, start_response):
  status = '200 OK'
  headers = [
    ('Content-Type', 'text/plain')
  ]
  qlist = environ['QUERY_STRING'].split('&')
  body = '\r\n'.join(qlist)
  start_response(status, headers)
  return [ body ]