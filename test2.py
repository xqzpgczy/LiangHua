# from app.app import create_app
# from app.models.users import User
#
#
# app = create_app()
# with app.app_context():
#
#     model = User.query.get(1).role
#
#     print(model.name)


# hous = 2000
# food = 2000
# other = 1000
# year_money = (hous + food + other)*12
#
# rate = 0.07
# aroumn = year_money / rate
#
# print(aroumn)

worke = 20
rate = 0.20
amound = 80

print(f"起始资金{amound}, 工资年盈余{worke},收益率{int((rate*100))}%")

for n in range(30):
    expenditure = 0
    # if n < 5:
    #     expenditure = 0 # 年开支
    # else:
    #     expenditure = 30

    y_savings = worke-expenditure  # 年储蓄

    rate_money = round(amound * rate, 2)
    amound = round(amound + rate_money + y_savings, 2)

    y_income = int(rate_money + y_savings)

    #     print(amound)
    # print(y+n, amound, rate_money, round(rate_money+worke, 2), round(worke / (rate_money+worke), 2))
    print(f"第{n+1}年结束, 资金总量达到{amound},总收入{y_income} ,资本收入{rate_money}, 储蓄{y_savings}, 工资/收入{int(worke / (rate_money+worke)*100)}%")


























