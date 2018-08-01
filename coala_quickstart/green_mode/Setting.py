settings_key = 'green_mode_infinite_value_settings'


def find_max_min_of_setting(setting, value, contents, operator):
    """
    Generates min/max value of a setting where this
    function is called upon for every value generated for
    every file in the project (excluding ignored files).
    :param setting:
        The setting for which to find the min value of.
    :param value:
        The current value to be compared against the
        supposedly min value stored in contents.
    :param contents:
        The python object to be written to 'PROJECT_DATA'
        which contains the min value of the setting which was
        encountered uptil now.
    :param operator:
        Either the less than or greater than operator.
    :return:
        The contents with the min value of the setting encountered
        uptil now after comparing it with the current value recieved
        by the function.
    """
    found = False
    for index, item in enumerate(contents[settings_key]):
        if isinstance(item, dict) and setting in item:
            found = True
            position = index
    if not found:
        contents[settings_key].append({setting: value})
        return contents
    current_val = contents[settings_key][position][setting]
    if operator(value, current_val):
        contents[settings_key][position][setting] = value
    return contents
