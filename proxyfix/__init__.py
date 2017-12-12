'Entry point for flaskbb-plugin-proxyfix'

from werkzeug.contrib.fixers import ProxyFix

def flaskbb_extensions(app):
    'Apply the middleware'
    app.wsgi_app = ProxyFix(app.wsgi_app)
