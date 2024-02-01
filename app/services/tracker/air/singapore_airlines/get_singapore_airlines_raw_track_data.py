from client.proxy.proxy_client import ProxyRequest


def call_get_singapore_airlines_raw_track_data(request):

    headers = {
        "Accept": "application/json",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Origin": "https://www.siacargo.com",
        "Referer": "https://www.siacargo.com/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        "sec-ch-ua": '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"macOS"',
    }

    json_data = {
        "awbPrefix": request.airline_code,
        "awbSuffix": request.document_number,
        "type": "public",
    }

    response = ProxyRequest().request(
        request_method="POST",
        request_url="https://cube.ccnexchange.com/quick-service/618f5141-5855-4f64-b29c-992dc23daa2f/PP/1/TrackSearch_Details",
        request_headers=headers,
        request_json=json_data,
    )

    return response.get("body").get("response").get("response_json")
