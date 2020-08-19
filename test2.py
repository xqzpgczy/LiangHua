#
# a = """
#     id = www
#     name = Column(db.String(80), nullable=False)
#     top = Column(db.Float)  # 价格顶部
#     bottom = Column(db.Float)  # 价格底部
#     buy_start = Column(db.Float)  # 起始买入价格
#     sell_start = Column(db.Float)  # 起始卖出价格
#     top_share = Column(db.Float)  # 初始额度
#     increase_rate = Column(db.Float)  # 仓位递增率
#     reduce_rate = Column(db.Float)  # 价格递减率
#
# """
#
# r = ""
#
# for i in a.split("\n"):
#
#     if not i:
#         continue
#     i = i.split("=")[0]
#     i = i.strip()
#     a = f'form.{i}.data = float(request.args.get("{i}"))'
#     print(a)
#
# print(r)

c = {}

date = [
    [1,2,3,4],
    [2,3,4,5]
]

for i in date:
    for k in i:
        if k in c:
            c[k] = c[k] + 1
        else:
            c[k] = 1
print(c)
