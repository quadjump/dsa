{ pkgs ? import <nixpkgs> {} }:

let 
# pythonEnv = pkgs.poetry2nix.mkPoetryEnv {
#   projectDir = ./.;
#   editablePackageSources = {
#       my-app = ./src;
#   };
#   python = pkgs.python310;
# };

in 
pkgs.mkShell {
  buildInputs = [ 
    # pythonEnv
    pkgs.python310
    pkgs.poetry
  ];
}