# from django.conf import settings
def my_middle(get_response):
    def my_function(request):
        print("code to be exetcuted before views function is getting called")
        res=get_response(request)
        print("code to be exetcuted after views function is getting called")
        return res
    return my_function
