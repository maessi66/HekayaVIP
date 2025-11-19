[app]
# اسم التطبيق الظاهر
title = Hekaya VIP

# اسم الحزمة (لا مسافات)
package.name = hekaya_vip
package.domain = org.hekaya

# مصدر المشروع
source.dir = .

# الامتدادات المسموح بها
source.include_exts = py,png,jpg,kv,json

# رقم النسخة
version = 1.0

# المتطلبات الأساسية
requirements = python3,kivy,plyer,pyjnius

# اتجاه الشاشة
orientation = portrait

# ملء الشاشة
fullscreen = 1

# أيقونة التطبيق (تأكد أن الملف موجود)
icon.filename = screens/icon.png

# إعدادات أندرويد
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.build_tools_version = 33.0.2

# الصلاحيات
android.permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 1
