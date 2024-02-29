{ pkgs }: {
  deps = [
    pkgs.imagemagick
    pkgs.sqlite.bin
    pkgs.mailutils
  ];
}