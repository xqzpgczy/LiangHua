

def func():
    top = 10
    start = 7
    price = []
    rate = 0.95

    share_number = 0  # 总数

    per_fund = 10000
    money_conut = 0

    data = []

    for i in range(1, 8):
        k = round(start * (rate**i), 2)
        price.append(k)

    start_share = per_fund * 3 // (start*100) * 100
    data.append([start, start_share])

    print(price)

    for i in price:
        _share = per_fund // (i * 100) * 100
        data.append([i, _share])

    # 计算均价
    for i in data:
        share_number += i[1]
        money_conut += i[0]*i[1]

    price_end = price[-1]

    price_ave = round(money_conut/share_number, 2)
    total_decline = round(1- price[-1]/top, 2)
    decline = round(1 - price[-1] / price_ave, 2)

    rise = round(top*0.9/price_ave-1, 2)

    print(money_conut)
    print(f"从顶部{top}下跌{total_decline}到{price_end}.  从均价{price_ave}下跌{decline}到{price_end}, 从均价{price_ave}到顶部{top}，最高涨幅{rise}")


# func()

print(57+33+71+71)

# length = 8
#
# if length <= 8:
#     print("密码太简单")
