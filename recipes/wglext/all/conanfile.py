import os
from conan import ConanFile, tools
from conan.tools.scm import Version
from conan.tools import files
from conan.errors import ConanInvalidConfiguration


required_conan_version = ">=1.37.0"

class WglextConan(ConanFile):
    name = "wglext"
    license = "MIT"
    url = "https://github.com/conan-io/conan-center-index"
    homepage = "https://www.khronos.org/registry/OpenGL/index_gl.php"
    description = "WGL extension interfaces"
    topics = ("opengl", "gl", "wgl", "wglext")
    no_copy_source = True
    requires = "opengl/system"
    settings = "os",

    def validate(self):
        if self.settings.os != "Windows":
            raise ConanInvalidConfiguration("wglext is only supported on Windows")

    def source(self):
        files.download(self, filename="wglext.h", **self.conan_data["sources"][self.version])

    def package(self):
        self.copy(pattern="wglext.h", dst=os.path.join("include", "GL"))
        license_data = files.load(self, os.path.join(self.source_folder, "wglext.h"))
        begin = license_data.find("/*") + len("/*")
        end = license_data.find("*/")
        license_data = license_data[begin:end]
        license_data = license_data.replace("**", "")
        files.save(self, "LICENSE", license_data)
        self.copy("LICENSE", dst="licenses")

    def package_id(self):
        self.info.header_only()
