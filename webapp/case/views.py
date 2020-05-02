from flask import Blueprint, render_template, abort

from webapp.db import db
from webapp.dashboard.models import Case

blueprint = Blueprint('case', __name__)


@blueprint.route("/case/<int:case_id>")
def case_information(case_id):
    content = {
        'case': Case.query.filter(Case.id == case_id).first()
    }
    if not content['case']:
        abort(404)
    return f"<p>Учетная карта судебного дела: {content['case'].number_case}</p>"
    # return render_template('case/index.html', **content)


@blueprint.route("/case/add")
def add_case():
    return 'Добавить новое дело'
