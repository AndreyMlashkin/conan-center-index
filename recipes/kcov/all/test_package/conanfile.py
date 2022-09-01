from conan import ConanFile, tools
from conan.tools import files


class KcovTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"

    def test(self):
        if not tools.build.cross_building(self, self.settings):
            self.run("kcov --version", run_environment=True)
