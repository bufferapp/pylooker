import requests


class LookerClient(object):
    """Client for Looker API.

    Used to initialize the client id and secret.

    Parameters
    ----------
    api_endpoint : str
        The API endpoint implemented for your Looker instance. Usually looks
        like https://<your-looker-host-name>:19999/api/3.0/
    client_id : str
        Client ID from the API3 credentials
    client_secret : str
        Client Secret from the API3 credentials

    Usage
    -----
    >>> from pylooker.client import LookerClient
    >>> api_endpoint = 'https://looker.company.com:19999/api/3.0/'
    >>> client_id = 'your-client-id'
    >>> client_secret = 'your-client-secret'
    >>> lc = LookerClient(api_endpoint, client_id, client_secret)
    """

    def __init__(self, api_endpoint, client_id, client_secret, verify=True):
        self.api_endpoint = api_endpoint
        self.client_id = client_id
        self.client_secret = client_secret
        self.verify = verify

    def _get_headers(self):
        token_request = requests.post(
            url=self.api_endpoint + "login",
            data={
                "client_id": self.client_id,
                "client_secret": self.client_secret
            },
            verify=self.verify,
        )

        token = token_request.json()["access_token"]
        headers = {"Authorization": "token " + token}

        return headers

    def run_look(
        self,
        look_id,
        format="json",
        limit=-1,
        apply_formatting=False,
        cache=False,
        apply_vis=False,
    ):
        """Get the result of running the specified look.

        Parameters
        ----------
        look_id : int
            Identifier of the saved look
        format : str
            Response format
        limit : int
            Limit the number of rows returned. Defaults to -1 to return all the
            results
        apply_formatting: boolean
            Apply model-specified formatting to each result.
        apply_vis: boolean
            Apply visualization options to results.
        cache:
            Get results from cache if available.
        """
        headers = self._get_headers()

        response = requests.get(
            url="{}{}/run/{}?limit={}&apply_formatting={}&apply_vis={}&cache={}".format(
                self.api_endpoint + "looks/",
                look_id,
                format,
                limit,
                apply_formatting,
                apply_vis,
                cache,
            ),
            verify=self.verify,
            headers=headers,
        )

        return response.json()

    def run_query(self, slug, format="json", limit=-1):
        """Get the result of running the specified query.

        Parameters
        ----------
        slug : str
            Identifier of the query. This slug is in every query URL after the
            qid parameter. In short URLs, the slug is the latest part of the
            URL
        format : str
            Response format
        limit : int
            Limit the number of rows returned. Defaults to -1 to return all the
            results
        """
        headers = self._get_headers()

        slug_response = requests.get(
            url=self.api_endpoint + "/queries/slug/" + slug,
            verify=self.verify,
            headers=headers,
        )

        response = requests.get(
            url="{}{}/run/{}?limit={}".format(
                self.api_endpoint + "queries/",
                slug_response.json()["id"],
                format,
                limit,
            ),
            verify=self.verify,
            headers=headers,
        )

        return response.json()
