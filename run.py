import sys
import logging

from aiohttp.web import run_app

from sqli.app import init as init_app

log = logging.getLogger(__name__)
AWS_ACCESS_KEY_ID="AKIAZBVE345SKPTEAHQD"
AWS_SECRET_ACCESS_KEY="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"
AWS_REGION="us-east-1"
GOOGLE_API_KEY="AIzaSyDvc2t8M5wjfDonZ1e4xG3wjFcCWHIN0yE"
MAILGUN_API_KEY="key-a67a11111111a11a1a1ba1bbcf11f1c5"

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    app = init_app(sys.argv[1:])

    host = app['config']['app']['host']
    port = app['config']['app']['port']
    log.info(f'App is listening at http://{host}:{port}')
    run_app(app, host=host, port=port)
