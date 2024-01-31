from client.proxy import ProxyRequest


def call_get_ana_cargo_raw_activity_data(cookies, bearer_token, request):
    headers = {
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
        "Connection": "keep-alive",
        "Origin": "https://prd.intcgo.ana.co.jp",
        "Referer": "https://prd.intcgo.ana.co.jp/icargoneoportal/app/main/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        "accept": "*/*",
        "authorization": "Bearer " + bearer_token,
        "content-type": "application/json",
        "cptoken": "null",
        "sec-ch-ua": '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"macOS"',
        "trigger-point": "PTL009",
    }

    json_data = {
        "operationName": "GetShipmentActivityByAwb",
        "variables": {
            "shipmentNumber": request.airline_code + request.document_number,
        },
        "query": "query GetShipmentActivityByAwb($shipmentNumber: String!) {\n  GetShipmentActivityByAwb(shipmentNumber: $shipmentNumber) {\n    items {\n      event\n      pieces\n      reason\n      airport_code\n      event_time\n      weight\n      weight_unit\n      from_carrier\n      to_carrier\n      uld_number\n      arrival_time\n      departure_time\n      flight {\n        flight_carrier_code\n        flight_number\n        flight_date\n        origin\n        destination\n        __typename\n      }\n      __typename\n    }\n    filters {\n      statuses\n      flights\n      stations\n      __typename\n    }\n    __typename\n  }\n}\n",
    }

    response = ProxyRequest().request(
        request_method="POST",
        request_url="https://prd.intcgo.ana.co.jp/portalgateway/graphql",
        request_cookies=cookies,
        request_headers=headers,
        request_json=json_data,
    )

    return response
