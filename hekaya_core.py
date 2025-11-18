class HekayaCore:
    def login(self, email, password, phone):
        # نظام دخول تجريبي – هنعمله حقيقي بعدين
        if email == "admin" and password == "1234":
            return True, "تم تسجيل الدخول بنجاح ✓"
        return False, "خطأ في البيانات ❌"
