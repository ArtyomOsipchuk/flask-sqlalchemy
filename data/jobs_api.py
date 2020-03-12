from flask import jsonify, Blueprint, request

from data import db_session
from .jobs import Jobs

blueprint = Blueprint('news_api', __name__,
                      template_folder='templates')


@blueprint.route('/api/jobs/')
def get_jobs():
    session = db_session.create_session()
    jobs = session.query(Jobs).all()
    return jsonify(
        {'news':
             [item.to_dict(only=('id', 'job',
                                 'work_size',
                                 'collaborators',
                                 'team_leader',
                                 'start_date',
                                 'end_date',
                                 'is_finished',
                                 'category'))
              for item in jobs]})