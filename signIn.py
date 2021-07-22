import time
import requests as re
import pytesseract
from PIL import Image
import io
import json
import pickle
import eventRec

cookieAtp = json.loads(open("config.json", "r").read())['getCookieAttempt'] + 1


def get_ver(image):
    text = str(pytesseract.image_to_string(image, config='-c tessedit_char_whitelist=0123456789'))[:4]
    return text


def make_postData(usr):
    """
    usr is a dict:
    {
     code: student's account
     pwd: password
     }
    """
    token = eval(re.get("https://fangkong.hnu.edu.cn/api/v1/account/getimgvcode").content.decode('utf-8'))['data'][
        'Token']
    verCode = get_ver(Image.open(io.BytesIO(re.get("https://fangkong.hnu.edu.cn/imagevcode?token=" + token).content)))

    return {
        "Code": usr['code'],
        "Password": usr['pwd'],
        "Token": token,
        "VerCode": verCode,
        "WechatUserinfoCode": None
    }


def make_cookies(usr):
    tryCount = 0
    while True:
        tryCount += 1
        HTML = re.post("https://fangkong.hnu.edu.cn/api/v1/account/login", data=make_postData(usr))
        loginStat = json.loads(
            HTML.content.decode('utf-8'))
        if loginStat['code'] == 0:
            print("-----------------")
            print("(√) " + usr["code"] + "登录成功!")
            loginStat = loginStat['data']
            break
        elif tryCount >= cookieAtp:
            raise Exception("try too much times")
        time.sleep(0.05)
        print("(-) ATTEMPT: " + str(tryCount) + " --- " + loginStat['msg'])

    with open("UsrLib/" + loginStat['Code'] + '.pkl', 'wb') as pkl:
        pickle.dump(HTML.cookies, pkl)
    pkl.close()
    eventRec.ok_msg(usr["code"], "build cookie successfully")
    print("(√) 已建立：" + loginStat["Name"] + " 的Cookie档案")
