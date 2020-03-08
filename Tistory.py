import requests
import webbrowser
import os
import http.server
import sys
from aiohttp import web
import threading
import asyncio
import Github
import UserInfo
import json
import CallBackServer

WRITE_POST_API = "https://www.tistory.com/apis/post/write"
MODIFY_POST_API = "https://www.tistory.com/apis/post/modify"
GET_CATEGORIES_API = "https://www.tistory.com/apis/category/list"
CODE_URL = "https://www.tistory.com/oauth/authorize"
CALLBACK_URL = "http://localhost:5000/callback"
TOKEN_URL = "https://www.tistory.com/oauth/access_token"

call_count = 1

def processToken(request):
    code = request.query_string.split('&')[0].split('=')[1]
    response = requests.get(TOKEN_URL, params={
        'client_id': UserInfo.get_client_id(),
        'client_secret':UserInfo.get_client_secret(),
        'redirect_uri': CALLBACK_URL,
        'code': code,
        'grant_type':'authorization_code',
        'output':'json'
    })

    key = response.text.split('=')[0]
    value = response.text.split('=')[1]
    if key == 'access_token':
        UserInfo.write_access_token(value)
        print('토큰 발급 완료')
        exit()

def writePost(req):
    req['access_token'] = UserInfo.get_access_token()
    req['blogName'] = UserInfo.get_blog_name()
    req['content'] = Github.toHtmlFromMarkdown(req['content'])

    response = requests.post(WRITE_POST_API, data=req)
    print(response.text)
    return response

def modifyPost(req):
    req['access_token'] = UserInfo.get_access_token()
    req['blogName'] = UserInfo.get_blog_name()
    req['content'] = Github.toHtmlFromMarkdown(req['content'])

    response = requests.post(MODIFY_POST_API, data=req)
    print(response.text)
    return response

def getCategories():
    req = {
        'access_token': UserInfo.get_access_token(),
        'blogName': UserInfo.get_blog_name(),
        'output':'json'
    }

    response = requests.get(GET_CATEGORIES_API, params=req)
    return response

def getAccessToken():
    params = 'client_id={client_id}&client_secret={client_secret}&redirect_uri={redirect_uri}&response_type={response_type}'.format(
        client_id=UserInfo.get_client_id(),
        client_secret=UserInfo.get_client_secret(),
        redirect_uri=CALLBACK_URL,
        response_type='code'
    )
    
    CallBackServer.run(processToken)
    authorize_url = CODE_URL+'?'+params
    webbrowser.open(authorize_url)


getAccessToken()