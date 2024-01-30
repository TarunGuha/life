import json
import logging
import requests


def main(args):
    try:
        request_parameters = args.get("request_parameters")

        http_request_response = requests.request(
            method=request_parameters.get("request_type"),
            url=request_parameters.get("request_url"),
            params=request_parameters.get("request_params"),
            data=request_parameters.get("request_data"),
            json=request_parameters.get("request_json"),
            headers=request_parameters.get("request_headers"),
            cookies=request_parameters.get("request_cookies"),
        )

        response = {
            "response_cookies": http_request_response.cookies.get_dict(),
            "response_encoding": http_request_response.encoding,
            "response_headers": json.dumps(dict(http_request_response.headers)),
            "response_status_code": http_request_response.status_code,
            "response_text": http_request_response.text,
        }

        try:
            response_json = http_request_response.json()
            response["response_json"] = response_json
        except Exception as e:
            response["response_json"] = {}
            logging.warning(
                "Response Is Not Json Serializable Error Received => {error_message}".format(
                    error_message=str(e)
                )
            )

    except Exception as e:
        logging.error(
            "Error Encountered => {error_message}\nRequest Payload => {request_payload}".format(
                error_message=str(e), request_payload=args.get("request_parameters")
            )
        )
        response = {"response_error": str(e)}

    function_response = {"body": {"response": response}}

    return function_response
