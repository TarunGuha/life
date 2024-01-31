from client.proxy import ProxyRequest


def call_get_ana_cargo_cookies():
    headers = {
        "Accept": "*/*",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
        "Connection": "keep-alive",
        "Origin": "https://www.anacargo.jp",
        "Referer": "https://www.anacargo.jp/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        "sec-ch-ua": '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"macOS"',
    }

    homepage_proxy_call = ProxyRequest().request(
        request_method="POST",
        request_url="https://prd.intcgo.ana.co.jp/portalgateway/rest/orgv",
        request_headers=headers,
    )

    cookies = homepage_proxy_call.get("body").get("response").get("response_cookies")

    return cookies
