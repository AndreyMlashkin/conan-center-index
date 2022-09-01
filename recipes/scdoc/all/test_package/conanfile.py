from conan import ConanFile, tools
from conan.tools.scm import Version
from conan.tools import files
import os


class TestPackageConan(ConanFile):

    def test(self):
        if not tools.build.cross_building(self):
            self.run(
                f"scdoc < {os.path.join(self.source_folder,'test_package.1.scd')}", run_environment=True)
