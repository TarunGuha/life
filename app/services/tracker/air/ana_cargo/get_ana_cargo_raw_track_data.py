from client.proxy import proxy_request


def call_get_ana_cargo_raw_track_data(cookies, bearer_token, request):
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
        "operationName": "GetShipmentDetailsByAwb",
        "variables": {
            "shipmentNumber": request.airline_code + request.document_number,
        },
        "query": "query GetShipmentDetailsByAwb($shipmentNumber: String!) {\n  GetShipmentByAwb(shipmentNumber: $shipmentNumber) {\n    ...ShipmentFragment\n    __typename\n  }\n  GetShipmentSubscriptions(shipmentNumber: $shipmentNumber) {\n    ...ShipmentSubscriptionsFragment\n    __typename\n  }\n  GetShipmentContactsByAwb(shipmentNumber: $shipmentNumber) {\n    ...ShipmentContactsFragment\n    __typename\n  }\n  GetShipmentSplitsByAwb(shipmentNumber: $shipmentNumber) {\n    ...ShipmentSplitsFragment\n    __typename\n  }\n}\n\nfragment ShipmentSplitsFragment on TrackingItemSplit {\n  split_number\n  pieces\n  milestone_status\n  transit_stations {\n    number_of_flights\n    stops\n    __typename\n  }\n  split_details {\n    item_id\n    next_item_id\n    origin_airport_code\n    milestone_status\n    milestone_time\n    milestone_time_postfix\n    pieces\n    carrier_code\n    flight_number\n    actual_flight_data {\n      carrier_code\n      flight_number\n      milestone_time\n      __typename\n    }\n    sub_splits {\n      item_id\n      next_item_id\n      origin_airport_code\n      milestone_status\n      milestone_time\n      milestone_time_postfix\n      pieces\n      carrier_code\n      flight_number\n      actual_flight_data {\n        carrier_code\n        flight_number\n        milestone_time\n        __typename\n      }\n      sub_splits {\n        item_id\n        next_item_id\n        origin_airport_code\n        milestone_status\n        milestone_time\n        milestone_time_postfix\n        pieces\n        carrier_code\n        flight_number\n        actual_flight_data {\n          carrier_code\n          flight_number\n          milestone_time\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment ShipmentContactsFragment on ContactsType {\n  shipper_details {\n    name\n    code\n    address\n    country\n    state\n    city\n    zip_code\n    __typename\n  }\n  consignee_details {\n    name\n    code\n    address\n    country\n    state\n    city\n    zip_code\n    __typename\n  }\n  __typename\n}\n\nfragment ShipmentSubscriptionsFragment on SubscriptionsType {\n  emails\n  tracking_awb_serial_number\n  notifications\n  __typename\n}\n\nfragment ShipmentFragment on TrackingItem {\n  awb_number\n  pieces\n  stated_weight\n  stated_volume\n  special_handling_code\n  product_name\n  shipment_description\n  origin_airport_code\n  destination_airport_code\n  milestones {\n    milestone\n    status\n    __typename\n  }\n  departure_time\n  departure_time_postfix\n  arrival_time\n  arrival_time_postfix\n  transit_stations {\n    number_of_flights\n    stops\n    __typename\n  }\n  units_of_measure {\n    weight\n    volume\n    __typename\n  }\n  __typename\n}\n",
    }

    response = proxy_request(
        request_method="POST",
        request_url="https://prd.intcgo.ana.co.jp/portalgateway/graphql",
        request_cookies=cookies,
        request_headers=headers,
        request_json=json_data,
    )

    return response
