{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {

  buildInputs = [
    pkgs.ansible
    pkgs.python312
    pkgs.python312Packages.python-dotenv
    pkgs.python312Packages.ansible
    pkgs.python312Packages.streamlit
    pkgs.python312Packages.digital-ocean
  ];
  # Pretty much all we need for this project
  shellHook = ''
    # fixes libstdc++ issues and libgl.so issues
    LD_LIBRARY_PATH=${pkgs.stdenv.cc.cc.lib}/lib/

    zsh
  '';
}
