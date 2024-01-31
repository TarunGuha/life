from client.proxy import ProxyRequest


def call_get_air_canada_bearer_token():

    headers = {
        "authority": "cognito-identity.ca-central-1.amazonaws.com",
        "accept": "*/*",
        "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
        "amz-sdk-invocation-id": "edba9fda-41b1-4cc6-9cb6-0ec0ce900787",
        "amz-sdk-request": "attempt=1; max=3",
        "content-type": "application/x-amz-json-1.1",
        "origin": "https://www.aircanada.com",
        "referer": "https://www.aircanada.com/",
        "sec-ch-ua": '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"macOS"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        "x-amz-target": "AWSCognitoIdentityService.GetCredentialsForIdentity",
        "x-amz-user-agent": "aws-sdk-js/3.6.1 os/macOS/10.15.7 lang/js md/browser/Chrome_121.0.0.0 api/cognito_identity/3.6.1 aws-amplify/3.8.23_js",
    }

    data = '{"IdentityId":"ca-central-1:dc129f70-1dbf-c831-1066-070f107c6c22"}'

    auth_token_request = ProxyRequest().request(
        request_method="POST",
        request_url="https://cognito-identity.ca-central-1.amazonaws.com/",
        request_headers=headers,
        request_data=data,
    )

    return auth_token_request.get("body").get("response").get("response_json").get("Credentials")
