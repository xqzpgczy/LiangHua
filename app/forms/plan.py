# -*- coding: utf-8 -*-
"""Public forms."""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, IntegerField
from wtforms.validators import DataRequired, Email, EqualTo, Length
from wtforms.validators import DataRequired


class PlanForm(FlaskForm):
    id = IntegerField("id")
    name = StringField("名称", validators=[DataRequired()])
    top = FloatField("价格顶部", validators=[DataRequired()])
    bottom = FloatField("价格底部", validators=[DataRequired()])
    buy_start = FloatField("起始买入价", validators=[DataRequired()])
    sell_start = FloatField("起始卖出价", validators=[DataRequired()])
    top_share = FloatField("起始股数", validators=[DataRequired()])
    increase_rate = FloatField("增长率", validators=[DataRequired()])
    reduce_rate = FloatField("减少率", validators=[DataRequired()])
    profit_rate = FloatField("利润率")
    count_amount = FloatField("总资金")

    # compare_increase_rate = StringField("股数增长率比较符")
    # compare_reduce_rate = StringField("价格下降比较符")
    # compare_profit_rate = StringField("利润率比较符")
    # compare_count_amount = StringField("总资金比较符")

    def __init__(self, *args, **kwargs):
        """Create instance."""
        super(PlanForm, self).__init__(*args, **kwargs)

    def validate(self):
        """Validate the form."""
        initial_validation = super(PlanForm, self).validate()
        if not initial_validation:
            return False

        if self.reduce_rate.data > 100 or self.reduce_rate.data < 0:
            self.reduce_rate.errors.append("价格递减只允许输入1 到100的%比数字")
            return False

        if self.increase_rate.data < 0:
            self.reduce_rate.errors.append("股数递增只允许输入正数")
            return False

        return True
