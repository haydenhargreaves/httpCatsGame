"""
Stores the http codes and various functions for working
with them.
"""

import random

from typing import Dict, List, Optional
from random import choice

# Stores a list of codes that the http-cats api supports
codes: Dict[int, str] = {
    100: "Continue",
    101: "Switching Protocols",
    102: "Processing",
    200: "OK",
    201: "Created",
    202: "Accepted",
    203: "Non-Authoritative Information",
    204: "No Content",
    206: "Partial Content",
    207: "Multi-Status",
    300: "Multiple Choices",
    301: "Moved Permanently",
    302: "Found",
    303: "See Other",
    304: "Not Modified",
    305: "Use Proxy",
    307: "Temporary Redirect",
    308: "Permanent Redirect",
    400: "Bad Request",
    401: "Unauthorized",
    402: "Payment Required",
    403: "Forbidden",
    404: "Not Found",
    405: "Method Not Allowed",
    406: "Not Acceptable",
    407: "Proxy Authentication Required",
    408: "Request Timeout",
    409: "Conflict",
    410: "Gone",
    411: "Length Required",
    412: "Precondition Failed",
    413: "Payload Too Large",
    414: "URI Too Long",
    415: "Unsupported Media Type",
    416: "Range Not Satisfiable",
    417: "Expectation Failed",
    418: "I'm a teapot",
    421: "Misdirected Request",
    422: "Unprocessable Entity",
    423: "Locked",
    424: "Failed Dependency",
    425: "Too Early",
    426: "Upgrade Required",
    428: "Precondition Required",
    429: "Too Many Requests",
    431: "Request Header Fields Too Large",
    451: "Unavailable For Legal Reasons",
    495: "SSL Certificate Error",
    496: "SSL Certificate Required",
    497: "HTTP Request Sent to HTTPS Port",
    498: "Token expired/invalid",
    499: "Client Closed Request",
    500: "Internal Server Error",
    501: "Not Implemented",
    502: "Bad Gateway",
    503: "Service Unavailable",
    504: "Gateway Timeout",
    506: "Variant Also Negotiates",
    507: "Insufficient Storage",
    508: "Loop Detected",
    510: "Not Extended",
    511: "Network Authentication Required",
    521: "Web Server Is Down",
    522: "Connection Timed Out",
    523: "Origin Is Unreachable",
    525: "SSL Handshake Failed",
    530: "Site is frozen",
    599: "Network Connect Timeout Error",
}


def random_code(exc: Optional[List] = None) -> tuple[int, str]:
    """
    Returns a random HTTP code with a desc.
    exc allows caller to exclude codes, default will exclude nothing
    """
    code: int = choice(list(codes.keys()))
    while exc is not None and code in exc:
        code = choice(list(codes.keys()))
    return code, codes[code]


def get_code_from_msg(msg: str) -> int:
    """
    Convert a message into a string
    """
    for code, message in codes.items():
        if msg == message:
            return code

    return -1


def random_choices(code: int, count: int) -> List[str]:
    """
    Given a code, return 4 options to quiz the user, one will be the correct code.
    Count is the number of choices to create.
    """
    lst: list[str] = [codes[code]]
    sel_codes: list[int] = [code]

    for _ in range(count - 1):
        (cd, msg) = random_code(sel_codes)
        sel_codes.append(cd)
        lst.append(msg)

    random.shuffle(lst)

    return lst
