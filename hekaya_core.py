# hekaya_core.py
import json
import os

DB_FILE = "users.json"

class HekayaCore:
    def __init__(self):
        if not os.path.exists(DB_FILE):
            with open(DB_FILE, "w") as f:
                json.dump({}, f)

    def _read(self):
        with open(DB_FILE, "r") as f:
            return json.load(f)

    def _write(self, data):
        with open(DB_FILE, "w") as f:
            json.dump(data, f, indent=2)

    def register(self, email, password, phone):
        data = self._read()
        data[email] = {"email": email, "password": password, "phone": phone}
        self._write(data)
        return True, "تم التسجيل"

    def login(self, email, password, phone):
        data = self._read()
        u = data.get(email)
        if not u:
            return False, "المستخدم غير موجود"
        if u["password"] != password or u["phone"] != phone:
            return False, "بيانات غير صحيحة"
        return True, "تم تسجيل الدخول بنجاح"

    def get_user(self, email=None):
        data = self._read()
        if not data:
            return None
        if email:
            return data.get(email)
        return next(iter(data.values()))
