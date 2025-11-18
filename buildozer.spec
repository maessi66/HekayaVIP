[app]
# (اسم التطبيق الظاهر)
title = Hekaya VIP
# اسم الحزمة (لا تضع مسافات)
package.name = hekaya_vip
package.domain = org.hekaya

# مصدر المشروع
source.dir = .
# امثلة الامتدادات المطلوبة
source.include_exts = py,png,jpg,kv,json

# رقم النسخة
version = 1.0

# متطلبات بايثون/كيفي
requirements = python3,kivy

# اتجاه الشاشة
orientation = portrait

fullscreen = 1

# Android settings
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b

# صلاحيات مطلوبة
android.permissions = INTERNET

# أيقونة التطبيق (ضع ملف icon.png داخل مجلد screens)
icon.filename = screens/icon.png

# buildozer-specific
[buildozer]
log_level = 2
warn_on_root = 1
