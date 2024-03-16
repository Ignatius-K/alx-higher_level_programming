#!/usr/bin/python3


def get_defined_names(attributes):
    """get_defined_names

    Args:
        attributes: list of attributes

    Returns:
        public sorted attibutes
    """
    attribute_list = []
    for attribute in attributes:
        if attribute.startswith("__"):
            continue
        attribute_list.append(attribute)
    return sorted(attribute_list) 


if __name__ == '__main__':
    import hidden_4
    module_attributes = get_defined_names(dir(hidden_4))
    for attribute in module_attributes:
        print("{}".format(attribute))

