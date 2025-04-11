{
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
  };

  outputs = { self, nixpkgs }:
  let
    system = "x86_64-linux";
    pkgs = import nixpkgs {
      inherit system;
    };
  in
  {
    devShell.${system} = pkgs.mkShell {
       packages = with pkgs; [
          zsh
          git

          python312
          ansible
          python312Packages.python-dotenv
          python312Packages.ansible
          python312Packages.streamlit
          python312Packages.digital-ocean
        ];


        # Simply just exec zsh
        shellHook = ''
          export LD_LIBRARY_PATH=\"${pkgs.stdenv.cc.cc.lib}/lib:$LD_LIBRARY_PATH\"
          exec zsh
        '';
    };
  };
}
