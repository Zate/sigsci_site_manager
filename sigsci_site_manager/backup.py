import json


def filter_data(data, keys):
    ret = []
    for item in data:
        # Only save the data required by the create API
        ret.append({k: item[k] for k in keys})
    return ret


def get_rule_lists(api):
    keys = ['name', 'type', 'description', 'entries']
    data = api.get_rule_lists()
    return filter_data(data['data'], keys)


def get_request_rules(api):
    keys = ['enabled', 'groupOperator', 'conditions',
            'action', 'signal', 'reason', 'expiration']
    data = api.get_request_rules()
    return filter_data(data['data'], keys)


def get_custom_signals(api):
    keys = ['longName', 'description']
    data = api.get_custom_signals()
    return filter_data(data['data'], keys)


def get_custom_alerts(api):
    keys = ['tagName', 'longName', 'interval',
            'threshold', 'enabled', 'action']
    data = api.get_custom_alerts()
    return filter_data(data['data'], keys)


def get_site_members(api):
    keys = ['user', 'role']
    data = api.get_site_members()
    return filter_data(data['data'], keys)


def backup(api, site_name, file_name):
    print('Backing up site "%s" to file "%s"...' %
          (site_name, file_name))
    api.site = site_name

    data = {}
    data['rule_lists'] = get_rule_lists(api)
    data['request_rules'] = get_request_rules(api)
    data['custom_signals'] = get_custom_signals(api)
    # data['signal_rules'] = get_signal_rules()
    # data['advanced_rules'] = get_advanced_rules()
    # data['templated_rules'] = get_templated_rules(api)
    data['custom_alerts'] = get_custom_alerts(api)
    data['site_members'] = get_site_members(api)

    with open(file_name, 'w') as f:
        f.write(json.dumps(data))
