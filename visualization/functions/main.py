from flask import escape
import pgeocode
from info import zipcodes
# gcloud functions deploy NAME --runtime RUNTIME TRIGGER [FLAGS...]
def hello_http(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <http://flask.pocoo.org/docs/1.0/api/#flask.Request>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>.
    """
    try:
        from google.cloud import firestore
        db = firestore.Client()
        doc_ref = db.collection(u'users').document(u'alovelace')
        doc_ref.set({
            u'first': u'Ada',
            u'last': u'Lovelace',
            u'born': 1815})
        request_json = request.get_json(silent=True)
        request_args = request.args
    except ImportError:
        print ("NO module found")

    if request_json and 'name' in request_json:
        name = request_json['name']
    elif request_args and 'name' in request_args:
        name = request_args['name']
    else:
        name = 'World'
    return 'Hello {}!'.format(escape(name))

def sort_data(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <http://flask.pocoo.org/docs/1.0/api/#flask.Request>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using make_response
        <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>.
    """
    try:
        from google.cloud import firestore
        _request = request.get_json(silent=True)
        if not _request:
            _request = request.args
        if not _request: 
            return None
        db = firestore.Client()
        q = db.collection(u'test')
        for elem in _request.keys():
            if not _request[elem] == '':
                print("Searching for", elem , '==', u'{}'.format(_request[elem]))
                q = q.where(elem, '==', u'{}'.format(_request[elem]))
        docs = q.stream()
        l = []

        for doc in docs:
            d = doc.to_dict()
            location = d['location']
            if location in zipcodes:
                coords = zipcodes[location]
            l.append(coords)

        print("Locations are ", l)    
        return l
    except ImportError:
        print ("NO module found")

    # if request_json and 'name' in request_json:
    #     name = request_json['name']
    # elif request_args and 'name' in request_args:
    #     name = request_args['name']
    # else:
    #     name = 'World'
    # return 'Hello {}!'.format(escape(name))
