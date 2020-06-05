from flask import escape, jsonify, make_response
from info import zipcodes
# gcloud functions deploy NAME --runtime RUNTIME TRIGGER [FLAGS...]

def cors_enabled(request):
    # For more information about CORS and CORS preflight requests, see
    # https://developer.mozilla.org/en-US/docs/Glossary/Preflight_request
    # for more information.
    print("Processing", request)
    # Set CORS headers for preflight requests
    if request.method == 'OPTIONS':
        # Allows GET requests from any origin with the Content-Type
        # header and caches preflight response for an 3600s
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600'
        }
        print("returning early")
        return ('', 204, headers)

    # Set CORS headers for the main request
    headers = {
        'Access-Control-Allow-Origin': '*'
    }

    print("In function", request)
    _request = request.get_json(silent=True)

    if not _request:
        _request = request.args
    print(1, _request)
    if not _request:
        return ('', 204, headers)
    print(2)
    _request = _request['data']
    print("_request is", request, _request)
    l = []
    try:
        from google.cloud import firestore
        db = firestore.Client()
        q = db.collection(u'test')
        for elem in _request.keys():
            print(elem, _request[elem], type(_request[elem]))
            if _request[elem] != []:
                print("Searching for", elem, 'IN', _request[elem])
                q = q.where(elem, 'in', _request[elem])
        docs = q.stream()
        for doc in docs:
            d = doc.to_dict()
            location = d['location']
            print("location is", location)
            if location in zipcodes:
                coords = zipcodes[location]
                l.append(coords)

        print("Locations are ", l)
    except Exception as e:
        print(e)
        print("returning early")
        return ('', 204, headers)

    print("Headers are ", headers)

    res = make_response(
        jsonify(
            {"data": l}
        ),
        200
    )

    res.headers['Access-Control-Allow-Origin'] = '*'

    print('res is', type(res), res)

    return res
    # res =  ("data", 200, headers)
    # print('type', type(res))
    # return res