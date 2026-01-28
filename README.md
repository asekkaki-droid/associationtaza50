# موقع جمعية تازة للمستقبل (Association Taza Dashboard)

تطبيق ويب مبني باستخدام **Flask** لإدارة أنشطة وأخبار الجمعية، مع لوحة تحكم كاملة للمسؤولين.

## المميزات
- **لوحة تحكم (Admin Dashboard)**: إدارة الأخبار والأنشطة.
- **إدارة الأخبار**: إضافة وتعديل وحذف المقالات الإخبارية.
- **التواصل**: نموذج تواصل متكامل يرسل الإشعارات.
- **تصميم متكامل**: يدعم اللغة العربية بشكل كامل (RTL).

## المتطلبات (Prerequisites)
- Python 3.10+
- Flask 3.0.2

## طريقة التشغيل محلياً (Installation)
1. قم بتحميل المستودع:
   ```bash
   git clone https://github.com/YOUR_USERNAME/assosiation-taza.git
   cd assosiation-taza
   ```
2. قم بإنشاء بيئة افتراضية:
   ```bash
   python -m venv venv
   source venv/bin/activate  # على Windows: venv\Scripts\activate
   ```
3. تثبيت المكتبات اللازمة:
   ```bash
   pip install -r requirements.txt
   ```
4. تشغيل التطبيق:
   ```bash
   python run.py
   ```

## ملاحظة أمنية
يستخدم هذا المشروع ملف `.gitignore` لمنع رفع ملفات قاعدة البيانات الخاصة (`site.db`) والمفاتيح السرية إلى الإنترنت.
