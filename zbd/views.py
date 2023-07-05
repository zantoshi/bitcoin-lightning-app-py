from django.shortcuts import render
from django.views import View
import requests, json
from django.http import JsonResponse
import zebedee
import environ

# Get Environmental Variables
env = environ.Env()

# Create a ZEBEDEE Project object
hackathon = zebedee.Project(env('ZEBEDEE_API_KEY'))

# You may now use the hackathon object to make API calls!

def index(request):
    # Example API Call
    # Getting balance
    wallet = hackathon.get_wallet_details()
    # Convert to Sats
    balance = hackathon.convert_msats_to_sats(wallet["balance"])
    # Creating the context for the template
    ctx = {"balance" : balance}
    # Passing the context to the template in ./zbd/index.html and rendering the template.
    return render(request, "zbd/index.html", ctx)

