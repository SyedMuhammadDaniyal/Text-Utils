from django.http import HttpResponse
from django.shortcuts import render

# Code for video 11
def index(request):
    return render(request, 'index.html')

def analyze(request):
    # Getting text
    djtext = request.POST.get('text','defaut')
    # Getting check button
    check1 = request.POST.get('removepunc', "off")
    check2 = request.POST.get('uppertext', "off")
    check3 = request.POST.get('newline', 'off')
    check4 = request.POST.get('titlecase', 'off')
    check5 = request.POST.get('charcount', 'off')
    check6 = request.POST.get('removespace', 'off')
    # Assign empty string analyze
    if check1 == 'on':
        analyzed = ""
        import string
        punc = string.punctuation
        for char in djtext:
            if char not in punc:
                analyzed += char
        dict = {"analysed":analyzed}
        djtext = analyzed

    if check2 == 'on':
        analyzed = ""
        analyzed = djtext.upper()
        dict = {"analysed":analyzed}
        djtext = analyzed

    if check3 == 'on':
        analyzed = ""
        for index,char in enumerate(djtext):
            if not((djtext[index]=="\n") or (djtext[index] == "\r")):
                analyzed += char
        dict = {"analysed":analyzed}
        djtext = analyzed

    if check4 == 'on':
        analyzed = ""
        analyzed = djtext.title()
        dict = {"analysed":analyzed}
        djtext = analyzed

    if check5 == 'on':
        analyzed = ""
        analyzed = len(djtext)
        dict = {"analysed":analyzed}
        djtext = analyzed

    if check6 == 'on':
        analyzed = ""
        for index, char in enumerate(djtext):
            if not((djtext[index] == " ") and (djtext[index+1] == " ")):
                analyzed += char
        dict = {"analysed":analyzed}


    if (not(check1 == "on")) and (not(check2 == "on")) and (not(check3 == "on")) and (not(check4 == "on")) and (not(check5 == "on")) and (not(check6 == "on")):
        return HttpResponse("<h1 style= 'text-align:center; color:green;'>Error<br>Please check a button</h1>")

    return render(request, 'analyze.html', dict)
