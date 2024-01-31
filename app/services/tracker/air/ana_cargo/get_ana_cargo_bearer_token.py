from client.proxy import ProxyRequest


def call_get_ana_cargo_bearer_token(cookies):
    headers = {
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
        "Connection": "keep-alive",
        "Origin": "https://prd.intcgo.ana.co.jp",
        "Referer": "https://prd.intcgo.ana.co.jp/icargoneoportal/app/main/?ext=true",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        "accept": "*/*",
        "content-type": "application/json",
        "sec-ch-ua": '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"macOS"',
    }

    json_data = {
        "operationName": "loginAsAnonymousUser",
        "variables": {},
        "query": "mutation loginAsAnonymousUser {\n  loginAsAnonymousUser {\n    security {\n      id_token\n      exp\n      __typename\n    }\n    loginProfile {\n      company_code\n      airport_code\n      default_warehouse_code\n      own_airline_code\n      own_airline_identifier\n      own_airline_numeric_code\n      station_code\n      first_name\n      last_name\n      screens\n      agent_code\n      language\n      user_timezone\n      portal_user_type\n      user_id\n      role_group_code\n      airline_mapping\n      email_address\n      __typename\n    }\n    errors {\n      error_description\n      error_code\n      error_type\n      __typename\n    }\n    __typename\n  }\n}\n",
    }

    track_page_proxy_call = ProxyRequest().request(
        request_method="POST",
        request_url="https://prd.intcgo.ana.co.jp/portalgateway/graphql",
        request_cookies=cookies,
        request_headers=headers,
        request_json=json_data,
    )

    bearer_token = (
        track_page_proxy_call.get("body")
        .get("response")
        .get("response_json")
        .get("data")
        .get("loginAsAnonymousUser")
        .get("security")
        .get("id_token")
    )

    return bearer_token
