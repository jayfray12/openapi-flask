from connexion.apps.flask_app import FlaskJSONEncoder
import six

from openapi_server.models.base_model_ import Model as APIModel


class JSONEncoder(FlaskJSONEncoder):
    include_nulls = False

    def default(self, o):
        if hasattr(o, 'openapi_types'):
            dikt = {}
            for attr, _ in six.iteritems(o.openapi_types):
                value = getattr(o, attr)
                if value is None and not self.include_nulls:
                    continue
                attr = o.attribute_map[attr]
                dikt[attr] = value
            return dikt
        return FlaskJSONEncoder.default(self, o)
