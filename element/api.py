import json
import logging
import time

import warnings
import requests
from requests.packages.urllib3 import exceptions

from solidfire import exceptions as sfexceptions

LOG = logging.getLogger(__name__)


class SolidFireClient(object):
    """The API for controlling a SolidFire cluster."""
    def __init__(self, *args, **kwargs):
        self.endpoint_dict = kwargs.get('endpoint_dict')
        self.endpoint_version = kwargs.get('endpoint_version', '7.0')
        self.raw = True
        self.request_history = []

    def issue_request(self, method, params, endpoint=None):
        if params is None:
            params = {}

        # NOTE(jdg): We allow passing in a new endpoint to issue_api_req
        # to enable some of the multi-cluster features like replication etc
        if endpoint is None:
            endpoint_dict = self.endpoint_dict
        payload = {'method': method, 'params': params}
        url = '%s/json-rpc/%s/' % (endpoint_dict['url'], self.endpoint_version)
        LOG.debug('Issue SolidFire API call: %s' % json.dumps(payload))

        start_time = time.time()
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", exceptions.InsecureRequestWarning)
            req = requests.post(url,
                                data=json.dumps(payload),
                                auth=(endpoint_dict['login'],
                                      endpoint_dict['password']),
                                verify=False,
                                timeout=30)

        # FIXME(jdg): Failure cases like wrong password
        # missing something that cause req.json to puke
        response = req.json()
        req.close()
        end_time = time.time()
        duration = end_time - start_time

        LOG.debug('Raw response data from SolidFire API: %s' % response)
        # TODO(jdg): Add check/retry catch for things where it's appropriate
        if 'error' in response:
            msg = ('API response: %s'), response
            self.request_history.append(
                (method, start_time, duration, 'failed'))
            LOG.error('Error in API request: %s' % response['error'])
            raise sfexceptions.SolidFireRequestException(msg)
        self.request_history.append(
            (method, start_time, duration, 'ok'))
        return response['result']
