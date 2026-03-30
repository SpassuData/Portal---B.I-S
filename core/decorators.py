from django.shortcuts import redirect

def login_required(view_func):
    def wrapper(request):
        if not request.session.get('user'):
            return redirect('/login/')
        return view_func(request)
    return wrapper