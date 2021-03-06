from __future__ import division
import operator
from flask import (Blueprint, request, render_template, flash, g, session,
    redirect, url_for, json, jsonify, current_app)
from flask.ext.login import (login_user, logout_user, current_user)
from flask.ext.principal import Identity, AnonymousIdentity, identity_changed

from sqlalchemy import create_engine
from sqlalchemy.sql import select, func, and_
from sqlalchemy.sql.expression import tuple_

from app import db
from config import SQLALCHEMY_DATABASE_URI
from app.users.models import Users, Roles
from app.census.datahelpers import build_table

mod = Blueprint('census', __name__, url_prefix='/census')


@mod.before_request
def before_request():
    g.conn = create_engine(SQLALCHEMY_DATABASE_URI)
    g.t = None
    g.t = build_table('census')


@mod.route('', methods=['GET', ])
def census():
    income_districts = []
    poverty_districts = []
    medianincome_districts = []
    s = select(
        [
            g.t.c.district,
        ], g.t.c.type == 'INCOME').distinct().order_by(
                g.t.c.district)
    districts = g.conn.execute(s).fetchall()
    for district in districts:
        income_districts.append(district)
    s = select(
        [
            g.t.c.district,
        ], g.t.c.type == 'POVERTY').distinct().order_by(
                g.t.c.district)
    districts = g.conn.execute(s).fetchall()
    for district in districts:
        poverty_districts.append(district)
    s = select(
        [
            g.t.c.district,
        ], g.t.c.type == 'MEDIANINCOME').distinct().order_by(
                g.t.c.district)
    districts = g.conn.execute(s).fetchall()
    for district in districts:
        medianincome_districts.append(district)
    
    return render_template('census/index.html', income_districts=income_districts, poverty_districts=poverty_districts, medianincome_districts=medianincome_districts)


@mod.route('/test', methods=['GET', ])
def census_test():
    values = {}
    s = select(
        [
            g.t.c.type,
            g.t.c.district,
            g.t.c.race,
            g.t.c.factor,
            func.sum(g.t.c.value).label('summed')
        ], g.t.c.race != 'ALL').group_by(
            g.t.c.type,
            g.t.c.district,
            g.t.c.race,
            g.t.c.factor).order_by(
                g.t.c.type,
                g.t.c.district,
                g.t.c.race,
                g.t.c.factor)
    results = g.conn.execute(s).fetchall()
    for result in results:
        type = getattr(result, 'type')
        if not values.get(type):
            values[type] = {}
        district = getattr(result, 'district')
        if not values[type].get(district):
            values[type][district] = {}
        race = getattr(result, 'race')
        if not values[type][district].get(race):
            if getattr(result, 'summed'):
                values[type][district][race] = {}
        if getattr(result, 'summed'):
            values[type][district][race] = getattr(result, 'summed')

    return render_template('census/test.html', values=values)


@mod.route('/poverty_json', methods=['GET', ])
def census_poverty_json():
    values = {}
    s = select(
        [
            g.t.c.race,
            g.t.c.factor,
            func.sum(g.t.c.value).label('summed')
        ], ).where(and_(
            g.t.c.type == 'POVERTY',
            g.t.c.value != 0)).group_by(
                g.t.c.race,
                g.t.c.factor).order_by(
                    g.t.c.race,
                    g.t.c.factor)
    results = g.conn.execute(s).fetchall()
    for value in results:
        race = getattr(value, 'race')
        if not values.get(race):
            values[race] = {}
        factor = getattr(value, 'factor')
        values[race][factor] = value.summed

    bad_keys = []
    for key in values:
        if values[key].get('POVERTY'):
            if values[key].get('ALL'):
                values[key]['percent'] = round((values[key]['POVERTY'] / values[key]['ALL']) * 100, 2)
                values[key]['percent_pov_pop'] = round((values[key]['POVERTY'] / values['ALL']['POVERTY']) * 100, 2)
                values[key]['percent_pop'] = round((values[key]['ALL'] / values['ALL']['ALL']) * 100, 2)
        else:
            if not values[key].get('percent'):
                bad_keys.append(key)

    if bad_keys:
        for key in bad_keys:
            values.pop(key, None)
            values.pop('ALL', None)
    values = sorted(values.items(), key=operator.itemgetter(1), reverse=True)

    return_val = {
        'values': values,
        'graph_name': 'Poverty % by Race in All Districts',
        'url': url_for('census.census_poverty_json', _external=True)
    }
    return jsonify(return_val)


