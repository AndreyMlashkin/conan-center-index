from conans import ConanFile, CMake, tools
from conan.tools.scm import Version
from conan.tools import files
import os


class TestPackageConan(ConanFile):
    settings = "os", "arch", "compiler", "build_type"
    generators = "cmake", "cmake_find_package_multi"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        if not tools.cross_building(self):
            bin_c_path = os.path.join("bin", "test_package_c")
            self.run(bin_c_path, run_environment=True)
            bin_cpp_path = os.path.join("bin", "test_package_cpp")
            self.run(bin_cpp_path, run_environment=True)
