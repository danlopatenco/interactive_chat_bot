import os

TRUTHY_STRINGS = ("true", "yes", "on", "1")


def get_env_var(var_name, default=None):
    var = os.getenv(var_name, default)
    if var is None or var == '':
        raise EnvironmentError(f"Set the {var_name} environment variable")
    return var


def get_int_env_var(var_name, default=None):
    var = get_env_var(var_name, default)
    try:
        return int(var)
    except ValueError:
        raise ValueError(
            f"Environment variable {var_name} must be an integer or integer-convertible string"
        )
