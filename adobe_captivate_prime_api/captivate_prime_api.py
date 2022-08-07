"""This module is mainly responsible for Adobe Captivate Prime APIs and their
methods via ``CaptivatePrimeAPI`` class."""

import configparser
import logging
import os
from datetime import (
    datetime,
    timedelta,
)

import requests

logging.getLogger(__name__).addHandler(logging.NullHandler())
config = configparser.ConfigParser()


class CaptivatePrimeAPI:
    """CaptivatePrimeAPI Class."""

    config_file = "config.cfg"
    default_server_instance = "captivateprime"

    def __init__(  # pylint:disable=too-many-arguments,too-many-branches
        self,
        server_instance=None,
        application_id=None,
        application_secret=None,
        application_url=None,
        application_scopes=None,
        access_token=None,
        refresh_token=None,
    ):

        config["CAPTIVATE"] = {
            "server_instance": f"{server_instance}",
            "application_id": f"{application_id}",
            "application_secret": f"{application_secret}",
            "application_url": f"{application_url}",
            "application_scopes": f"{application_scopes}",
            "access_token": f"{access_token}",
            "refresh_token": f"{refresh_token}",
        }

        config["APP"] = {
            "account_id": "",
            "user_id": "",
            "user_role": "",
            "checked_at": "",
            "refreshed_at": "",
            "expires_on": "",
        }

        if not os.path.exists(self.config_file):
            logging.error(
                "Configuration file is not valid, please provide a valid %s",
                self.config_file,
            )
            self.write_config()
        else:
            config.read(self.config_file)

            if config.has_section(section="CAPTIVATE"):
                if server_instance:
                    config.set(
                        section="CAPTIVATE",
                        option="server_instance",
                        value=server_instance,
                    )
                    logging.debug(
                        'Config file updated with "server_instance = %s"',
                        server_instance,
                    )
                elif config["CAPTIVATE"]["server_instance"] is None:
                    self.server_instance = self.default_server_instance
                    logging.debug(
                        'Config file updated with "server_instance = %s"',
                        self.default_server_instance,
                    )
                else:
                    self.server_instance = config["CAPTIVATE"]["server_instance"]
                if application_id:
                    config.set(
                        section="CAPTIVATE",
                        option="application_id",
                        value=application_id,
                    )
                    logging.debug(
                        'Config file updated with "application_id = %s"', application_id
                    )
                else:
                    self.application_id = config["CAPTIVATE"]["application_id"]
                if application_secret:
                    config.set(
                        section="CAPTIVATE",
                        option="application_secret",
                        value=application_secret,
                    )
                    logging.debug(
                        'Config file updated with "application_secret = %s"',
                        application_secret,
                    )
                else:
                    self.application_secret = config["CAPTIVATE"]["application_secret"]
                if application_url:
                    config.set(
                        section="CAPTIVATE",
                        option="application_url",
                        value=application_url,
                    )
                    logging.debug(
                        'Config file updated with "application_url = %s"',
                        application_url,
                    )
                else:
                    self.application_url = config["CAPTIVATE"]["application_url"]
                if application_scopes:
                    config.set(
                        section="CAPTIVATE",
                        option="application_scopes",
                        value=application_scopes,
                    )
                    logging.debug(
                        'Config file updated with "application_scopes = %s"',
                        application_scopes,
                    )
                else:
                    self.application_scopes = config["CAPTIVATE"]["application_scopes"]
                if access_token:
                    config.set(
                        section="CAPTIVATE",
                        option="access_token",
                        value=access_token,
                    )
                    logging.debug(
                        'Config file updated with "access_token = %s"',
                        access_token,
                    )
                else:
                    self.access_token = config["CAPTIVATE"]["access_token"]
                if refresh_token:
                    config.set(
                        section="CAPTIVATE",
                        option="refresh_token",
                        value=refresh_token,
                    )
                    logging.debug(
                        'Config file updated with "refresh_token = %s"',
                        refresh_token,
                    )
                else:
                    self.refresh_token = config["CAPTIVATE"]["refresh_token"]

                self.write_config()
            else:
                self.write_config()

    def fetch(  # pylint:disable=too-many-branches
        self, method: str, endpoint: str = None, params: dict = None
    ) -> list:
        """Generic API call function.

        :param method: str
        :param endpoint: str
        :param params: dict
        :return: list
        :raises: NotImplementedError: Not implemented.
        :exception Exception: Broad exception.

        """

        url = f"https://{self.server_instance}.adobe.com/primeapi/v2/{endpoint}"
        headers = {
            "Accept": "application/vnd.api+json",
            "Authorization": f"oauth {self.access_token}",
        }

        try:
            if method in ("get", "GET"):
                r_data = []
                while url:
                    logging.debug(url)
                    r = requests.get(url=url, params=params, headers=headers)
                    r_json = r.json()
                    if r.status_code == 200:
                        if isinstance(r_json["data"], list):
                            r_data.extend(r_json["data"])
                        elif isinstance(r_json["data"], dict):
                            r_data.append(dict(r_json["data"]))
                        try:
                            url = r_json["links"]["next"]
                            params = {}
                        except KeyError:
                            url = None
                    elif r.status_code == 400:
                        logging.error(
                            "%s %s - %s: %s",
                            r.status_code,
                            r_json["status"],
                            r_json["title"],
                            r_json["source"]["info"],
                        )
                        url = None
                    elif r.status_code == 401:
                        logging.error(
                            "%s %s - %s: %s",
                            r.status_code,
                            r_json["status"],
                            r_json["title"],
                            r_json["source"]["info"],
                        )
                        logging.info(
                            "A generic http unauthorized access error. "
                            "Access is denied due to invalid credentials. "
                            "Automatic process will try to refresh it..."
                        )
                        if not self.check_access_token():
                            url = None
                    else:
                        logging.error("%s %s", r.status_code, r.reason)
                        url = None

                return r_data
            elif method in ("post", "POST"):
                # TODO: POST
                # r = requests.post(url=url, params=params, headers=headers)
                raise NotImplementedError("POST method is not yet implemented.")
            elif method in ("patch", "PATCH"):
                # TODO: PATCH
                # r = requests.patch(url=url, params=params, headers=headers)
                raise NotImplementedError("PATCH method is not yet implemented.")
            elif method in ("delete", "DELETE"):
                # TODO: DELETE
                # r = requests.delete(url=url, params=params, headers=headers)
                raise NotImplementedError("DELETE method is not yet implemented.")
        except Exception as e:
            logging.error(str(e), url)
            raise Exception from e

    @staticmethod
    def create_tokens():
        """Captivate Prime APIs use OAuth 2.0 framework to authenticate and
        authorize your client applications.

        :raise NotImplementedError: Not implemented.

        """

        logging.error(
            "Captivate Prime APIs use OAuth 2.0 framework to "
            "authenticate and authorize the application. Due to limitations "
            "it is only possible to authenticate with login, manually."
        )

        raise NotImplementedError("Authenticate manually and set tokens in config.cfg")

    def check_access_token(self):
        """Checks in access token and check if it is expired or not.

        Logs remaining days and seconds.
        :return: True/False
        :rtype: Boolean

        """

        params = {
            "access_token": self.access_token,
        }

        url = f"https://{self.server_instance}.adobe.com/oauth/token/check"

        r = requests.get(
            url=url,
            params=params,
        )

        if r.status_code == 200:
            r_json = r.json()
            if "error" in r_json:
                logging.error("Error: %s", r_json["error"])
                logging.info(
                    '"access_token" has been expired and '
                    "automatic process will try to refresh it..."
                )
                return self.refresh_access_token()

            elif "expires_in" in r_json:
                checked_at = datetime.timestamp(datetime.utcnow())
                expires_on = datetime.timestamp(
                    datetime.utcnow() + timedelta(0, r_json["expires_in"])
                )
                expires_on_human = datetime.fromtimestamp(expires_on).isoformat()
                logging.info('"access_token" will be valid until %s', expires_on_human)

                if not config.has_section(section="APP"):
                    config.add_section(section="APP")
                config.set(
                    section="APP",
                    option="account_id",
                    value=str(r_json["account_id"]),
                )
                logging.debug(
                    'Config file updated with "account_id = %s"',
                    str(r_json["account_id"]),
                )

                config.set(
                    section="APP",
                    option="user_id",
                    value=str(r_json["user_id"]),
                )
                logging.debug(
                    'Config file updated with "user_id = %s"',
                    str(r_json["user_id"]),
                )

                config.set(
                    section="APP",
                    option="user_role",
                    value=r_json["user_role"],
                )
                logging.debug(
                    'Config file updated with "user_role = %s"',
                    r_json["user_role"],
                )

                config.set(
                    section="APP",
                    option="checked_at",
                    value=str(checked_at),
                )
                logging.debug(
                    'Config file updated with "checked_at = %s"',
                    str(checked_at),
                )

                config.set(
                    section="APP",
                    option="expires_on",
                    value=str(expires_on),
                )
                logging.debug(
                    'Config file updated with "expires_on = %s"',
                    str(expires_on),
                )

                self.write_config(content=config)
                return True
        else:
            logging.error("%s %s", r.status_code, r.reason)
            return False

    def refresh_access_token(self):
        """Retrieve new access token with given refresh token.

        Returns old access token if previous one is still valid
        :return: access_token, refresh_token
        :rtype: tuple
        :raises RuntimeError: Failed authorization or unexpected error while refreshing.

        """

        config.read(self.config_file)

        if not config.has_section(section="APP"):
            config.add_section(section="APP")

        url = f"https://{self.server_instance}.adobe.com/oauth/token/refresh"

        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
        }

        params = {
            "client_id": self.application_id,
            "client_secret": self.application_secret,
            "refresh_token": self.refresh_token,
        }

        r = requests.post(
            url=url,
            headers=headers,
            params=params,
        )

        r_json = r.json()

        if r.status_code == 200:
            access_token = r_json["access_token"]
            refresh_token = r_json["refresh_token"]
            refreshed_at = datetime.timestamp(datetime.utcnow())

            config.set(
                section="APP",
                option="checked_at",
                value=str(refreshed_at),
            )
            logging.debug(
                'Config file updated with "checked_at = %s"', str(refreshed_at)
            )

            if access_token != config["CAPTIVATE"]["access_token"]:

                expires_on = datetime.timestamp(
                    datetime.utcnow() + timedelta(0, r_json["expires_in"])
                )
                expires_on_human = datetime.fromtimestamp(expires_on).isoformat()

                self.access_token = access_token
                config.set(
                    section="CAPTIVATE",
                    option="access_token",
                    value=access_token,
                )
                logging.debug(
                    'Config file updated with "access_token = %s"',
                    access_token,
                )

                self.refresh_token = refresh_token
                config.set(
                    section="CAPTIVATE",
                    option="refresh_token",
                    value=refresh_token,
                )
                logging.debug(
                    'Config file updated with "refresh_token = %s"',
                    refresh_token,
                )

                config.set(
                    section="APP",
                    option="refreshed_at",
                    value=str(refreshed_at),
                )
                logging.debug(
                    'Config file updated with "refreshed_at = %s"',
                    str(refreshed_at),
                )

                config.set(
                    section="APP",
                    option="expires_on",
                    value=str(expires_on),
                )
                logging.debug(
                    'Config file updated with "expires_on = %s"',
                    str(expires_on),
                )

                logging.info(
                    '"access_token" has been refreshed and will be valid until %s',
                    expires_on_human,
                )

            self.write_config(content=config)
            return True
        elif r.status_code == 400:
            logging.error(
                "%s %s - %s: %s",
                r.status_code,
                r_json["status"],
                r_json["title"],
                r_json["source"]["info"],
            )
            raise RuntimeError(
                f"{r.status_code} {r_json['status']} - "
                f"{r_json['title']}: {r_json['source']['info']}"
            )
        else:
            logging.error("%s %s", r.status_code, r.reason)
            raise RuntimeError(
                f"Unexpected error: {r.status_code} {r.reason} while refreshing token!",
            )

    def write_config(
        self,
        content: configparser = config,
    ) -> None:
        """Write config to file.

        :param content: ConfigParser
        :raise RuntimeError: error while writing to the config file.

        """
        try:
            with open(self.config_file, "w", encoding="utf-8") as configfile:
                content.write(configfile)
        except Exception as e:
            logging.critical("Config file could not be saved: %s", str(e))
            raise RuntimeError from e
