from source import route1

def post_http() -> None:
    http_message = {
        "method" : "POST",
        "header" : {
            "token" : "1234567890",
            "origin" : "http://some.url.com"
        },
        "body" : {
            "name" : "John Doe",
            "message" : "Hello World!"
        }
    }

    route1(http_message)