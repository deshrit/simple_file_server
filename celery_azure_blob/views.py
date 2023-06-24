from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .forms import FileUploadForm
from django.contrib import messages

from .models import File
from .tasks import handle_files_upload, get_uploaded_files

def index(request):
    form = FileUploadForm()
    if request.method == "POST":
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            handle_files_upload(request.FILES.getlist('file'))
            messages.add_message(request, messages.INFO, "Files sent to upload queue.")
            return redirect("index")
    names = get_uploaded_files()
    files = File.objects.filter(is_deleted=False, blob_name__in=names).order_by('-uploaded_at')
    context = {'form': form, 'files': files}
    return render(request, 'index.html', context)


def delete(request, id):
    obj = get_object_or_404(File, pk=id)
    obj.is_deleted = True
    obj.save()
    messages.add_message(request, messages.WARNING, f"'{obj.file_name}{obj.file_ext}' deleted")
    return redirect("index")

def refresh(request):
    names = get_uploaded_files()
    files = File.objects.filter(is_deleted=False, blob_name__in=names).order_by('-uploaded_at')
    files = list(files.values())
    return JsonResponse(files, safe=False)