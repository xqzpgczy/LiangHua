# -*- coding: utf-8 -*-
"""User models."""
import datetime as dt

from app.database import (
    Column,
    Model,
    SurrogatePK,
    db,
    reference_col,
    relationship,
)
from app.extensions import bcrypt


class Plan(SurrogatePK, Model):
    id = Column(db.Integer, primary_key=True)
    name = Column(db.String(80), nullable=False)
    top = Column(db.Float)  # 价格顶部
    bottom = Column(db.Float)  # 价格底部
    buy_start = Column(db.Float)  # 起始买入价格
    sell_start = Column(db.Float)  # 起始卖出价格
    top_share = Column(db.Float)  # 初始额度
    increase_rate = Column(db.Float)  # 仓位递增率
    reduce_rate = Column(db.Float)  # 价格递减率




