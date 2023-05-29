from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.

monthly_challenges = {
    "january": "Start a new hobby or learn a new skill.",
    "february": "Exercise for at least 30 minutes every day.",
    "march": "Read one book from a genre you haven't explored before.",
    "april": "Eat no meat for a whole month!",
    "may": "Take a daily walk and enjoy the outdoors.",
    "june": "Try a new recipe each week and expand your culinary skills.",
    "july": "Spend more time with family and friends.",
    "august": "Practice meditation or mindfulness daily for inner peace.",
    "september": "Set new goals and create a plan to achieve them.",
    "october": "Visit a local pumpkin patch or go apple picking.",
    "november": "Express gratitude daily and appreciate the small things in life.",
    "december": "Give back to your community through volunteering or acts of kindness."
}

def monthly_challenge_by_number(request, month):
  months = list(monthly_challenges.keys())

  if month > len(months):
      return HttpResponseNotFound("Invalid month!")

  redirect_month = months[month -1]
  return HttpResponseRedirect("/challenges/" + redirect_month)

def monthly_challenge(request, month):
  try:
    challenge_text = monthly_challenges[month]
    return HttpResponse(challenge_text)
  except:  
    return HttpResponseNotFound("This month is not supported!") 
  