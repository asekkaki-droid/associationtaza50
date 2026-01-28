// ==========================================
// Association Taza - Interactive Scripts
// ==========================================

document.addEventListener('DOMContentLoaded', function () {
    // Navbar scroll effect
    initNavbarScroll();

    // Smooth scroll for anchor links
    initSmoothScroll();

    // Gallery lightbox
    initGalleryLightbox();

    // Form enhancements
    initFormEnhancements();

    // Lazy loading for images
    initLazyLoading();

    // Animation on scroll
    initScrollAnimations();
});

// ==========================================
// Navbar Scroll Effect
// ==========================================
function initNavbarScroll() {
    const navbar = document.querySelector('.navbar');
    if (!navbar) return;

    window.addEventListener('scroll', function () {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });
}

// ==========================================
// Smooth Scroll for Anchor Links
// ==========================================
function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const href = this.getAttribute('href');
            if (href === '#' || href === '#!') return;

            e.preventDefault();
            const target = document.querySelector(href);
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

// ==========================================
// Gallery Lightbox
// ==========================================
function initGalleryLightbox() {
    const galleryItems = document.querySelectorAll('.gallery-item');
    if (galleryItems.length === 0) return;

    // Create lightbox modal
    const lightbox = createLightboxModal();
    document.body.appendChild(lightbox);

    const lightboxImg = lightbox.querySelector('.lightbox-image');
    const lightboxCaption = lightbox.querySelector('.lightbox-caption');
    const closeBtn = lightbox.querySelector('.lightbox-close');

    galleryItems.forEach(item => {
        item.addEventListener('click', function () {
            const img = this.querySelector('img');
            if (img) {
                lightboxImg.src = img.src;
                lightboxCaption.textContent = img.alt || '';
                lightbox.classList.add('active');
                document.body.style.overflow = 'hidden';
            }
        });
    });

    closeBtn.addEventListener('click', closeLightbox);
    lightbox.addEventListener('click', function (e) {
        if (e.target === lightbox) {
            closeLightbox();
        }
    });

    document.addEventListener('keydown', function (e) {
        if (e.key === 'Escape' && lightbox.classList.contains('active')) {
            closeLightbox();
        }
    });

    function closeLightbox() {
        lightbox.classList.remove('active');
        document.body.style.overflow = '';
    }
}

function createLightboxModal() {
    const lightbox = document.createElement('div');
    lightbox.className = 'lightbox';
    lightbox.innerHTML = `
        <div class="lightbox-content">
            <span class="lightbox-close">&times;</span>
            <img class="lightbox-image" src="" alt="">
            <div class="lightbox-caption"></div>
        </div>
    `;

    // Add lightbox styles
    const style = document.createElement('style');
    style.textContent = `
        .lightbox {
            display: none;
            position: fixed;
            z-index: 9999;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.95);
            opacity: 0;
            transition: opacity 0.3s ease;
        }
        
        .lightbox.active {
            display: flex;
            align-items: center;
            justify-content: center;
            opacity: 1;
        }
        
        .lightbox-content {
            position: relative;
            max-width: 90%;
            max-height: 90%;
            animation: zoomIn 0.3s ease;
        }
        
        .lightbox-image {
            max-width: 100%;
            max-height: 85vh;
            border-radius: 8px;
            box-shadow: 0 25px 50px rgba(0, 0, 0, 0.5);
        }
        
        .lightbox-close {
            position: absolute;
            top: -40px;
            right: 0;
            color: white;
            font-size: 40px;
            font-weight: bold;
            cursor: pointer;
            transition: color 0.3s;
        }
        
        .lightbox-close:hover {
            color: #27ae60;
        }
        
        .lightbox-caption {
            color: white;
            text-align: center;
            padding: 15px;
            font-size: 18px;
        }
        
        @keyframes zoomIn {
            from {
                transform: scale(0.8);
                opacity: 0;
            }
            to {
                transform: scale(1);
                opacity: 1;
            }
        }
    `;
    document.head.appendChild(style);

    return lightbox;
}

// ==========================================
// Form Enhancements
// ==========================================
function initFormEnhancements() {
    const forms = document.querySelectorAll('form');

    forms.forEach(form => {
        const inputs = form.querySelectorAll('input, textarea, select');

        inputs.forEach(input => {
            // Add floating label effect
            input.addEventListener('focus', function () {
                this.parentElement.classList.add('focused');
            });

            input.addEventListener('blur', function () {
                if (!this.value) {
                    this.parentElement.classList.remove('focused');
                }
            });

            // Real-time validation feedback
            input.addEventListener('input', function () {
                if (this.validity.valid) {
                    this.classList.remove('is-invalid');
                    this.classList.add('is-valid');
                } else if (this.value) {
                    this.classList.remove('is-valid');
                    this.classList.add('is-invalid');
                }
            });
        });

        // Form submission with loading state
        form.addEventListener('submit', function (e) {
            const submitBtn = this.querySelector('button[type="submit"]');
            if (submitBtn) {
                const originalText = submitBtn.textContent;
                submitBtn.disabled = true;
                submitBtn.innerHTML = '<span class="spinner-border spinner-border-sm me-2"></span>جاري الإرسال...';

                // Re-enable after 3 seconds if not redirected
                setTimeout(() => {
                    submitBtn.disabled = false;
                    submitBtn.textContent = originalText;
                }, 3000);
            }
        });
    });
}

// ==========================================
// Lazy Loading for Images
// ==========================================
function initLazyLoading() {
    if ('IntersectionObserver' in window) {
        const imageObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    if (img.dataset.src) {
                        img.src = img.dataset.src;
                        img.classList.add('fade-in');
                        observer.unobserve(img);
                    }
                }
            });
        });

        document.querySelectorAll('img[data-src]').forEach(img => {
            imageObserver.observe(img);
        });
    }
}

// ==========================================
// Scroll Animations
// ==========================================
function initScrollAnimations() {
    if ('IntersectionObserver' in window) {
        const animationObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('animate-in');
                }
            });
        }, {
            threshold: 0.1
        });

        document.querySelectorAll('.card, .activity-card, .section-title').forEach(el => {
            animationObserver.observe(el);
        });
    }
}

// ==========================================
// Active Nav Link
// ==========================================
function updateActiveNavLink() {
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll('.nav-link');

    navLinks.forEach(link => {
        const href = link.getAttribute('href');
        if (href === currentPath || (href !== '/' && currentPath.includes(href))) {
            link.classList.add('active');
        } else {
            link.classList.remove('active');
        }
    });
}

updateActiveNavLink();

// ==========================================
// Admin Helpers
// ==========================================
function viewMessage(id) {
    alert('ميزة قيد التطوير: عرض الرسالة رقم ' + id);
}

function viewVolunteer(id) {
    alert('ميزة قيد التطوير: عرض المتطوع رقم ' + id);
}

// ==========================================
// Dashboard Chart Initialization (if Chart.js is loaded)
// ==========================================
if (typeof Chart !== 'undefined') {
    initDashboardCharts();
}

function initDashboardCharts() {
    // Example: Activity chart
    const activityCtx = document.getElementById('activityChart');
    if (activityCtx) {
        new Chart(activityCtx, {
            type: 'line',
            data: {
                labels: ['يناير', 'فبراير', 'مارس', 'أبريل', 'مايو', 'يونيو'],
                datasets: [{
                    label: 'الأنشطة',
                    data: [12, 19, 15, 25, 22, 30],
                    borderColor: '#27ae60',
                    backgroundColor: 'rgba(39, 174, 96, 0.1)',
                    tension: 0.4
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false
            }
        });
    }
}
