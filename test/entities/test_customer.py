import json

from starling.starling import Starling
from starling.utils.http import default_headers
from test.testsupport import expect_authorization_header


def test_get_customer(requests_mock):
    mock_url = "http://localhost"
    mock_access_token = "0123456789"

    mock_object = Starling({
        "api_url": mock_url
    })

    with open("../responses/v1-get-customers.json") as f:
        expected_response = json.load(f)

        requests_mock.get("{}/api/v1/customers".format(mock_url),
                          headers=default_headers(mock_access_token),
                          request_headers=expect_authorization_header(mock_access_token),
                          json=expected_response)

        mocked_response = mock_object.get_customer(access_token=mock_access_token)

        assert expected_response == mocked_response
