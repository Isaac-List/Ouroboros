# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

"""Classify Module"""

import requests
import json
import xmltodict


def getInfo(isbn: str):
    url = "http://classify.oclc.org/classify2/Classify?summary=true&isbn=" + isbn
    json_data = json.dumps(xmltodict.parse(requests.get(url).content))

    code = json.loads(json_data)["classify"]["response"]["@code"]

    if code == "4":
        owi = json.loads(json_data)["classify"]["works"]["work"][0]["@owi"]
        url = "http://classify.oclc.org/classify2/Classify?summary=true&owi=" + owi
        json_data = json.dumps(xmltodict.parse(requests.get(url).content))
        code = json.loads(json_data)["classify"]["response"]["@code"]

        if code == "4":
            wi = json.loads(json_data)["classify"]["works"]["work"][0]["@wi"]
            url = "http://classify.oclc.org/classify2/Classify?summary=true&wi=" + wi
            json_data = json.dumps(xmltodict.parse(requests.get(url).content))
    
    return json.loads(json_data)
