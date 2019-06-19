# PJNATH module for Godot

Godot 3.1 compatible.

See [thirdparty/README.md](thirdparty/README.md) for PJNATH license and details.

## Installation

Before installing, you must be able to 
[compile Godot Engine](https://docs.godotengine.org/en/latest/development/compiling/) 
from source.

```bash
# Copy the module under directory named `pjnath` (must be exactly that)
cp godot-pjnath <godot_path>/modules/pjnath && cd <godot_path>
# Compile the engine manually, for instance:
scons platform=windows target=release_debug bits=64
```

Also see platform-specific instructions:
* [Building for Android](README-android.md)
