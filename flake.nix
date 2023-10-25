{
  description = "Labo2 IFT511";

  inputs.flake-utils.url = "github:numtide/flake-utils";

  # Pointing nixpkgs input to a specific commit
  inputs.nixpkgs.url =
    "github:nixos/nixpkgs/e5b91d92a01178f9eecc0c7dd09a89e29fe9cc6f";

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let pkgs = import nixpkgs { inherit system; };
      in {
        devShell = pkgs.mkShell {
          buildInputs = with pkgs; [
            python38
            python38Packages.pycryptodomex
            python38Packages.construct
          ];
        };
      });
}
