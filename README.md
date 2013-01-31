tornado-utils
=============

Some tools for tornado web framework created by myself.

1. Validation framework usage
This framework is simply a decorator function, which accepts a
dict as its only arguments. The argument dict use request argument
name as its key, and a list of tuples of validator function and
validator arguments as its value. The usage is quite simple.

Examples
---------

    class RegisterHandler(tornado.web.RequestHandler):
        @validate({
            'username': [
                (required_validator),
                (regex_validator, (r"[a-zA-Z][\w]+"), "invalid username.")],
            'password': [(required_validator)]
        })
        def post(self):
            # your coding processing registration...


remember to add a error page template to your template path, for more
info, please refer to the source.

More utils are on the way...