@mod.route('/poverty', methods=['GET', ])
def census_proverty():
    values = {}
    s = select(
        [
            g.t.c.race,
            g.t.c.factor,
            func.sum(g.t.c.value).label('summed')
        ], ).where(and_(
            g.t.c.type == 'POVERTY',
            g.t.c.value != 0)).group_by(
                g.t.c.race,
                g.t.c.factor).order_by(
                    g.t.c.race,
                    g.t.c.factor)
    results = g.conn.execute(s).fetchall()
    for value in results:
        race = getattr(value, 'race')
        if not values.get(race):
            values[race] = {}
        factor = getattr(value, 'factor')
        values[race][factor] = value.summed

    bad_keys = []
    for key in values:
        if values[key].get('POVERTY'):
            if values[key].get('ALL'):
                values[key]['percent'] = round((values[key]['POVERTY'] / values[key]['ALL']) * 100, 2)
                values[key]['percent_pov_pop'] = round((values[key]['POVERTY'] / values['ALL']['POVERTY']) * 100, 2)
                values[key]['percent_pop'] = round((values[key]['ALL'] / values['ALL']['ALL']) * 100, 2)
        else:
            if not values[key].get('percent'):
                bad_keys.append(key)

    if bad_keys:
        for key in bad_keys:
            values.pop(key, None)
            values.pop('ALL', None)
    values = sorted(values.items(), key=operator.itemgetter(1), reverse=True)

    return render_template('census/poverty.html', values=values)


@mod.route('/poverty_by_district/<district_name>', methods=['GET', ])
def census_proverty_by_district(district_name):
    values = {}
    s = select(
        [
            g.t.c.race,
            g.t.c.factor,
            func.sum(g.t.c.value).label('summed')
        ], ).where(and_(
            g.t.c.type == 'POVERTY',
            g.t.c.district == district_name,
            g.t.c.value != 0)).group_by(
                g.t.c.race,
                g.t.c.factor).order_by(
                    g.t.c.race,
                    g.t.c.factor)
    results = g.conn.execute(s).fetchall()
    for value in results:
        race = getattr(value, 'race')
        if not values.get(race):
            values[race] = {}
        factor = getattr(value, 'factor')
        values[race][factor] = value.summed

    bad_keys = []
    for key in values:
        if values[key].get('POVERTY'):
            if values[key].get('ALL'):
                values[key]['percent'] = round((values[key]['POVERTY'] / values[key]['ALL']) * 100, 2)
                values[key]['percent_pov_pop'] = round((values[key]['POVERTY'] / values['ALL']['POVERTY']) * 100, 2)
                values[key]['percent_pop'] = round((values[key]['ALL'] / values['ALL']['ALL']) * 100, 2)
        else:
            if not values[key].get('percent'):
                bad_keys.append(key)

    if bad_keys:
        for key in bad_keys:
            values.pop(key, None)
            values.pop('ALL', None)
    values = sorted(values.items(), key=operator.itemgetter(1), reverse=True)

    return render_template('census/poverty_by_district.html', values=values, district=district_name)


@mod.route('/income_by_district/<district_name>', methods=['GET', ])
def census_income_by_district(district_name):
    values = {}
    s = select(
        [
            g.t.c.race,
            g.t.c.factor,
            func.sum(g.t.c.value).label('summed')
        ], ).where(
            and_(
                g.t.c.type == 'INCOME',
                g.t.c.district == district_name,
                g.t.c.value != 0,
                g.t.c.race == 'ALL',
            )
        ).group_by(
            g.t.c.race,
            g.t.c.factor).order_by(
                g.t.c.race,
                g.t.c.factor)
    results = g.conn.execute(s).fetchall()
    total_value = 0
    for value in results:
        total_value = total_value + getattr(value, 'summed')
        factor = getattr(value, 'factor')
        values[factor] = {'count': value.summed}

    for key in values:
        if total_value > 0:
                values[key]['percent'] = round((values[key]['count'] / values['ALL']['count']) * 100, 2)
    values.pop('ALL', None)
    values = sorted(values.items(), key=operator.itemgetter(1), reverse=True)

    return render_template('census/income_by_district.html', values=values, district=district_name)


