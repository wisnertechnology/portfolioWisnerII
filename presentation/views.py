from django.shortcuts import redirect, render
from .models import Mesaj
from .forms import formsMesaj

# Create your views here.

# Pour la page d'acceuil
def home(request):
    return render(request, 'index.html')




# Pour la page de contact
def contact(request):
    if request.method == "POST":
        nomComplet = request.POST.get('Fullname')
        emailadrss = request.POST.get('EmailAddress')
        phoneNb = request.POST.get('PhoneNumber')
        Mss = request.POST.get('Message')

        newMessage = Mesaj.objects.create(Fullname=nomComplet, EmailAddress=emailadrss, PhoneNumber=phoneNb, Message=Mss)
        newMessage.save()

        print("tout est bien passee")
        return redirect(home)
    
    return render(request, 'contact.html')



def extractForm(request):
    
    if request.method == "POST":
        # Fullname = request.POST.get('Fullname')
        # EmailAddress = request.POST.get('EmailAddress')
        # PhoneNumber = request.POST.get('PhoneNumber')
        # Message = request.POST.get('Message')

        form = formsMesaj(data=request.POST)
        if form.is_valid():
            form.save()
            print("donnee enregistrer")
            print("donnee enregistrer")
            print("donnee enregistrer")
            print("donnee enregistrer")
            print("donnee enregistrer")
            print("donnee enregistrer")
            print("donnee enregistrer")
            print("donnee enregistrer")
            print("donnee enregistrer")
            print("donnee enregistrer")
        return redirect(home)
    
    else:
        form = formsMesaj()
        print("erreur d'envoi")
        print("erreur d'envoi")
        return render(request, 'kontak.html', {'form':form})






# Pour la page de contact
def projects(request):
    return render(request, 'projects.html')





# Pour la page de contact
def resume(request):
    return render(request, 'resume.html')