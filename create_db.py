from app import create_app, db
from app.models import User, Activity, News, Gallery
from datetime import datetime, timedelta
import sys

app = create_app()

with app.app_context():
    # Create tables
    db.create_all()
    print("تم إنشاء قاعدة البيانات.")

    # Check if admin exists
    if not User.query.filter_by(username='admin').first():
        user = User(username='admin')
        user.set_password('admin123')
        db.session.add(user)
        db.session.commit()
        print("تم إنشاء حساب المسؤول (المستخدم: admin، كلمة المرور: admin123)")
    else:
        print("حساب المسؤول موجود بالفعل.")
    
    # Add sample activities if none exist
    if Activity.query.count() == 0:
        activities = [
            Activity(
                title="عمل تضامني مجتمعي",
                description="توزيع سلال غذائية على العائلات المحتاجة وزرع الأشجار في أحياء تازة.",
                date=datetime.now() - timedelta(days=10)
            ),
            Activity(
                title="مهرجان تازة الثقافي",
                description="احتفال بالثراء الثقافي لمنطقتنا مع موسيقى تقليدية، رقصات وحرف يدوية محلية.",
                date=datetime.now() - timedelta(days=5)
            ),
            Activity(
                title="تكوين وتوجيه الشباب",
                description="برنامج تكوين مهني ومرافقة لشباب المنطقة.",
                date=datetime.now() + timedelta(days=10)
            )
        ]
        for activity in activities:
            db.session.add(activity)
        print("تمت إضافة أنشطة نموذجية.")
    
    # Add sample news if none exist
    if News.query.count() == 0:
        news_items = [
            News(
                title="إطلاق برنامجنا التعليمي الجديد",
                content="يسعدنا الإعلان عن إطلاق برنامجنا التعليمي الجديد لأطفال المنطقة.",
                date_posted=datetime.now() - timedelta(days=3)
            ),
            News(
                title="شكراً لكل متطوعينا!",
                content="شكراً جزيلاً لجميع المتطوعين الذين شاركوا في آخر عمل تضامني.",
                date_posted=datetime.now() - timedelta(days=7)
            ),
            News(
                title="تعاون جديد مع المجلس البلدي",
                content="يسرنا الإعلان عن تعاون جديد مع المجلس البلدي لمدينة تازة.",
                date_posted=datetime.now() - timedelta(days=14)
            )
        ]
        for news in news_items:
            db.session.add(news)
        print("تمت إضافة مقالات نموذجية.")
    
    # Add sample gallery items if none exist
    if Gallery.query.count() == 0:
        gallery_items = [
            Gallery(title="عمل مجتمعي", media_file="activity-1.jpg"),
            Gallery(title="حدث ثقافي", media_file="activity-2.jpg"),
            Gallery(title="مدينتنا تازة", media_file="taza-hero.jpg")
        ]
        for item in gallery_items:
            db.session.add(item)
        print("تمت إضافة صور للمعرض.")
    
    db.session.commit()
    print("تم إنشاء البيانات النموذجية بنجاح!")

