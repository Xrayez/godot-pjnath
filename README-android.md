# Building for Android

See [Compiling for Android](http://docs.godotengine.org/en/latest/development/compiling/compiling_for_android.html) and 
[Exporting for Android](http://docs.godotengine.org/en/latest/getting_started/workflow/export/exporting_for_android.html) 
official documentation for details.

## Compile
```bash
export ANDROID_HOME=/path/to/android-sdk
export ANDROID_NDK_ROOT=/path/to/android-ndk

# Release templates
scons platform=android target=release tools=no android_arch=armv7
scons platform=android target=release tools=no android_arch=arm64v8

cd platform/android/java
./gradlew build

# apk located at bin/android_release.apk

# Debug templates
scons platform=android target=release_debug android_arch=armv7
scons platform=android target=release_debug android_arch=arm64v8

cd platform/android/java
./gradlew build

# apk located at bin/android_debug.apk
```
