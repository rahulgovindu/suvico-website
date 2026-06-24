/* Suvico International — site interactions (vanilla, no deps) */
(function () {
  "use strict";

  /* Sticky header shadow */
  var header = document.querySelector(".site-header");
  if (header) {
    var onScroll = function () {
      header.classList.toggle("scrolled", window.scrollY > 8);
    };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  /* Mobile menu */
  var burger = document.querySelector(".hamburger");
  var navMenu = document.querySelector(".nav-menu");
  var backdrop = document.querySelector(".nav-backdrop");
  function closeMenu() {
    if (!navMenu) return;
    navMenu.classList.remove("open");
    if (backdrop) backdrop.classList.remove("open");
    if (burger) { burger.classList.remove("open"); burger.setAttribute("aria-expanded", "false"); }
    document.body.style.overflow = "";
  }
  function toggleMenu() {
    if (!navMenu) return;
    var open = navMenu.classList.toggle("open");
    if (backdrop) backdrop.classList.toggle("open", open);
    burger.classList.toggle("open", open);
    burger.setAttribute("aria-expanded", open ? "true" : "false");
    document.body.style.overflow = open ? "hidden" : "";
  }
  if (burger) burger.addEventListener("click", toggleMenu);
  if (backdrop) backdrop.addEventListener("click", closeMenu);
  document.addEventListener("keydown", function (e) { if (e.key === "Escape") closeMenu(); });
  /* On mobile, let a parent menu item toggle its submenu */
  document.querySelectorAll(".nav-menu .has-sub > a").forEach(function (a) {
    a.addEventListener("click", function (e) {
      if (window.matchMedia("(max-width:820px)").matches) {
        var sub = a.parentElement.querySelector(".submenu");
        if (sub) { e.preventDefault(); sub.style.display = sub.style.display === "block" ? "" : "block"; }
      }
    });
  });

  /* Reveal on scroll */
  var reveals = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window && reveals.length) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); }
      });
    }, { threshold: 0.12 });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add("in"); });
  }

  /* Animated stat counters */
  var counted = false;
  var statsEl = document.querySelector(".stats");
  function runCounters() {
    if (counted || !statsEl) return;
    var r = statsEl.getBoundingClientRect();
    if (r.top > window.innerHeight || r.bottom < 0) return;
    counted = true;
    document.querySelectorAll("[data-count]").forEach(function (el) {
      var target = parseFloat(el.getAttribute("data-count"));
      var suffix = el.getAttribute("data-suffix") || "";
      var dur = 1400, start = null;
      function step(ts) {
        if (!start) start = ts;
        var p = Math.min((ts - start) / dur, 1);
        var val = Math.floor(p * target);
        el.textContent = val + suffix;
        if (p < 1) requestAnimationFrame(step); else el.textContent = target + suffix;
      }
      requestAnimationFrame(step);
    });
  }
  window.addEventListener("scroll", runCounters, { passive: true });
  runCounters();

  /* Contact form — front-end UX (demo: no live backend in this build) */
  var form = document.getElementById("contactForm");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var note = document.getElementById("formNote");
      if (!form.checkValidity()) { form.reportValidity(); return; }
      if (note) {
        note.hidden = false;
        note.textContent = "Thank you — your enquiry is ready to send. (Connect this form to send.php on the live server.)";
        note.scrollIntoView({ behavior: "smooth", block: "center" });
      }
      form.reset();
    });
  }

  /* Footer year */
  var y = document.getElementById("year");
  if (y) y.textContent = new Date().getFullYear();
})();
