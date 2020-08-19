# -*- coding: utf-8 -*-
"""plan views."""
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required
from app.utils import flash_errors

blueprint = Blueprint("plan", __name__, url_prefix="/plan", static_folder="../static")


@blueprint.route("/")
@login_required
def index():
    """List members."""
    return render_template("plan/members.html")


from app.forms.plan import PlanForm
from app.services.PlanServices_2 import PlanServices
from app.services.ScreenServices import ScreenServices
from app.models.plan import Plan


@blueprint.route("/ergodic", methods=["GET", "POST"])
@login_required
def ergodic():
    """List members."""
    form = PlanForm(request.form)
    infos = []
    if form.validate_on_submit():
        screen = ScreenServices(form)
        infos = screen.run()
    else:
        flash_errors(form)
    return render_template("plan/ergodic.html", form=form, infos=infos)


@blueprint.route("/plan_test", methods=["GET", "POST"])
def plan_test():

    """
    <float:top>/<float:bottom>/<float:buy_start>/<float:sell_start>/<float:top_share>/<float:increase_rate>/<float:reduce_rate>
    """
    form = PlanForm(request.form)
    form.id.data = int(request.args.get("id"))
    form.name.data = request.args.get("name")
    form.top.data = float(request.args.get("top"))
    form.bottom.data = float(request.args.get("bottom"))
    form.buy_start.data = float(request.args.get("buy_start"))
    form.sell_start.data = float(request.args.get("sell_start"))
    form.top_share.data = float(request.args.get("top_share"))
    form.increase_rate.data = float(request.args.get("increase_rate"))
    form.reduce_rate.data = float(request.args.get("reduce_rate"))
    plan = PlanServices(form.top.data, form.bottom.data, form.buy_start.data, form.sell_start.data,
                        form.top_share.data, form.increase_rate.data, form.reduce_rate.data)
    plan.run()

    return render_template("plan/info.html", form=form, plan=plan)


@blueprint.route("/info/<int:_id>", methods=["GET", "POST"])
def info(_id):

    form = PlanForm(request.form)
    if request.method == "POST":
        if form.validate_on_submit():

            PlanServices.save_plan_mode(form)

            plan = PlanServices(form.top.data, form.bottom.data, form.buy_start.data, form.sell_start.data,
                                form.top_share.data,
                                form.increase_rate.data, form.reduce_rate.data)
            plan.run()
        else:
            flash_errors(form)
            plan = None
        return render_template("plan/info.html", form=form, plan=plan)
    else:
        model = Plan.query.filter_by(id=_id).first()
        if model:
            form.id.data = model.id
            form.name.data = model.name
            form.top.data = model.top
            form.bottom.data = model.bottom
            form.buy_start.data = model.buy_start
            form.sell_start.data = model.sell_start
            form.top_share.data = model.top_share
            form.increase_rate.data = model.increase_rate
            form.reduce_rate.data = model.reduce_rate
            plan = PlanServices(form.top.data, form.bottom.data, form.buy_start.data, form.sell_start.data,
                                form.top_share.data, form.increase_rate.data, form.reduce_rate.data)
            plan.run()
        else:
            plan = None
    return render_template("plan/info.html", form=form, plan=plan)
