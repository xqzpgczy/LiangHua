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
    initial_quotas = Column(db.Float, unique=True, nullable=False)  # 初始额度
    price_top = Column(db.Float)  # 价格顶部
    price_bottom = Column(db.Float)  # 价格底部
    increase_rate = Column(db.Float)  # 仓位递增率
    reduce_rate = Column(db.Float)  # 价格递减率

    start_price = Column(db.Float)  # 起始价格
