# TigerBlock

TigerBlock is a Kivy-based Android firewall prototype. It requests Android VPN
permission and starts the native `BlockVpnService` without requiring root
access.

## Requirements

- Linux environment with Python 3
- Buildozer and its Android toolchain
- Android SDK/API 33
- A USB-connected or emulated Android device for testing

Install the Python dependencies with:

```bash
pip install kivy pyjnius buildozer
```

## Build the APK

From the project root, run:

```bash
buildozer android debug
```

The generated APK is placed in `bin/`. To build, install, and start it on a
connected device, use:

```bash
buildozer android debug deploy run
```

The first build downloads the required Android SDK, NDK, and Gradle
components, so it may take some time.

## Project layout

- `main.py` - Kivy user interface and VPN permission flow
- `src/org/tigerblock/BlockVpnService.java` - native Android VPN service
- `buildozer.spec` - Android package and build configuration

## Notes

The app must be granted VPN permission by Android before the service can run.
The current interface is a prototype and does not yet provide per-application
rules or a persistent settings screen.