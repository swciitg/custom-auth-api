from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, JsonResponse
from .auth_helper import get_sign_in_flow, get_token_from_code, store_user, remove_user_and_token, get_token
from .graph_helper import *
from django.urls import reverse
# Create your views here.

def initialize_context(request):
  context = {}

  # Check for any errors in the session
  error = request.session.pop('flash_error', None)
  context['errors'] = []

  if error != None:
    context['errors'].append(error)

  # Check for user in the session
  context['user'] = request.session.get('user', False)
  return context

def home(request):

  context = initialize_context(request)

  if(context['user']):
    return JsonResponse({
        'message': 'You have been successfully authenticated',
        'user details': context['user']
    }, status=200)
    
  elif len(context['errors']) > 0:
    return JsonResponse({
        'message': 'authentication failed!',
        'errors': context['errors']
    }, status=404)
  
  else:
    return redirect('signin')

def sign_in(request):
  # Get the sign-in flow
  flow = get_sign_in_flow()
  # Save the expected flow so we can use it in the callback
  try:
    request.session['auth_flow'] = flow
  except Exception as e:
    print(e)
  # Redirect to the Azure sign-in page
  return HttpResponseRedirect(flow['auth_uri'])


def callback(request):
  # Make the token request
  result = get_token_from_code(request)
  
  #Get the user's profile
  user = get_user(result['access_token'])

  # Store user
  store_user(request, user)
  return HttpResponseRedirect(reverse('home'))


def sign_out(request):
  # Clear out the user and token
  remove_user_and_token(request)

  return JsonResponse({
      'message': 'Successfully logged out!'
  }, status=200)



#91c424eb-af1a-4526-a592-2f56f774f4be