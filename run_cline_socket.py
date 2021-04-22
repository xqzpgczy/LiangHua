# -*- coding: utf-8 -*-

import socket, sqlite3, time, requests
from log import logger


def get_config():
    conn = sqlite3.connect('./data.sqlite')
    c = conn.cursor()
    cursor = c.execute('SELECT IP_address, IP_port FROM "config" WHERE is_use = 1')
    data = [[i for i in row] for row in cursor]
    IP_address = data[0][0]
    IP_port = int( data[0][1])

    #logger.info(f"获取配置信息， socket 请求地址：{IP_address}:{IP_port}")
    conn.close()
    return IP_address, IP_port


def func(data):
    data = data.split('!')[0]
    data = data.strip('\n')
    _d = data.split('@')

    k1 = _d[0][1:]
    k2 = _d[1]
    k3 = _d[2]
    k4 = _d[3]

    url = f'http://127.0.0.1/csv/{k2}/{k3}/{k4}/{k1}'
    resp = requests.get(url=url)
    resp = resp.content.decode('unicode_escape')
    logger.info(f"request web function work: {resp}")



def socket_cline():
    ip_address, ip_port = get_config()
    # ip_address, ip_port = "127.0.0.1", 20000
    print(ip_address, ip_port)

    with socket.socket() as s:
        # s.settimeout(100)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
        print(f"try connect socket service {ip_address}:{ip_port}")
        s.connect((ip_address, ip_port))

        while True:
            # 一. 接受 socket 数据
            data = s.recv(1024)
            data = data.decode(encoding="utf-8")  # '#13@2@12@1!   #13@2@12@1!' => {}
            if data:
                print(f"-------------- socket sent data:{data} \n")
            if data and "@" in data:
                func(data)
                print(data)


def run_cline_socket(F=False):
    print(" socket work -------------- 启动", )
    while True:
        time.sleep(1)

        try:
            socket_cline()
            print("connect  socket service Success")
        except BaseException as e:
            print(e)
            pass
        if F:
            break


