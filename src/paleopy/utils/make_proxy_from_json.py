def make_proxy_from_json(jsonfile, djsons=None):

    if djsons is None: 
        raise ValueError("must pass a value for the path to the datasets.json file")

    import json

    with open(jsonfile, 'r') as f: 
        dict_from_json = json.load(f)

    dict_from_json['description'] = 'proxy'
    dict_from_json['djsons'] = djsons
    
    class obj_from_dict:
        def __init__(self, in_dict:dict):
            assert isinstance(in_dict, dict)
            for key, val in in_dict.items():
                if isinstance(val, (list, tuple)):
                   setattr(self, key, [obj_from_dict(x) if isinstance(x, dict) else x for x in val])
                else:
                   setattr(self, key, obj_from_dict(val) if isinstance(val, dict) else val)

    p = obj_from_dict(dict_from_json)

    return p