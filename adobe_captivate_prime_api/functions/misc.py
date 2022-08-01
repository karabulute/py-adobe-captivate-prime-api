from adobe_captivate_prime_api import CaptivatePrimeAPI


def get_account_info(
    api: CaptivatePrimeAPI,
):
    """Get detailed information for an account in your organization.

    :param api: CaptivatePrimeAPI
    :type api: CaptivatePrimeAPI
    :return:

    """

    return api.fetch(
        method="GET",
        endpoint="account",
    )


def check_elthor_support(
    api: CaptivatePrimeAPI,
    version: str,
):
    """Checks if a version of the elthor desktop app is supported.

    :param api: CaptivatePrimeAPI
    :type api: CaptivatePrimeAPI
    :param version: str
    :return:

    """

    params = {
        "version": version,
    }

    return api.fetch(
        method="GET",
        endpoint="elthor/check",
        params=params,
    )


def get_user_info(
    api: CaptivatePrimeAPI,
    include: str,
):
    """Get the detailed information of the user who is currently logged in.

    :param api: CaptivatePrimeAPI
    :type api: CaptivatePrimeAPI
    :param include: str
    :return:

    """

    params = {
        "include": include,
    }

    return api.fetch(
        method="GET",
        endpoint="user",
        params=params,
    )


def go(  # pylint:disable=invalid-name
    api: CaptivatePrimeAPI,
):
    """Go Urls. Authentication is not required.

    :type api: CaptivatePrimeAPI
    :return:
    :rtype:

    """

    raise NotImplementedError
