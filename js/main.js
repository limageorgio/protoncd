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
    let mobileMenu = document.getElementById('mobile-menu');

    function lockBodyScroll(lock) {
        document.body.style.overflow = lock ? 'hidden' : '';
    }

    function closeMobileMenu() {
        if (!mobileMenu) return;
        mobileMenu.classList.remove('active');
        mobileMenu.setAttribute('aria-hidden', 'true');
        lockBodyScroll(false);
    }

    function ensureMobileMenu() {
        if (mobileMenu) return mobileMenu;

        const navLinks = document.querySelector('#main-nav .nav-links');
        if (!navLinks) return null;

        mobileMenu = document.createElement('div');
        mobileMenu.className = 'nav-mobile-menu';
        mobileMenu.id = 'mobile-menu';
        mobileMenu.setAttribute('aria-hidden', 'true');

        const closeButton = document.createElement('button');
        closeButton.className = 'nav-mobile-close';
        closeButton.id = 'mobile-close';
        closeButton.type = 'button';
        closeButton.setAttribute('aria-label', 'Fechar menu');
        closeButton.innerHTML = '&times;';
        closeButton.addEventListener('click', closeMobileMenu);

        mobileMenu.appendChild(closeButton);

        navLinks.querySelectorAll('a').forEach(link => {
            const mobileLink = link.cloneNode(true);
            mobileLink.classList.add('mobile-link');
            mobileLink.addEventListener('click', closeMobileMenu);
            mobileMenu.appendChild(mobileLink);
        });

        mobileMenu.addEventListener('click', (event) => {
            if (event.target === mobileMenu) {
                closeMobileMenu();
            }
        });

        document.body.appendChild(mobileMenu);
        return mobileMenu;
    }

    const existingMobileClose = document.getElementById('mobile-close');
    if (existingMobileClose) {
        existingMobileClose.addEventListener('click', closeMobileMenu);
    }

    document.querySelectorAll('.mobile-link').forEach(link => {
        link.addEventListener('click', closeMobileMenu);
    });

    if (mobileToggle) {
        mobileToggle.addEventListener('click', () => {
            const menu = ensureMobileMenu();
            if (!menu) return;

            const isActive = menu.classList.contains('active');
            if (isActive) {
                closeMobileMenu();
                return;
            }

            menu.classList.add('active');
            menu.setAttribute('aria-hidden', 'false');
            lockBodyScroll(true);
        });
    }

    document.addEventListener('keydown', (event) => {
        if (event.key === 'Escape') {
            closeMobileMenu();
        }
    });

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

    // ========== GA4 CUSTOM EVENT TRACKING ==========
    // Helper: envia evento para GA4 via gtag
    function trackEvent(eventName, params) {
        if (typeof gtag === 'function') {
            gtag('event', eventName, params);
        }
    }

    // Mapa de telefones → profissional responsável
    const PHONE_TO_PROFESSIONAL = {
        '5562992852704': 'Eng. Georgio Lima',
        '5516982203631': 'Eng. Marina Saccardo',
        '558196537023': 'Eng. Luciene Marques',
        '5562992346424': 'Eng. Jose Raimenson'
    };

    // Extrai o número do telefone da URL do WhatsApp
    function extractPhone(url) {
        const match = url.match(/phone=(\d+)/);
        return match ? match[1] : '';
    }

    // Retorna o nome do profissional pelo número
    function getProfessional(url) {
        const phone = extractPhone(url);
        return PHONE_TO_PROFESSIONAL[phone] || 'Desconhecido (' + phone + ')';
    }

    // — 1. WHATSAPP CLICKS (todos os links de WhatsApp, separados por profissional) —
    document.querySelectorAll('a[href*="api.whatsapp.com"], a[href*="wa.me"]').forEach(link => {
        link.addEventListener('click', function () {
            const pageTitle = document.title.split('|')[0].trim();
            const linkText = this.textContent.trim().substring(0, 50);
            const section = this.closest('section, footer, nav, header');
            const sectionId = section ? (section.id || section.className.split(' ')[0]) : 'unknown';
            const phone = extractPhone(this.href);
            const professional = getProfessional(this.href);

            trackEvent('whatsapp_click', {
                event_category: 'conversao',
                profissional: professional,
                telefone: phone,
                page_title: pageTitle,
                link_text: linkText,
                link_url: this.href,
                page_section: sectionId,
                page_location: window.location.pathname
            });
        });
    });

    // — 2. PHONE CALL CLICKS (links tel:, separados por profissional) —
    document.querySelectorAll('a[href^="tel:"]').forEach(link => {
        link.addEventListener('click', function () {
            const phone = this.href.replace('tel:', '');
            const professional = PHONE_TO_PROFESSIONAL[phone] || 'Desconhecido (' + phone + ')';

            trackEvent('phone_click', {
                event_category: 'conversao',
                profissional: professional,
                phone_number: phone,
                page_title: document.title.split('|')[0].trim(),
                page_location: window.location.pathname
            });
        });
    });

    // — 3. EMAIL CLICKS (links mailto:, separados por profissional) —
    const EMAIL_TO_PROFESSIONAL = {
        'lima.georgio.eng@gmail.com': 'Eng. Georgio Lima',
        'ma.saccardoengenheira@gmail.com': 'Eng. Marina Saccardo',
        'luciene.silva.eng@gmail.com': 'Eng. Luciene Marques',
        'raimensosilva@gmail.com': 'Eng. Jose Raimenson'
    };

    document.querySelectorAll('a[href^="mailto:"]').forEach(link => {
        link.addEventListener('click', function () {
            const email = this.href.replace('mailto:', '').toLowerCase();
            const professional = EMAIL_TO_PROFESSIONAL[email] || 'Desconhecido (' + email + ')';

            trackEvent('email_click', {
                event_category: 'conversao',
                profissional: professional,
                email_address: email,
                page_title: document.title.split('|')[0].trim(),
                page_location: window.location.pathname
            });
        });
    });

    // — 4. FORM SUBMISSION (formulário WhatsApp) —
    const whatsappFormBtn = document.getElementById('enviar-whatsapp');
    if (whatsappFormBtn) {
        whatsappFormBtn.addEventListener('click', function () {
            const name = document.getElementById('name');
            const email = document.getElementById('email');
            const sistema = document.getElementById('sistema');

            // Detecta para qual profissional o formulário vai (pelo action do form ou número hardcoded na página)
            const formParent = this.closest('form') || this.closest('section');
            const formWhatsappLink = formParent ? formParent.querySelector('a[href*="api.whatsapp.com"]') : null;
            let formProfessional = 'Eng. Georgio Lima'; // Default: formulário central vai para Georgio
            if (formWhatsappLink) {
                formProfessional = getProfessional(formWhatsappLink.href);
            }

            if (name && name.value.trim()) {
                trackEvent('generate_lead', {
                    event_category: 'conversao',
                    profissional: formProfessional,
                    form_type: 'whatsapp_form',
                    service_type: sistema ? sistema.value : 'geral',
                    page_title: document.title.split('|')[0].trim(),
                    page_location: window.location.pathname,
                    has_email: email && email.value.trim() ? 'sim' : 'nao'
                });
            }
        });
    }

    // — 5. CTA BUTTON CLICKS (botões principais de conversão) —
    document.querySelectorAll('.btn-primary, .btn-whatsapp, .nav-cta, [class*="btn-cta"]').forEach(btn => {
        // Ignora botões que já têm tracking específico (WhatsApp, tel, mailto)
        if (btn.href && (btn.href.includes('whatsapp') || btn.href.startsWith('tel:') || btn.href.startsWith('mailto:'))) return;
        btn.addEventListener('click', function () {
            trackEvent('cta_click', {
                event_category: 'engajamento',
                cta_text: this.textContent.trim().substring(0, 50),
                cta_url: this.href || 'button',
                page_title: document.title.split('|')[0].trim(),
                page_location: window.location.pathname
            });
        });
    });

    // — 6. FAQ INTERACTIONS —
    document.querySelectorAll('.faq-question').forEach(faqBtn => {
        faqBtn.addEventListener('click', function () {
            const questionText = this.textContent.trim().substring(0, 100);
            trackEvent('faq_interaction', {
                event_category: 'engajamento',
                faq_question: questionText,
                page_title: document.title.split('|')[0].trim(),
                page_location: window.location.pathname
            });
        });
    });

    // — 7. SCROLL DEPTH TRACKING (25%, 50%, 75%, 100%) —
    const scrollThresholds = [25, 50, 75, 100];
    const scrollFired = {};
    window.addEventListener('scroll', function () {
        const scrollPercent = Math.round((window.scrollY / (document.documentElement.scrollHeight - window.innerHeight)) * 100);
        scrollThresholds.forEach(threshold => {
            if (scrollPercent >= threshold && !scrollFired[threshold]) {
                scrollFired[threshold] = true;
                trackEvent('scroll_depth', {
                    event_category: 'engajamento',
                    percent_scrolled: threshold,
                    page_title: document.title.split('|')[0].trim(),
                    page_location: window.location.pathname
                });
            }
        });
    }, { passive: true });

    // — 8. OUTBOUND LINK CLICKS —
    document.querySelectorAll('a[href^="http"]').forEach(link => {
        if (!link.href.includes(window.location.hostname)) {
            link.addEventListener('click', function () {
                trackEvent('outbound_click', {
                    event_category: 'engajamento',
                    link_url: this.href,
                    link_text: this.textContent.trim().substring(0, 50),
                    page_location: window.location.pathname
                });
            });
        }
    });

    // — 9. SERVICE CARD / SECTION VISIBILITY (quais serviços o usuário vê) —
    const serviceCards = document.querySelectorAll('.service-card, .card, [class*="servico"]');
    if (serviceCards.length > 0 && 'IntersectionObserver' in window) {
        const serviceObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const title = entry.target.querySelector('h2, h3, h4');
                    const titleText = title ? title.textContent.trim().substring(0, 80) : 'sem-titulo';
                    trackEvent('service_view', {
                        event_category: 'engajamento',
                        service_name: titleText,
                        page_title: document.title.split('|')[0].trim(),
                        page_location: window.location.pathname
                    });
                    serviceObserver.unobserve(entry.target);
                }
            });
        }, { threshold: 0.5 });
        serviceCards.forEach(card => serviceObserver.observe(card));
    }

    // — 10. TIME ON PAGE (engagement milestones: 30s, 60s, 120s, 300s) —
    const timeMilestones = [30, 60, 120, 300];
    const timeFired = {};
    timeMilestones.forEach(seconds => {
        setTimeout(() => {
            if (!document.hidden) {
                timeFired[seconds] = true;
                trackEvent('time_on_page', {
                    event_category: 'engajamento',
                    seconds_on_page: seconds,
                    page_title: document.title.split('|')[0].trim(),
                    page_location: window.location.pathname
                });
            }
        }, seconds * 1000);
    });

})();
