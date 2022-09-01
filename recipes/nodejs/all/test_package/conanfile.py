import os
from conan import ConanFile, tools
from conan.tools.scm import Version
from conan.tools import files


class TestPackageConan(ConanFile):

    settings = "os", "arch"

    def test(self):
        if not tools.build.cross_building(self):
            self.output.info("Node version:")
            self.run("node --version", run_environment=True)
