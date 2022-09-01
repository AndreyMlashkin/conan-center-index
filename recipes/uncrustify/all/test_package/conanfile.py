from conan import ConanFile, tools
from conan.tools import files


class TestPackageConan(ConanFile):
    settings = "os", "arch", "compiler", "build_type"

    def test(self):
        if not tools.build.cross_building(self):
            self.run("uncrustify --version", run_environment=True)