@mod.route('/income', methods=['GET', ])
def census_income():
    values = {}
    s = select(
        [
            g.t.c.race,
            g.t.c.factor,
            func.sum(g.t.c.value).label('summed')
        ], ).where(
            and_(
                g.t.c.type == 'INCOME',
                g.t.c.value != 0,
                g.t.c.race == 'ALL',
            )
        ).group_by(
            g.t.c.race,
            g.t.c.factor).order_by(
                g.t.c.race,
                g.t.c.factor)
    results = g.conn.execute(s).fetchall()
    total_value = 0
    for value in results:
        total_value = total_value + getattr(value, 'summed')
        factor = getattr(value, 'factor')
        values[factor] = {'count': value.summed}

    for key in values:
        print
        if total_value > 0:
                values[key]['percent'] = round((values[key]['count'] / values['ALL']['count']) * 100, 2)
    values.pop('ALL', None)
    values = sorted(values.items(), key=operator.itemgetter(1), reverse=True)

    return render_template('census/income.html', values=values)

@mod.route('/income_json', methods=['GET', ])
def census_income_json():
    values = {}
    s = select(
        [
            g.t.c.race,
            g.t.c.factor,
            func.sum(g.t.c.value).label('summed')
        ], ).where(
            and_(
                g.t.c.type == 'INCOME',
                g.t.c.value != 0,
                g.t.c.race == 'ALL',
            )
        ).group_by(
            g.t.c.race,
            g.t.c.factor).order_by(
                g.t.c.race,
                g.t.c.factor)
    results = g.conn.execute(s).fetchall()
    total_value = 0
    for value in results:
        total_value = total_value + getattr(value, 'summed')
        factor = getattr(value, 'factor')
        values[factor] = {'count': value.summed}

    for key in values:
        print
        if total_value > 0:
                values[key]['percent'] = round((values[key]['count'] / values['ALL']['count']) * 100, 2)
    values.pop('ALL', None)
    values = sorted(values.items(), key=operator.itemgetter(1), reverse=True)
    return_val = {
        'values': values,
        'graph_name': 'Poverty % by Race in All Districts',
        'url': url_for('census.census_income_json', _external=True)
    }

    return jsonify(return_val)


@mod.route('/medianincome', methods=['GET', ])
def census_medianincome():
    values = {}
    s = select(
        [
            g.t.c.race,
            g.t.c.factor,
            func.sum(g.t.c.value).label('summed')
        ], ).where(
            and_(
                g.t.c.type == 'MEDIANINCOME',
                g.t.c.value != 0,
                g.t.c.race != 'WHITE',
            )
        ).group_by(
            g.t.c.race,
            g.t.c.factor).order_by(
                g.t.c.race,
                g.t.c.factor)
    results = g.conn.execute(s).fetchall()
    total_value = 0
    for value in results:
        median_income = round(total_value + getattr(value, 'summed')/len(results),2)
        race = getattr(value, 'race')
        if not values.get(race):
            values[race] = {}
        factor = getattr(value, 'factor')
        if not values[race].get(factor):
            values[race][factor] = {}
        values[race][factor] = median_income

    values.pop('ALL', None)
    values = sorted(values.items(), key=operator.itemgetter(1), reverse=True)
    print values

    return render_template('census/medianincome.html', values=values)


@mod.route('/medianincome_by_district/<district_name>', methods=['GET', ])
def census_medianincome_by_district(district_name):
    values = {}
    s = select(
        [
            g.t.c.race,
            g.t.c.factor,
            func.sum(g.t.c.value).label('summed')
        ], ).where(
            and_(
                g.t.c.type == 'MEDIANINCOME',
                g.t.c.district == district_name,
                g.t.c.value != 0,
                g.t.c.race != 'WHITE',
            )
        ).group_by(
            g.t.c.race,
            g.t.c.factor).order_by(
                g.t.c.race,
                g.t.c.factor)
    results = g.conn.execute(s).fetchall()
    total_value = 0
    for value in results:
        median_income = round(total_value + getattr(value, 'summed') / len(results),2)
        race = getattr(value, 'race')
        if not values.get(race):
            values[race] = {}
        factor = getattr(value, 'factor')
        if not values[race].get(factor):
            values[race][factor] = {}
        values[race][factor] = median_income

    values.pop('ALL', None)
    values = sorted(values.items(), key=operator.itemgetter(1), reverse=True)
    print values

    return render_template('census/medianincome_by_district.html', values=values, district=district_name)


