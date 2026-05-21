/**
 * Aarohan NGO - Homepage Interactions
 */

document.addEventListener('DOMContentLoaded', function() {
    'use strict';

    // ========================================
    // HERO SLIDER
    // ========================================
    const slides = document.querySelectorAll('.hero-slide');
    const dotsContainer = document.getElementById('sliderDots');
    const prevBtn = document.getElementById('sliderPrev');
    const nextBtn = document.getElementById('sliderNext');
    let currentSlide = 0;
    let autoSlideInterval;

    // Create dots
    slides.forEach((_, index) => {
        const dot = document.createElement('span');
        dot.classList.add('slider-dot');
        if (index === 0) dot.classList.add('active');
        dot.addEventListener('click', () => goToSlide(index));
        dotsContainer.appendChild(dot);
    });

    const dots = document.querySelectorAll('.slider-dot');

    function goToSlide(index) {
        slides[currentSlide].classList.remove('active');
        dots[currentSlide].classList.remove('active');

        currentSlide = index;

        if (currentSlide >= slides.length) currentSlide = 0;
        if (currentSlide < 0) currentSlide = slides.length - 1;

        slides[currentSlide].classList.add('active');
        dots[currentSlide].classList.add('active');
    }

    function nextSlide() {
        goToSlide(currentSlide + 1);
    }

    function prevSlide() {
        goToSlide(currentSlide - 1);
    }

    function startAutoSlide() {
        autoSlideInterval = setInterval(nextSlide, 5000);
    }

    function stopAutoSlide() {
        clearInterval(autoSlideInterval);
    }

    // Event listeners
    if (prevBtn) prevBtn.addEventListener('click', () => { stopAutoSlide(); prevSlide(); startAutoSlide(); });
    if (nextBtn) nextBtn.addEventListener('click', () => { stopAutoSlide(); nextSlide(); startAutoSlide(); });

    // Start auto slide
    startAutoSlide();

    // Pause on hover
    const heroSection = document.querySelector('.hero');
    if (heroSection) {
        heroSection.addEventListener('mouseenter', stopAutoSlide);
        heroSection.addEventListener('mouseleave', startAutoSlide);
    }

    // ========================================
    // PARTNERS SLIDER
    // ========================================
    const partnerSlides = document.querySelectorAll('.partner-slide');
    const partnerIndicators = document.getElementById('partnerSliderIndicators');
    const partnerPrevBtn = document.getElementById('partnerSliderPrev');
    const partnerNextBtn = document.getElementById('partnerSliderNext');
    let currentPartnerSlide = 0;

    // Create indicators
    partnerSlides.forEach((_, index) => {
        const indicator = document.createElement('span');
        indicator.classList.add('slider-indicator');
        if (index === 0) indicator.classList.add('active');
        indicator.addEventListener('click', () => goToPartnerSlide(index));
        partnerIndicators.appendChild(indicator);
    });

    const partnerDots = document.querySelectorAll('.slider-indicator');

    function goToPartnerSlide(index) {
        partnerSlides[currentPartnerSlide].classList.remove('active');
        partnerDots[currentPartnerSlide].classList.remove('active');

        currentPartnerSlide = index;

        if (currentPartnerSlide >= partnerSlides.length) currentPartnerSlide = 0;
        if (currentPartnerSlide < 0) currentPartnerSlide = partnerSlides.length - 1;

        partnerSlides[currentPartnerSlide].classList.add('active');
        partnerDots[currentPartnerSlide].classList.add('active');
    }

    function nextPartnerSlide() {
        goToPartnerSlide(currentPartnerSlide + 1);
    }

    function prevPartnerSlide() {
        goToPartnerSlide(currentPartnerSlide - 1);
    }

    // Event listeners
    if (partnerPrevBtn) partnerPrevBtn.addEventListener('click', () => { prevPartnerSlide(); });
    if (partnerNextBtn) partnerNextBtn.addEventListener('click', () => { nextPartnerSlide(); });

    // Auto-rotate partners slider (every 4 seconds)
    setInterval(nextPartnerSlide, 4000);

    // ========================================
    // MOBILE MENU TOGGLE
    // ========================================
    const hamburger = document.getElementById('hamburger');
    const nav = document.getElementById('nav');

    hamburger.addEventListener('click', () => {
        hamburger.classList.toggle('active');
        nav.classList.toggle('active');
        document.body.style.overflow = nav.classList.contains('active') ? 'hidden' : '';
    });

    document.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', () => {
            if (!link.closest('.dropdown')) {
                hamburger.classList.remove('active');
                nav.classList.remove('active');
                document.body.style.overflow = '';
            }
        });
    });

    // Close nav on outside tap
    document.addEventListener('click', (e) => {
        if (nav.classList.contains('active') &&
            !nav.contains(e.target) &&
            !hamburger.contains(e.target)) {
            nav.classList.remove('active');
            hamburger.classList.remove('active');
            document.body.style.overflow = '';
        }
    });

    // Mobile: tap dropdown parent to toggle submenu
    document.querySelectorAll('.dropdown > .nav-link').forEach(link => {
        link.addEventListener('click', (e) => {
            if (window.innerWidth <= 768) {
                e.preventDefault();
                const parent = link.parentElement;
                document.querySelectorAll('.dropdown').forEach(d => {
                    if (d !== parent) d.classList.remove('open');
                });
                parent.classList.toggle('open');
            }
        });
    });



    // ========================================
    // SMOOTH SCROLL
    // ========================================
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                const headerHeight = header.offsetHeight;
                const targetPosition = target.offsetTop - headerHeight;
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });

    // ========================================
    // COUNTER ANIMATION
    // ========================================
    const counters = document.querySelectorAll('.stats-number[data-count]');
    let countersAnimated = false;

    function animateCounter(counter) {
        const target = parseInt(counter.getAttribute('data-count'));
        if (!target) return;

        const duration = 2000;
        const increment = target / (duration / 16);
        let current = 0;

        function updateCounter() {
            current += increment;
            if (current < target) {
                counter.textContent = Math.floor(current).toLocaleString();
                requestAnimationFrame(updateCounter);
            } else {
                counter.textContent = target.toLocaleString();
            }
        }

        updateCounter();
    }

    const statsSection = document.querySelector('.impact-stats');
    if (statsSection) {
        const observer = new IntersectionObserver((entries) => {
            if (entries[0].isIntersecting && !countersAnimated) {
                countersAnimated = true;
                counters.forEach(counter => animateCounter(counter));
            }
        }, { threshold: 0.3 });

        observer.observe(statsSection);
    }

    // ========================================
    // INITIALS AVATARS FOR BOARD MEMBERS
    // ========================================
    document.querySelectorAll('.team-img[data-initials]').forEach(img => {
        const initials = img.getAttribute('data-initials');
        const avatar = document.createElement('div');
        avatar.className = 'avatar-initials';
        avatar.textContent = initials;
        img.parentNode.replaceChild(avatar, img);
    });

    // Also handle founder cards with same pattern
    document.querySelectorAll('.founder-img[data-initials]').forEach(img => {
        const initials = img.getAttribute('data-initials');
        const avatar = document.createElement('div');
        avatar.className = 'avatar-initials';
        avatar.style.cssText = 'width:60px;height:60px;font-size:1rem;margin:0;flex-shrink:0;';
        avatar.textContent = initials;
        img.parentNode.replaceChild(avatar, img);
    });

    // ========================================
    // SCROLL ANIMATIONS
    // ========================================
    const fadeElements = document.querySelectorAll('.program-card, .method-card, .team-card, .award-item');

    const fadeObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, { threshold: 0.1 });

    fadeElements.forEach((el, index) => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(20px)';
        el.style.transition = `all 0.5s ease ${index * 0.1}s`;
        fadeObserver.observe(el);
    });

    // ========================================
    // FORM HANDLING
    // ========================================
    const contactForm = document.querySelector('.contact-form');

    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();

            const submitBtn = this.querySelector('button[type="submit"]');
            const originalText = submitBtn.textContent;

            submitBtn.textContent = 'Sending...';
            submitBtn.disabled = true;

            setTimeout(() => {
                submitBtn.textContent = 'Message Sent!';
                submitBtn.style.background = 'var(--accent)';

                setTimeout(() => {
                    this.reset();
                    submitBtn.textContent = originalText;
                    submitBtn.disabled = false;
                    submitBtn.style.background = '';
                }, 2000);
            }, 1500);
        });
    }

    // ========================================
    // KEYBOARD ACCESSIBILITY
    // ========================================
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && nav.classList.contains('active')) {
            hamburger.classList.remove('active');
            nav.classList.remove('active');
        }
    });

    console.log('Aarohan NGO Homepage initialized');
});