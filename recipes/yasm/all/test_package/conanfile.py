from conan import ConanFile, tools
from conan.tools.scm import Version
from conan.tools import files


class TestPackage(ConanFile):
    settings = "os", "arch", "compiler", "build_type"

    def test(self):
        if not tools.build.cross_building(self, self, skip_x64_x86=True):
            self.run("yasm --help", run_environment=True)
