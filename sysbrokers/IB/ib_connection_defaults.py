from sysdata.config.production_config import production_config
from syscore.objects import arg_not_supplied

LIST_OF_IB_PARAMS = ["ib_ipaddress", "ib_port", "ib_idoffset"]


def ib_defaults(**kwargs):
    """
    Returns ib configuration with following precedence
    1- if passed in arguments: ipaddress, port, idoffset - use that
    2- if defined in private_config file, use that. ib_ipaddress, ib_port, ib_idoffset
    3 - if defined in system defaults file, use that

    :return: mongo db, hostname, port
    """

    # this will include defaults.yaml if not defined in private
    passed_param_names = list(kwargs.keys())
    output_dict = {}
    for param_name in LIST_OF_IB_PARAMS:
        if param_name in passed_param_names:
            param_value = kwargs[param_name]
        else:
            param_value = arg_not_supplied

        if param_value is arg_not_supplied:
            param_value = getattr(production_config, param_name)

        output_dict[param_name] = param_value

    # Get from dictionary
    ipaddress = output_dict['ib_ipaddress']
    port = output_dict['ib_port']
    idoffset = output_dict['ib_idoffset']

    return ipaddress, port, idoffset