@mod.route('/occupation_bygender', methods=['GET', ])
def census_occupation_bygender():
    values = {}
    s = select(
        [
            g.t.c.factor,
            g.t.c.sex,
            func.sum(g.t.c.value).label('summed')
        ], ).where(
            and_(
                g.t.c.type == 'OCC',
                g.t.c.value != 0,
                g.t.c.race != 'WHITE',
            )
        ).group_by(
            g.t.c.factor,
            g.t.c.sex
            ).order_by(
                g.t.c.sex,
                g.t.c.factor)
    results = g.conn.execute(s).fetchall()
    for value in results:
        factor = getattr(value, 'factor')
        if not values.get(factor):
            values[factor] = {}
        sex = getattr(value, 'sex')
        if not values[factor].get(sex):
            values[factor][sex] = {}
        values[factor][sex] = getattr(value, 'summed')

    values.pop('ALL', None)
    values = sorted(values.items(), key=operator.itemgetter(1), reverse=True)
    print values

    return render_template('census/occupation_bygender.html', values=values)


@mod.route('/occupation_bygender_bydistrict/<district_name>', methods=['GET', ])
def census_occupation_bygender_by_district(district_name):
    values = {}
    s = select(
        [
            g.t.c.factor,
            g.t.c.sex,
            func.sum(g.t.c.value).label('summed')
        ], ).where(
            and_(
                g.t.c.type == 'OCC',
                g.t.c.district == district_name,
                g.t.c.value != 0,
                g.t.c.race != 'WHITE',
            )
        ).group_by(
            g.t.c.factor,
            g.t.c.sex
            ).order_by(
                g.t.c.sex,
                g.t.c.factor)
    results = g.conn.execute(s).fetchall()
    for value in results:
        factor = getattr(value, 'factor')
        if not values.get(factor):
            values[factor] = {}
        sex = getattr(value, 'sex')
        if not values[factor].get(sex):
            values[factor][sex] = {}
        values[factor][sex] = getattr(value, 'summed')

    values.pop('ALL', None)
    values = sorted(values.items(), key=operator.itemgetter(1), reverse=True)
    print values

    return render_template('census/occupation_bygender.html', values=values, district=district_name)

@mod.route('/education_bygender', methods=['GET', ])
def census_education_bygender():
    values = {}
    s = select(
        [
            g.t.c.factor,
            g.t.c.sex,
            func.sum(g.t.c.value).label('summed')
        ], ).where(
            and_(
                g.t.c.type == 'EDU',
                g.t.c.value != 0,
                g.t.c.race != 'WHITE',
            )
        ).group_by(
            g.t.c.factor,
            g.t.c.sex
            ).order_by(
                g.t.c.sex,
                g.t.c.factor)
    results = g.conn.execute(s).fetchall()
    for value in results:
        factor = getattr(value, 'factor')
        if not values.get(factor):
            values[factor] = {}
        sex = getattr(value, 'sex')
        if not values[factor].get(sex):
            values[factor][sex] = {}
        values[factor][sex] = getattr(value, 'summed')

    values.pop('ALL', None)
    values = sorted(values.items(), key=operator.itemgetter(1), reverse=True)

    return render_template('census/education_bygender.html', values=values)


@mod.route('/education_bygender_bydistrict/<district_name>', methods=['GET', ])
def census_education_bygender_by_district(district_name):
    values = {}
    s = select(
        [
            g.t.c.factor,
            g.t.c.sex,
            func.sum(g.t.c.value).label('summed')
        ], ).where(
            and_(
                g.t.c.type == 'EDU',
                g.t.c.district == district_name,
                g.t.c.value != 0,
                g.t.c.race != 'WHITE',
            )
        ).group_by(
            g.t.c.factor,
            g.t.c.sex
            ).order_by(
                g.t.c.sex,
                g.t.c.factor)
    results = g.conn.execute(s).fetchall()
    for value in results:
        factor = getattr(value, 'factor')
        if not values.get(factor):
            values[factor] = {}
        sex = getattr(value, 'sex')
        if not values[factor].get(sex):
            values[factor][sex] = {}
        values[factor][sex] = getattr(value, 'summed')

    values.pop('ALL', None)
    values = sorted(values.items(), key=operator.itemgetter(1), reverse=True)

    return render_template('census/education_bygender.html', values=values, district=district_name)
