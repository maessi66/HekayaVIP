[app]

title = Hekaya VIP
package.name = hekayavip
package.domain = org.hekaya.vip
source.dir = .
source.include_exts = py, kv, png, jpg, jpeg

fullscreen = 0
orientation = portrait

# Icon
icon.filename = icon.png

# Python Requirements
requirements = python3, kivy

# Entry point
main.py = main.py

# Permissions
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# Supported Android Versions
android.api = 30
android.minapi = 21
android.ndk = 21b

[buildozer]
log_level = 2
warn_on_root = 1
