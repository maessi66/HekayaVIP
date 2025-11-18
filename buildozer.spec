[app]

title = General VIP
package.name = general_vip
package.domain = com.generalvip

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json

version = 1.0

requirements = python3,kivy

orientation = portrait
fullscreen = 1

android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b

android.permissions = INTERNET,ACCESS_NETWORK_STATE,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

icon.filename = screens/icon.png

[buildozer]
log_level = 2
warn_on_root = 1
