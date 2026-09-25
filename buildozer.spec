[app]
title = TigerBlock
version = 1.0.0
package.name = tigerblock
package.domain = org.tigerblock

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,java

# ربط مجلد ملفات Java بالنظام
android.add_src = src

# الأذونات المطلوبة لعمل الجدار الناري
android.permissions = INTERNET, ACCESS_NETWORK_STATE, BIND_VPN_SERVICE, CHANGE_WIFI_STATE

# المكتبات المطلوبة
requirements = python3,kivy,pyjnius

# إعدادات الأندرويد
android.api = 33
android.minapi = 21
android.sdk = 33
android.accept_sdk_license = True