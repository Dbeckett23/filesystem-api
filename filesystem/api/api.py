"""REST API for Filesystem."""
import flask
import filesystem


@filesystem.app.route('/api/v1/', methods=["GET"])
def api():
    """Return a list of available services."""
    context = {
        "url": flask.request.path,
    }
    return flask.jsonify(**context)