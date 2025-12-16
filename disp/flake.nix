{
  description = "Hypercube visualization recording environment";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};

        # Build Hyperspeedcube with all X11 dependencies
        hyperspeedcube = pkgs.rustPlatform.buildRustPackage rec {
          pname = "hyperspeedcube";
          version = "0.4.0";

          src = ../hyper/Hyperspeedcube;

          cargoLock = {
            lockFile = ../hyper/Hyperspeedcube/Cargo.lock;
          };

          nativeBuildInputs = with pkgs; [
            pkg-config
            cmake
          ];

          buildInputs = with pkgs; [
            xorg.libxcb
            xorg.libxkbcommon
            xorg.libX11
            libGL
            wayland
            wayland-protocols
            libxkbcommon
          ];

          # Set library path for runtime
          postInstall = ''
            wrapProgram $out/bin/hyperspeedcube \
              --prefix LD_LIBRARY_PATH : ${pkgs.lib.makeLibraryPath [
                pkgs.xorg.libxcb
                pkgs.xorg.libxkbcommon
                pkgs.xorg.libX11
                pkgs.libGL
                pkgs.wayland
                pkgs.libxkbcommon
              ]}
          '';
        };

      in {
        # Development shell with all tools
        devShells.default = pkgs.mkShell {
          buildInputs = with pkgs; [
            # Hyperspeedcube (built above)
            hyperspeedcube

            # Automation tools
            xdotool
            xorg.xev        # For debugging key events
            wmctrl          # Window manager control

            # Recording and conversion
            ffmpeg-full
            gifsicle
            imagemagick

            # Optional screen recorders
            simplescreenrecorder

            # X11 runtime dependencies
            xorg.libxcb
            xorg.libxkbcommon
            xorg.libX11
            libGL
            wayland
            libxkbcommon

            # Python for scripting
            python3
          ];

          shellHook = ''
            echo "🎬 Hypercube Recording Environment"
            echo "=================================="
            echo ""
            echo "Available tools:"
            echo "  hyperspeedcube - 4D puzzle simulator"
            echo "  xdotool        - X11 automation"
            echo "  ffmpeg         - Video recording/conversion"
            echo "  gifsicle       - GIF optimization"
            echo ""
            echo "Scripts:"
            echo "  ./scripts/automate_hyperspeedcube.sh"
            echo "  ./scripts/video_to_gif.sh"
            echo ""
            echo "Quick start:"
            echo "  1. Launch: hyperspeedcube &"
            echo "  2. Record: ./scripts/automate_hyperspeedcube.sh 'FO FO' recordings/fo_fo.mp4"
            echo "  3. Convert: ./scripts/video_to_gif.sh recordings/fo_fo.mp4 figures/sequence_FO_FO.gif"
            echo ""

            export LD_LIBRARY_PATH="${pkgs.lib.makeLibraryPath [
              pkgs.xorg.libxcb
              pkgs.xorg.libxkbcommon
              pkgs.xorg.libX11
              pkgs.libGL
              pkgs.wayland
              pkgs.libxkbcommon
            ]}:$LD_LIBRARY_PATH"
          '';
        };

        # Package output
        packages.default = hyperspeedcube;
      }
    );
}