from urllib import request
from project import Project
import tomli

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        toml = tomli.loads(content)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(toml["tool"]["poetry"]["name"], toml["tool"]["poetry"]["description"],toml["tool"]["poetry"]["dependencies"],toml["tool"]["poetry"]["dev-dependencies"],)

