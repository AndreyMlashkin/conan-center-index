from conan import ConanFile, tools
from conan.tools import files


class TestPackageConan(ConanFile):

    settings = "os", "arch", "build_type", "compiler"

    def test(self):
        if not tools.build.cross_building(self):
            self.run("ragel --version", run_environment=True)
