import time


def get_time():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


def fail_msg(sId=" ", msg="UNKNOWN"):
    file = open("EVENT.TXT", 'a+')
    file.write("[X] sId: " + str(sId) + " --- " + msg + "    " + get_time() + "\n")
    file.close()


def ok_msg(sId=" ", msg="UNKNOWN"):
    file = open("EVENT.TXT", 'a+')
    file.write("[√] sId: " + str(sId) + " --- " + msg + "    " + get_time() + "\n")
    file.close()


def rec_msg(msg=" "):
    file = open("EVENT.TXT", 'a+')
    file.write("[-] " + msg + "    " + get_time() + "\n")
    file.close()
