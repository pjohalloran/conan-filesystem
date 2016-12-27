from conans import ConanFile, CMake

class FilesystemConan(ConanFile):
  name = "filesystem"
  version = "1.0"
  description = "A tiny self-contained path manipulation library for C++."
  license="Modified BSD License (3-Clause BSD license)"
  settings = "os", "compiler", "build_type", "arch"
  url = "https://github.com/pjohalloran/conan-filesystem"

  def source(self):
    self.run("git clone https://github.com/wjakob/filesystem")

  def package(self):
    self.copy("*.h", src="filesystem/filesystem", dst="include", keep_path=True)

  def package_info(self):
    self.cpp_info.sharedlinkflags = ["-std=c++11"]
    self.cpp_info.exelinkflags = ["-std=c++11"]
    self.cpp_info.cppflags = ["-std=c++11", "-stdlib=libc++"]
