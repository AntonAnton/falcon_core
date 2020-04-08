import falcon


class Resource(object):
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200  # This is the default status
        resp.body = ('\nHey, I love you, i want you, i want to go for'
                     ' a walking with you and i wont to eat little bit\n'
                     '\n'
                     '    ~ Your lovely husband\n\n')

# falcon.API instances are callable WSGI apps
app = falcon.API()

# Resources are represented by long-lived class instances
resource = Resource()

# things will handle all requests to the '/things' URL path
app.add_route('/for-my-wife', resource)