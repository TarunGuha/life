from client.proxy.proxy_client import proxy_request


def call_get_virgin_atlantic_token():
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
        "Authorization": "Basic bWVyY2F0b3I6",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
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

    data = {
        "password": "12345678",
        "username": "APPGUEST",
        "grant_type": "password",
    }

    response = proxy_request(
        request_url="https://myvs.virginatlanticcargo.com/api/iam/oauth/token",
        request_method="POST",
        request_headers=headers,
        request_data=data,
    )

    bearer_token = (
        response.get("body").get("response").get("response_json").get("access_token")
    )
    return bearer_token
