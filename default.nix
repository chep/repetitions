{ pkgs ? import <nixpkgs> { } }:

let
  pythonEnv = pkgs.python3.withPackages (ps: [ ps.pyqt6 ]);
  qtPlugins = [ pkgs.qt6.qtbase ]
    ++ pkgs.lib.optionals pkgs.stdenv.isLinux [ pkgs.qt6.qtwayland ];
in
pkgs.mkShell {
  packages = [
    pythonEnv
    pkgs.python3Packages.pyqt6 # fournit pyuic6
  ] ++ qtPlugins;

  shellHook = ''
    export QT_PLUGIN_PATH=${
      pkgs.lib.concatMapStringsSep ":"
        (p: "${p}/${pkgs.qt6.qtbase.qtPluginPrefix}") qtPlugins
    }''${QT_PLUGIN_PATH:+:$QT_PLUGIN_PATH}
  '';
}
