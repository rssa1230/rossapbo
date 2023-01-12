from django.shortcuts import render

def data(request):
    nama = ["Rossa", "Raysa"]
    kelas = "12 RPL 1"

    konteks = {
        'name' : nama,
        'class' : kelas,

    }
    return render(request, 'data.html', konteks)
