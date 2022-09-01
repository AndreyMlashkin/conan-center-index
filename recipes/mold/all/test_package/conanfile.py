import os
from conan import ConanFile, tools
from conan.tools.scm import Version
from conan.tools import files
from conan.tools.build import cross_building

class TestPackageConan(ConanFile):
    settings = "os", "arch", "build_type", "compiler"

    def test(self):
        if not cross_building(self):
            self.run("mold -v", run_environment=True)
