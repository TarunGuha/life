from client.proxy.proxy_client import ProxyRequest


def call_get_virgin_atlantic_raw_data(bearer_token, booking_reference_number):
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
        "Authorization": "Bearer " + bearer_token,
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Referer": "https://myvs.virginatlanticcargo.com/app/offerandorder/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        "sec-ch-ua": '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"macOS"',
    }

    raw_tracking_data = ProxyRequest().request(
        request_method="GET",
        request_url="https://myvs.virginatlanticcargo.com/api/order/services/cargo/v1/orders/b"
        + booking_reference_number,
        request_headers=headers,
    )

    return raw_tracking_data
