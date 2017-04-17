#!/usr/bin/env python

import sys
sys.path.append("../../")

import json
import tornado.ioloop
from tornado_json.routes import get_routes
from tornado_json.application import Application


def main():
    import api
    routes = get_routes(api)
    print("Routes\n======\n\n" + json.dumps(
        [(url, repr(rh)) for url, rh in routes],
        indent=2)
    )
    # Create the application by passing routes and any settings
    application = Application(routes=routes, settings={}, generate_docs=True)

    # Start the application on port 8888
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    main()
