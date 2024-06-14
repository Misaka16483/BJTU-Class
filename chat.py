# -*- coding: utf-8 -*-
import urllib.parse
import httpx
from PIL import Image
from io import BytesIO
import urllib
import requests
cookies={'csrftoken':'your-token','sessionid':'your-id'}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Referer': 'https://aa.bjtu.edu.cn/course_selection/courseselecttask/selects/',
    'X-Requested-With':'XMLHttpRequest'
}
client = httpx.Client(http2=True)
url='https://aa.bjtu.edu.cn/captcha/refresh/'
res=client.get(url=url,cookies=cookies,headers=headers)
json_data=res.json()
image_url='https://aa.bjtu.edu.cn'+json_data.get('image_url')
print(image_url)
res_image=client.get(url=image_url,cookies=cookies,headers=headers)
image_data=BytesIO(res_image.content)
image=Image.open(image_data)
image.show()
anwser=input() #input your captcha
post_url='https://aa.bjtu.edu.cn/course_selection/courseselecttask/selects_action/?action=submit'
headers_post={
    'Referer':'https://aa.bjtu.edu.cn/course_selection/courseselecttask/selects_action/?action=load&iframe=school',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With':'XMLHttpRequest'
}
form_data={
    'checkboxs':'142269',
    'hashkey':json_data.get('key'),
    'answer':anwser
}
encoded_data=urllib.parse.urlencode(form_data)
print(encoded_data)
res_final=client.post(url=post_url,cookies=cookies,headers=headers_post,data=encoded_data)
print(res_final.read())
cookie_get=requests.utils.dict_from_cookiejar(res_final.cookies.jar)
cookies.update(cookie_get)
url_final='https://aa.bjtu.edu.cn/course_selection/courseselecttask/selects/'
headers_final={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Referer':'https://aa.bjtu.edu.cn/course/course/'
}
Res=client.get(url=url_final,cookies=cookies,headers=headers_final)
#print(Res.read())
#print(cookies)
