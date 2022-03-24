from django.shortcuts import render


def HomePage(request):
    def logged_in_view(request):
        if request.user.is_authenticated:
            if request.user.groups.filter(name__in=["manager"]).exists():
                return render(request, "mysite/manager_homepage.html")
            if request.user.groups.filter(name__in=["members"]).exists():
                return render(request, "mysite/members_homepage.html")

        return render(request, "mysite/homepage.html")

    return logged_in_view(request)
