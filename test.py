# bottom = 52
# top = 69.5


# 计算幅度
def b_f_q_n(bottom, top):
    p1 = 0.382
    p2 = 0.618

    # 计算幅度

    for p in [p1, p2]:
        k = top - (top - bottom) * p
        print(p, k)


# 计算 风险

def f_x(s, p):
    """s = 自有资产
       p = 平仓线
    """

    q = 1  # 负债
    while True:
        start = s+q  #  自有+负债
        end = int(p*q) # 触及警戒线的总资产

        f = round(1 - end/start, 3)

        if p < 0.2:
            break

        dan_bao = int((q+s)*100/q)

        print(f"负债{q}:自有资金{s}={dan_bao}%, 剩余资产{end}/负债{q} 时 触及警戒线{int(p*100)}%  1-{end}/{start}=跌掉{round(f*100, 1)}%")

        q = q+1
        if q > 2*s:
            break


#计算通胀和风险
def f_y():
    count = 200  # 总资金
    y = 12  # 年度消耗

    r_1 = 0.10
    r_2 = 0.03

    for i in range(100):

        old = count
        new = round(count*(1+r_1), 2)
        y = round(y*(1+r_2), 2)
        count = round(new - y, 2)

        print(f"{i+1} {old} * (1+{r_1})={new}-{y} = {count}    {round(new-old-y, 2)}  ")

        if count < 0: break


def kl():
    p = 0.5  # 成功概率
    b = 0.7/0.3  # 赔率
    q = 1-p
    f = (b*p - q)/b
    print(f)






f_x(100, 1.50)

# b_f_q_n(0.5, 1.664)  # 科技50
# b_f_q_n(16.58, 28.8)
# b_f_q_n(0.835, 2.15)  # 消费50

# f_y()#计算通胀和风险
# kl()










