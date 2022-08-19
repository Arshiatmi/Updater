import enum
from typing import Callable
import requests


class RequestType(enum.Enum):
    Json = 0
    XML = 1


class Server:
    def __init__(self, link: str, current_version: str, server_routes: dict = None) -> None:
        self.link: str = link
        self.version: str = current_version
        self.changes: list = []
        if not server_routes:
            self.server_routes: dict = {
                "/latest_version": self.latest_version,
                "/changes": self.changes,
                "/download_latest": self.download_latest
            }

    def latest_version(self, server_route=None) -> str:
        if not server_route:
            server_route = self.server_routes["/latest_version"]
        return self.version

    def changes(self, server_route=None):
        if not server_route:
            server_route = self.server_routes["/changes"]
        pass

    def download_latest(self, server_route=None):
        if not server_route:
            server_route = self.server_routes["/download_latest"]
        pass


class Client:
    def __init__(self, link: str, version: str, server_routes: dict = None) -> None:
        self.link: str = link
        self.version: str = version
        self.changes: list = []
        if not server_routes:
            self.server_routes: dict = {
                "/latest_version": self.latest_version,
                "/changes": self.changes,
                "/download_latest": self.download_latest
            }

    def latest_version(self, server_route=None, parser: Callable = None) -> str:
        if not server_route:
            server_route = self.server_routes["/latest_version"]
        if not parser:
            parser = self.parser
        r = requests.get("{}/{}".format(self.link, server_route))
        return parser(r)

    def changes(self, server_route=None, parser: Callable = None):
        if not server_route:
            server_route = self.server_routes["/changes"]
        if not parser:
            parser = self.parser
        r = requests.get("{}/{}".format(self.link, server_route))
        return parser(r)

    def download_latest(self, server_route=None, parser: Callable = None):
        if not server_route:
            server_route = self.server_routes["/download_latest"]
        if not parser:
            parser = self.parser
        r = requests.get("{}/{}".format(self.link, server_route))
        return parser(r)

    @staticmethod
    def parser(request, request_type=RequestType.Json) -> dict:
        if request_type == RequestType.Json:
            return request.json()
