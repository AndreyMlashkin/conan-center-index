from conan import ConanFile, tools
from conan.tools.scm import Version
from conan.tools import files
from conans import CMake
import os

class TestPackageConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake", "cmake_find_package_multi"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        if not tools.build.cross_building(self):
            self.run(os.path.join("bin", "test_package"), run_environment=True)
