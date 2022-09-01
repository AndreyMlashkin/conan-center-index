from conan import ConanFile, tools
from conan.tools.scm import Version
from conan.tools import files
import os


class TestPackgeConan(ConanFile):
    settings = "os", "arch"

    def test(self):
        self.run("b2 -v", run_environment=True)
