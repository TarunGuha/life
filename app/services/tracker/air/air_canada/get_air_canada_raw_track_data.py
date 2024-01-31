from client.proxy import ProxyRequest
import datetime

def call_get_air_canada_raw_track_data(
    basic_cookies, auth_cookies, auth_tokens, signature, request
):
    headers = {
        "authority": "akamai-gw-cargo.digital.aircanada.com",
        "accept": "*/*",
        "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
        "authorization": "AWS4-HMAC-SHA256 Credential={access_key_id}/20240131/ca-central-1/execute-api/aws4_request, SignedHeaders=host;x-amz-date;x-amz-security-token, Signature={signature}".format(
            access_key_id=auth_tokens.get("AccessKeyId"),
            signature=signature,
        ),
        "origin": "https://www.aircanada.com",
        "referer": "https://www.aircanada.com/",
        "sec-ch-ua": '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"macOS"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        "x-amz-date": datetime.utcnow().strftime('%Y%m%dT%H%M%SZ'),
        "x-amz-security-token": auth_tokens.get("SessionToken"),
    }

    params = {
        "bookinginfo": "true",
        "flightinfo": "true",
    }

    raw_track_data = ProxyRequest().request(
        request_method="POST",
        request_url="https://akamai-gw-cargo.digital.aircanada.com/cargo/flights/tracking/01431716366",
        request_params=params,
        request_cookies=auth_cookies | basic_cookies,
        request_headers=headers,
    )

    return raw_track_data
