{ pkgs ? import <nixpkgs> {} }:
 
pkgs.mkShell {
  buildInputs = with pkgs; [
    python310Packages.mypy
    python310Packages.poetry    
  ];
  
  shellHook = ''
    export PYTHONPATH=./src
  '';
}