{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {

  buildInputs = [];
  
  # Pretty much all we need for this project
  shellHook = ''
    # fixes libstdc++ issues and libgl.so issues
    LD_LIBRARY_PATH=${pkgs.stdenv.cc.cc.lib}/lib/
  '';
}