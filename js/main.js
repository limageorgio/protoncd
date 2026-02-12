/**
 * Proton Engenharia — v2 Design System
 * Main JavaScript — shared across all pages
 */

(function () {
    'use strict';

    // ========== NAV SCROLL EFFECT ==========
    const nav = document.getElementById('main-nav');
    if (nav) {
        window.addEventListener('scroll', () => {
            nav.classList.toggle('scrolled', window.scrollY > 50);
        }, { passive: true });
    }

    // ========== MOBILE MENU ==========
    const mobileToggle = document.getElementById('mobile-toggle');
    const mobileMenu = document.getElementById('mobile-menu');
    const mobileClose = document.getElementById('mobile-close');

    if (mobileToggle && mobileMenu) {
        mobileToggle.addEventListener('click', () => {
            mobileMenu.classList.add('active');
            document.body.style.overflow = 'hidden';
        });

        if (mobileClose) {
            mobileClose.addEventListener('click', () => {
                mobileMenu.classList.remove('active');
                document.body.style.overflow = '';
            });
        }

        document.querySelectorAll('.mobile-link').forEach(link => {
            link.addEventListener('click', () => {
                mobileMenu.classList.remove('active');
                document.body.style.overflow = '';
            });
        });
    }

    // ========== SMOOTH SCROLL ==========
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const href = this.getAttribute('href');
            if (href === '#') return;
            const target = document.querySelector(href);
            if (target) {
                e.preventDefault();
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    });

    // ========== FAQ ACCORDION ==========
    window.toggleFaq = function (el) {
        const item = el.closest('.faq-item');
        if (!item) return;
        const isActive = item.classList.contains('active');
        // Close all
        document.querySelectorAll('.faq-item.active').forEach(i => i.classList.remove('active'));
        // Toggle current
        if (!isActive) item.classList.add('active');
    };

    // ========== SCROLL REVEAL (IntersectionObserver) ==========
    const revealSelector = '.reveal, .reveal-left, .reveal-right, .reveal-scale';
    const revealElements = document.querySelectorAll(revealSelector);

    if (revealElements.length > 0 && 'IntersectionObserver' in window) {
        const revealObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                }
            });
        }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

        revealElements.forEach(el => revealObserver.observe(el));
    } else {
        // Fallback: show all immediately
        revealElements.forEach(el => el.classList.add('visible'));
    }

    // ========== WHATSAPP FORM ==========
    const whatsappBtn = document.getElementById('enviar-whatsapp');
    if (whatsappBtn) {
        whatsappBtn.addEventListener('click', function () {
            const getValue = (id) => {
                const el = document.getElementById(id);
                return el ? el.value.trim() : '';
            };

            const name = getValue('name');
            const email = getValue('email');
            const phone = getValue('phone');
            const condo = getValue('condominio');
            const sistema = getValue('sistema');
            const message = getValue('message');

            // Basic validation
            if (!name || !email || !phone) {
                alert('Por favor, preencha nome, e-mail e telefone.');
                return;
            }

            // Get page title for context
            const pageTitle = document.title.split('|')[0].trim();

            let msg = '📋 SOLICITAÇÃO — ' + pageTitle + '\n\n';
            msg += 'Nome: ' + name + '\n';
            msg += 'Email: ' + email + '\n';
            msg += 'Telefone: ' + phone + '\n';
            if (condo) msg += 'Edifício: ' + condo + '\n';
            if (sistema) msg += 'Sistema: ' + sistema + '\n';
            if (message) msg += '\nMensagem:\n' + message;

            window.open('https://api.whatsapp.com/send?phone=+5562992852704&text=' + encodeURIComponent(msg));
        });
    }

    // ========== BACK TO TOP ==========
    const backToTop = document.getElementById('back-to-top');
    if (backToTop) {
        window.addEventListener('scroll', () => {
            backToTop.classList.toggle('visible', window.scrollY > 600);
        }, { passive: true });

        backToTop.addEventListener('click', () => {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }

})();
