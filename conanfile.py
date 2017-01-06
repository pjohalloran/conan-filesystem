from conans import ConanFile, CMake

class FilesystemConan(ConanFile):
  name = "filesystem"
  version = "1.0"
  description = "A tiny self-contained path manipulation library for C++."
  license="Modified BSD License (3-Clause BSD license)"
  settings = "os", "compiler", "build_type", "arch"
  url = "https://github.com/pjohalloran/conan-filesystem"
  options = {"compiler_version": ["11", "14"]}
  default_options = "compiler_version=14",

  def source(self):
    self.run("git clone https://github.com/wjakob/filesystem")

  def package(self):
    self.copy("*.h", src="filesystem/filesystem", dst="include", keep_path=True)

  def package_info(self):
    self.cpp_info.sharedlinkflags = ["-std=c++%s" % self.options.compiler_version]
    self.cpp_info.exelinkflags = ["-std=c++%s" % self.options.compiler_version]
    self.cpp_info.cppflags = ["-std=c++%s" % self.options.compiler_version, "-stdlib=libc++"]
