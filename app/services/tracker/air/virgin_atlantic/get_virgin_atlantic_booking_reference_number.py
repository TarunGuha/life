from client.proxy.proxy_client import proxy_request


def call_get_virgin_atlantic_booking_reference_number(request, bearer_token):
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
        "Authorization": "Bearer " + bearer_token,
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Origin": "https://myvs.virginatlanticcargo.com",
        "Referer": "https://myvs.virginatlanticcargo.com/app/offerandorder/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        "sec-ch-ua": '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"macOS"',
    }

    params = {
        "view": "summary",
    }

    json_data = {
        "orderFilter": {
            "airCapacity": {
                "documentNumbers": [
                    request.airline_code + request.document_number,
                ],
                "includeItinerary": False,
            },
        },
        "pageRequest": {
            "page": 1,
            "pageSize": 10,
        },
    }

    booking_list = proxy_request(
        request_method="POST",
        request_url="https://myvs.virginatlanticcargo.com/api/order/services/cargo/v1/orders/actions/search",
        request_params=params,
        request_headers=headers,
        request_json=json_data,
    )

    booking_reference_number = (
        (
            (
                (
                    (
                        booking_list.get("body")
                        .get("response")
                        .get("response_json")
                        .get("data")
                        .get("order")
                    )[0]
                )
                .get("orderItems")
                .get("orderItem")
            )[0]
        )
        .get("reference")
        .get("bookingReferenceNumber")
    )

    return booking_reference_number
