from conan import ConanFile, tools
from conan.tools.scm import Version
from conan.tools import files
from conans import CMake
import os


class TestPackageConan(ConanFile):
    settings = "os", "arch", "compiler", "build_type"
    generators = "cmake", "cmake_find_package_multi"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        if not tools.build.cross_building(self):
            exec_path = os.path.join("bin", "test_package")
            self.run("{} --help".format(exec_path), run_environment=True)
