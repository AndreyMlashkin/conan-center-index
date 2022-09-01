from conan import ConanFile, tools
from conan.tools.scm import Version
from conan.tools import files


class LibsassTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"

    def test(self):
        if not tools.build.cross_building(self):
            self.run("sassc --version", run_environment=True)
