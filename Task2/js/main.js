/* ===== NovaClean Eco — Main JavaScript ===== */

document.addEventListener('DOMContentLoaded', () => {
  // --- Navigation ---
  const navLinks = document.querySelectorAll('[data-page]');
  const pages = document.querySelectorAll('.page');
  const header = document.querySelector('.header');
  const burger = document.querySelector('.header__burger');
  const nav = document.querySelector('.header__nav');

  function showPage(pageId) {
    pages.forEach(p => p.classList.remove('active'));
    navLinks.forEach(a => a.classList.remove('active'));

    const target = document.getElementById(pageId);
    if (target) {
      target.classList.add('active');
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    navLinks.forEach(a => {
      if (a.dataset.page === pageId) a.classList.add('active');
    });

    // Close mobile menu
    if (nav) nav.classList.remove('open');
    if (burger) burger.classList.remove('open');

    // Update URL hash without scroll
    history.replaceState(null, '', `#${pageId}`);
  }

  // Bind navigation clicks
  navLinks.forEach(link => {
    link.addEventListener('click', (e) => {
      e.preventDefault();
      showPage(link.dataset.page);
    });
  });

  // Handle hash on load
  const hash = window.location.hash.slice(1);
  if (hash && document.getElementById(hash)) {
    showPage(hash);
  }

  // Burger menu toggle
  if (burger) {
    burger.addEventListener('click', () => {
      burger.classList.toggle('open');
      nav.classList.toggle('open');
    });
  }

  // --- Header scroll effect ---
  let lastScroll = 0;
  window.addEventListener('scroll', () => {
    const scrollY = window.scrollY;
    if (scrollY > 50) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
    lastScroll = scrollY;
  });

  // --- Cookie Banner ---
  const cookieBanner = document.getElementById('cookieBanner');
  const cookieAccept = document.getElementById('cookieAccept');
  const cookieDecline = document.getElementById('cookieDecline');

  if (!localStorage.getItem('novaclean_cookies')) {
    setTimeout(() => {
      cookieBanner.classList.add('show');
    }, 1500);
  }

  if (cookieAccept) {
    cookieAccept.addEventListener('click', () => {
      localStorage.setItem('novaclean_cookies', 'accepted');
      cookieBanner.classList.remove('show');
    });
  }

  if (cookieDecline) {
    cookieDecline.addEventListener('click', () => {
      localStorage.setItem('novaclean_cookies', 'declined');
      cookieBanner.classList.remove('show');
    });
  }

  // --- Scroll animations (Intersection Observer) ---
  const fadeElements = document.querySelectorAll('.fade-up');
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, {
    threshold: 0.15,
    rootMargin: '0px 0px -40px 0px'
  });

  fadeElements.forEach(el => observer.observe(el));

  // --- Form stub handling ---
  const forms = document.querySelectorAll('form[data-stub]');
  forms.forEach(form => {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      showToast('Дякуємо! Ваше повідомлення отримано. Ми зв\'яжемося з вами найближчим часом.');
      form.reset();
    });
  });

  // --- Toast notification ---
  function showToast(message) {
    const toast = document.getElementById('toast');
    const toastMsg = document.getElementById('toastMessage');
    if (toast && toastMsg) {
      toastMsg.textContent = message;
      toast.classList.add('show');
      setTimeout(() => {
        toast.classList.remove('show');
      }, 4000);
    }
  }

  // --- Policy tabs ---
  const policyTabs = document.querySelectorAll('.policy-tab');
  const policySections = document.querySelectorAll('.policy-section');

  policyTabs.forEach(tab => {
    tab.addEventListener('click', () => {
      policyTabs.forEach(t => t.classList.remove('active'));
      policySections.forEach(s => s.classList.remove('active'));
      tab.classList.add('active');
      const target = document.getElementById(tab.dataset.target);
      if (target) target.classList.add('active');
    });
  });

  // --- Make showPage globally accessible ---
  window.showPage = showPage;

  // --- Parallax Leaves ---
  const parallaxLeaves = document.querySelectorAll('.parallax-leaf');
  if (parallaxLeaves.length > 0) {
    window.addEventListener('scroll', () => {
      const scrollY = window.scrollY;
      parallaxLeaves.forEach(leaf => {
        const speed = parseFloat(leaf.dataset.speed) || 0.1;
        const yPos = scrollY * speed;
        leaf.style.setProperty('--y', `${yPos}px`);
      });
    }, { passive: true });
  }
});
