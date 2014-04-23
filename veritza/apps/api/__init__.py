from tastypie.resources import Resource

from veritza.apps.core.models import Dataset

class DatasetResource(Resource):
    model = Dataset