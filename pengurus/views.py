from django.shortcuts import render, redirect
from pengurus.models import Data
from pengurus.forms import FormData

def ubah_data(request, id_data):
    data = Data.objects.get(id=id_data)
    template = 'ubah-data.html'
    if request.POST:
        form = FormData(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('ubah_data', id_data=id_data)
    else:
        form = FormData(instance=data)
        konteks = {
            'form':form,
            'data':data,
        }
        return render(request, template, konteks)

def data(request):
    dataa = Data.objects.all()

    konteks = {
        'dataa' : dataa,

    }
    return render(request, 'data.html', konteks)


def tambah_data(request):
    if request.POST:
        form = FormData(request.POST)
        if form.is_valid():
            form.save()
            form = FormData()
            pesan = "Data berhasil disimpan"

            konteks = {
                'form' : form,
                'pesan' : pesan,
            }
            return render(request, 'tambah-data.html', konteks)

    else: 
        form = FormData()

        konteks = {
            'form' : form,
        }

    return render(request, 'tambah-data.html', konteks)