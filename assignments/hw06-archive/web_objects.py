class Request:
    """Represents an HTTP request. Parses a request and creates properties
    on this request instance. For example... if the request is:

    GET /dice HTTP/1.1
    User-Agent: p4a browser ftw! 
    Host: localhost:5000
    Accepts: text/html

    Then a Request object representing the above request (where req is the
    instance name):

    req.path --> "/dice"
    req.method --> "/GET"
    req.http_version --> "HTTP/1.1"
    req.headers --> {
        "User-Agent": "p4a browser ftw!",
        "Host": "localhost:5000",
        "Accepts": "text/html"
    }
    req.body --> "" (the request did not have a body)
    """
    # TODO: WRITE YOUR IMPLEMENTATION HERE!


class Response:
    """An object that represents an HTTP response. Example usage:

    res = Response(200)
    res.set_header('Content-Type', 'text/html')
    res.set_header('Server', 'p4a server ftw!')
    res.set_body('<h1>stuff</h1>')
    print(res)

    # prints out...

    HTTP/1.1 200 OK
    Content-Type: text/html
    Server: p4a server ftw!

    <h1>stuff</h1>
    """

    # TODO: WRITE YOUR IMPLEMENTATION HERE!

if __name__ == '__main__':
    """if you'd like to test your objects in isolation (which you should),
    you can write your tests here and run this file on its own (without
    web_server.py)
    """
    pass
    
