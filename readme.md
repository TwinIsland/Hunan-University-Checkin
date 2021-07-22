# CheckinAssistant

湖南大学打卡签到脚本，适用于https://fangkong.hnu.edu.cn/app/

### features

1. 可批量签到
2. 自定义检测参数

### package

1. `pytesseract`
2. `PIL`
3. `requests`

### config

> 配置文件

```json
//config.json
{
  "getCookieAttempt": 15 --> 尝试设置cookie最大次数
  "checkinAttempt": 10, --> 尝试签到最大次数
  "showStatus": true --> 是否显示学校打卡情况
}
```

```json
//UsrLib/Usr.json
{
  "xxxx": { --> 用户名
    "pwd": "xxxx" --> 密码
  }, 
  "sample": { --> 用户2
    "pwd": "123456" -->用户2密码
  }
}
```

>*你也可以通过运行`usrControl.py`来更改用户信息*

### run

```bash
python multiCheckin.py
```

*p.s. 如果打算每天定时打卡或者是每隔一段时间检测打卡情况写一个批处理就行了*

### debug

脚本自带一个事件记录模块，如果出现bug首先考虑查看`EVENT.TXT`文件排查错误

### other

传播脚本之前请务必记得删除`UserLib`里的`pkl`文件、`EVENT.TXT`并通过`usrControl.py`**删除所有用户信息！！**



*Project By TwIsland, 2021/7/15*

