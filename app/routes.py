from flask import Blueprint, render_template, flash, redirect, url_for, request, current_app
from flask_login import login_user, logout_user, login_required, current_user
from flask_mail import Message
from app import db, mail
from app.models import User, Activity, News, Gallery, Contact, Volunteer

main = Blueprint('main', __name__)

@main.route('/')
def home():
    news = News.query.order_by(News.date_posted.desc()).limit(3).all()
    return render_template('index.html', news=news)

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/activities')
def activities():
    activities = Activity.query.all()
    return render_template('activities.html', activities=activities)

@main.route('/news')
def news():
    news_items = News.query.order_by(News.date_posted.desc()).all()
    return render_template('news.html', news=news_items)

@main.route('/gallery')
def gallery():
    items = Gallery.query.all()
    return render_template('gallery.html', items=items)

@main.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')
        
        new_contact = Contact(name=name, email=email, subject=subject, message=message)
        db.session.add(new_contact)
        db.session.commit()
        flash('تم إرسال رسالتكم بنجاح!', 'success')
        
        # Send Email Notification
        try:
            msg = Message(f"رسالة جديدة: {subject}",
                          recipients=[current_app.config['ADMIN_EMAIL']])
            msg.body = f"من: {name} ({email})\nالموضوع: {subject}\n\nالرسالة:\n{message}"
            mail.send(msg)
        except Exception as e:
            print(f"Erreur d'envoi d'email: {e}")
            
        return redirect(url_for('main.contact'))
    return render_template('contact.html')

@main.route('/join', methods=['GET', 'POST'])
def join():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        motivation = request.form.get('motivation')
        
        volunteer = Volunteer(name=name, email=email, phone=phone, motivation=motivation)
        db.session.add(volunteer)
        db.session.commit()
        flash('لقد تم استلام طلبكم بنجاح!', 'success')
        
        # Send Email Notification
        try:
            msg = Message("طلب تطوع جديد",
                          recipients=[current_app.config['ADMIN_EMAIL']])
            msg.body = f"طلب جديد من: {name}\nالبريد الإلكتروني: {email}\nالهاتف: {phone}\n\nالدافع:\n{motivation}"
            mail.send(msg)
        except Exception as e:
            print(f"Erreur d'envoi d'email: {e}")
            
        return redirect(url_for('main.join'))
    return render_template('join.html')

# Admin Routes

@main.route('/admin', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('main.dashboard'))
        flash('بيانات الدخول غير صحيحة. يرجى التحقق من اسم المستخدم وكلمة المرور.', 'danger')
    return render_template('admin/login.html')

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.home'))

@main.route('/login')
def login_redirect():
    return redirect(url_for('main.login'))

@main.route('/dashboard')
@login_required
def dashboard():
    # Get statistics
    messages_count = Contact.query.count()
    volunteers_count = Volunteer.query.count()
    activities_count = Activity.query.count()
    news_count = News.query.count()
    
    # Get recent items
    recent_messages = Contact.query.order_by(Contact.date_posted.desc()).limit(5).all()
    recent_volunteers = Volunteer.query.order_by(Volunteer.date_applied.desc()).limit(5).all()
    
    return render_template('admin/dashboard.html',
                         messages_count=messages_count,
                         volunteers_count=volunteers_count,
                         activities_count=activities_count,
                         news_count=news_count,
                         recent_messages=recent_messages,
                         recent_volunteers=recent_volunteers)

@main.route('/admin/news/add', methods=['GET', 'POST'])
@login_required
def add_news():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        
        if not title or not content:
            flash('يرجى ملء جميع الحقول المطلوبة', 'danger')
            return redirect(url_for('main.add_news'))
            
        new_item = News(title=title, content=content)
        db.session.add(new_item)
        db.session.commit()
        flash('تم إضافة المقال بنجاح!', 'success')
        return redirect(url_for('main.dashboard'))
        
    return render_template('admin/add_news.html')

@main.route('/admin/news/manage')
@login_required
def manage_news():
    news_items = News.query.order_by(News.date_posted.desc()).all()
    return render_template('admin/manage_news.html', news_items=news_items)

@main.route('/admin/news/delete/<int:news_id>', methods=['POST'])
@login_required
def delete_news(news_id):
    news_item = News.query.get_or_404(news_id)
    db.session.delete(news_item)
    db.session.commit()
    flash('تم حذف المقال بنجاح', 'success')
    return redirect(url_for('main.manage_news'))
