class PackIdTool < Formula
  include Language::Python::Virtualenv

  desc "CLI tool to modify Cribl pack IDs in .crbl files"
  homepage "https://github.com/yourusername/pack-cli"
  url "https://github.com/yourusername/pack-cli/archive/refs/tags/v1.0.0.tar.gz"
  sha256 "YOUR_SHA256_HERE"  # Replace with actual SHA256 after creating release
  license "MIT"

  depends_on "python@3.11"

  def install
    virtualenv_install_with_resources
  end

  test do
    system "#{bin}/pack-id", "--help"
  end
end

