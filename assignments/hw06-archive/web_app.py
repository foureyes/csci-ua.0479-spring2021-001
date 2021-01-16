from web_objects import Request, Response
import random
        
# routes contains mappings of paths to functions
# for example, the path /dice would map to a function called dice:
# {'/dice': dice,
# '/': home}
# that function will be called to generate a response
routes = {}

def route(path):
    """decorator (with parameter) for used to map a path to a function
    """
    def decorator(old_f):
        # add path and function to routes dictionary
        routes[path] = old_f

        # just give back the old function unmodified
        return old_f

    return decorator

##########
# ROUTES #
##########
@route('/')
def home(req):
    res = Response(200)
    html = 'The homepage! '
    html += 'Check out <a href="/creatures">creatures</a> '
    html += 'or <a href="/dice">dice</a>.'
    res.set_body(html)
    return res

@route('/creatures')
def creatures(req):
    """displays a page of random creatures in an unordered list!
    """

    # TODO: WRITE YOUR IMPLEMENTATION HERE!
    # (remove pass below)
    pass

@route('/dice')
def dice(req):
    res = Response(200)
    html = "Dice Roll: {}".format(random.randint(1, 6))
    res.set_body(html)
    return res

def handle_request(http_request):
    """takes an http request as a string and gives backs an http response
    as a string
    """

    # TODO: WRITE YOUR IMPLEMENTATION HERE!

    # 1. create a Request object based on the incoming http request

    # 2. based on the path of the http request, get the right "route"
    #    (function that will generate the appropriate response... that is
    #    one of the functions above)

    # 3. if the route exists, call the appropriate function with the
    #    request object as a parameter... add any headers necessary
    #    to the resulting Response object

    # 4. if the route doesn't exist, create a Response object with a
    #    status code of 404 and a body of "Not Found"

    # 5. give back the resulting response object from the either of the
    #    two previous steps as a string (just use str(...))

    # 6. (remove pass below)
    pass
