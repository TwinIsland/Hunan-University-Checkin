import pickle
import time
import checkin
import signIn
import json
import usrLib
import os
import eventRec

Students = usrLib.Students()
isShowStatus = json.loads(open("config.json", "r").read())['showStatus']

for sId in Students.get_sId_list():
    print("=================")
    print("(-) 正在检测：" + sId + "...")
    eventRec.rec_msg("START CHECKING IN: " + sId)
    if not os.path.exists(usrLib.get_cookies_address(sId)):
        cookies = []
    else:
        with open(usrLib.get_cookies_address(sId), 'rb+', ) as pkl:
            cookies = pickle.load(pkl)

    curTime = int(time.time())
    expTime = 0
    for i in cookies:
        if i.name == "TOKEN":
            expTime = int(i.expires)

    if curTime >= expTime:
        print("(-) Cookie 已过期，正在更新中...")
        print("-----------------\nSTART ATTEMPT")
        try:
            signIn.make_cookies(usr={
                "code": sId,
                "pwd": Students.get_pwd_by_id(sId)
            })
            with open(usrLib.get_cookies_address(sId), 'rb+', ) as pkl:
                cookies = pickle.load(pkl)
        except Exception as e:
            eventRec.fail_msg(sId, str(e))
            print("(x) Cookie Error: " + sId + " --- " + str(e))
            eventRec.rec_msg("FINISH CHECKING IN: " + sId)
            continue
    else:
        print("(√) Cookie 已经是最新状态")

    try:
        status = checkin.checkin(cookies)
    except Exception as e:
        eventRec.fail_msg(sId, str(e))
        print("(x) Checkin Error: " + sId + " --- " + str(e) + "\n")
        eventRec.rec_msg("FINISH CHECKING IN: " + sId)
        continue

    if isShowStatus:
        try:
            print(checkin.print_cur_status(cookies))
        except Exception as e:
            eventRec.fail_msg(sId, str(e))
            print("(x) Get Inf Error: " + sId + " --- " + str(e) + "\n")

    eventRec.rec_msg("FINISH CHECKING IN: " + sId)
