from django.shortcuts import render
from .forms import InputForm
from .jenkins import render_scene


def index(request):
    if request.method == "POST":
        Path = request.POST.get("Path")
        RGB = request.POST.get("RGB")
        log = render_scene(Path, RGB)
        return render(request, "result.html", {"log": log})
    else:
        inform = InputForm()
        return render(request, "index.html", {"form": inform})
