import bisect
from app.services.PlanServices_2 import PlanServices

class ScreenServices:
    """
    筛选策略
    """
    def __init__(self, form):
        self.check_date(form)

    def get_x(self):

        resp = []
        for x in range(100, 300):
            if not self._cmp(x, self.increase_rate, self.compare_increase_rate):
                continue
            resp.append(x)
        return resp

    def get_y(self):
        resp = []
        for y in range(0, 1000):
            if not self._cmp(y, self.reduce_rate, self.compare_reduce_rate):
                continue
            resp.append(y)
        return resp

    def run(self):

        resp = []
        stop_y = {}

        _x = self.get_x()
        _y = self.get_y()
        _x_stop = False
        _y_0 = _y[0]

        sort_int = []

        for x in _x:
            if _x_stop:
                break
            for y in _y:

                if x in stop_y and y > stop_y[x]:  # 当 x  恒定    y  和最大值比较
                    break

                if not self._cmp(y, self.reduce_rate, self.compare_reduce_rate):
                    continue

                try:
                    plan = self._run_plan(x / 100, y / 1000)
                except BaseException as e:
                    print(e)
                    continue
                if not self._cmp(plan.count_amount, self.count_amount, self.compare_count_amount):
                    if y == _y_0:
                        _x_stop = True
                        continue

                    if x not in stop_y:
                        stop_y[x] = y
                    continue

                if self._cmp(plan.profit_rate, self.profit_rate, self.compare_profit_rate):
                    # _info = f'''总资金：{round(plan.count_amount / 10000, 3)}万   股数增长比:{plan.increase_rate}
                    #         价格下降比:{plan.reduce_rate}
                    #         总层数：{len(plan.plan_info)} 初始仓位比{plan.initial_position}
                    #        最高价格: {plan.sell_top_price} 增长：{round(plan.profit_rate * 100, 1)}%'''

                    _info = {"count_amount": round(plan.count_amount / 10000, 3), "increase_rate": plan.increase_rate,
                             "reduce_rate": plan.reduce_rate, "initial_position": plan.initial_position,
                             "cell": len(plan.plan_info), "sell_top_price": plan.sell_top_price,
                             "profit_rate": round(plan.profit_rate * 100, 1)
                             }


                    # resp.append(_info)

                    sort_k = plan.profit_rate
                    k = bisect.bisect(sort_int,sort_k)
                    sort_int.insert(k, sort_k)
                    resp.insert(k, _info)

        return resp[::-1]

    def _cmp(self, a, b, cop):
        '''
        简单说下这几个函数的意思吧。
        lt(a, b) 相当于 a < b
        le(a,b) 相当于 a <= b
        eq(a,b) 相当于 a == b
        ne(a,b) 相当于 a != b
        gt(a,b) 相当于 a > b
        ge(a, b)相当于 a>= b
        '''
        a = float(a)
        b = float(b)

        if cop == "<":
            return a < b
        if cop == "<=":
            return a <= b
        if cop == "=":
            return a == b
        if cop == "!=":
            return a != b
        if cop == ">":
            return a > b
        if cop == ">=":
            return a >= b

    def check_date(self, form):
        self.name = form.name.data
        self.top = form.top.data
        self.bottom = form.bottom.data
        self.buy_start = form.buy_start.data
        self.sell_start = form.sell_start.data
        self.top_share = form.top_share.data
        self.increase_rate = form.increase_rate.data*100
        self.reduce_rate = form.reduce_rate.data * 1000
        self.profit_rate = form.profit_rate.data/100
        self.count_amount = form.count_amount.data * 10000

        # self.compare_increase_rate = form.compare_increase_rate.data
        # self.compare_reduce_rate = form.compare_reduce_rate.data
        # self.compare_profit_rate = form.compare_profit_rate.data
        # self.compare_count_amount = form.compare_count_amount.data

        self.compare_increase_rate = ">="
        self.compare_reduce_rate = ">="
        self.compare_profit_rate = ">="
        self.compare_count_amount = "<="

    def _run_plan(self, increase, reduce):
        plan = PlanServices(self.top, self.bottom, self.buy_start, self.sell_start, self.top_share, increase, reduce)
        plan.run()
        return plan