[app]

title = Hekaya VIP
package.name = hekaya_vip
package.domain = org.hekaya

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0

requirements = python3,kivy

orientation = portrait

fullscreen = 1

android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b

android.permissions = INTERNET,ACCESS_NETWORK_STATE

icon.filename = screens/icon.png

[buildozer]
log_level = 2
warn_on_root = 1
