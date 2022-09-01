from conan import ConanFile, tools
from conan.tools import files
import os


class TestPackageConan(ConanFile):
    settings = "os", "arch", "compiler", "build_type"

    def test(self):
        if not tools.build.cross_building(self):
            self.run("xsd --help", run_environment=True)
