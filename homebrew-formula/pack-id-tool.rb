class PackIdTool < Formula
  include Language::Python::Virtualenv

  desc "CLI tool to modify Cribl pack IDs in .crbl files"
  homepage "https://github.com/gcribl/pack-cli"
  url "https://github.com/gcribl/pack-cli/archive/refs/tags/v1.0.0.tar.gz"
  sha256 "992078c38950f764e76474a92a90eb2aca19981ada1a135b93bba10ed1d04342"  # Replace with actual SHA256 after creating release
  license "MIT"

  depends_on "python@3.11"

  def install
    virtualenv_install_with_resources
    
    # Install shell completions
    bash_completion.install "completions/pack-id.bash" => "pack-id"
    zsh_completion.install "completions/_pack-id"
    fish_completion.install "completions/pack-id.fish"
  end

  test do
    system "#{bin}/pack-id", "--help"
  end
end

