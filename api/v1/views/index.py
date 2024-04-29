#!/usr/bin/python3
'''Create app_views '''
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', strict_slashes=False)
def api_status():
    '''Return status '''
    response = {'status': "OK"}
    return jsonify(response)


@app_views.route('/stats', strict_slashes=False)
def count():
    ''' '''
    data = {'states': State, 'users': User,
            'amenities': Amenity, 'cities': City,
            'places': Place, 'reviews': Review}
    for i in data:
        data[i] = storage.count(data[i])
    return jsonify(data)
