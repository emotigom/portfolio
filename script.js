"use strict";

// Theme and menu behavior are optional; no script controls content visibility.
(() => {
  const root = document.documentElement;
  const button = document.querySelector(".theme-toggle");
  const preference = window.matchMedia("(prefers-color-scheme: light)");
  const storageKey = "portfolio-theme";
  let savedTheme = null;
  try {
    const value = localStorage.getItem(storageKey);
    if (value === "light" || value === "dark") savedTheme = value;
  } catch {
    // Storage may be blocked; the current page remains fully usable.
  }

  function applyTheme(theme) {
    const light = theme === "light";
    root.dataset.theme = light ? "light" : "dark";
    if (button) {
      button.setAttribute("aria-pressed", String(light));
      button.setAttribute("aria-label", light ? "어두운 테마로 전환" : "밝은 테마로 전환");
    }
  }

  applyTheme(savedTheme ?? (preference.matches ? "light" : "dark"));
  if (button) {
    button.hidden = false;
    button.addEventListener("click", () => {
      savedTheme = root.dataset.theme === "light" ? "dark" : "light";
      applyTheme(savedTheme);
      try { localStorage.setItem(storageKey, savedTheme); } catch { /* Optional persistence only. */ }
    });
  }

  function onPreferenceChange(event) {
    if (!savedTheme) applyTheme(event.matches ? "light" : "dark");
  }
  if (preference.addEventListener) preference.addEventListener("change", onPreferenceChange);
  else if (preference.addListener) preference.addListener(onPreferenceChange);

  const menu = document.querySelector(".mobile-menu");
  if (menu) {
    menu.querySelectorAll("nav a").forEach((link) => {
      link.addEventListener("click", () => {
        menu.open = false;
        const destination = document.querySelector(link.getAttribute("href"));
        if (destination) {
          // Keep keyboard focus out of the now-closed navigation.
          destination.setAttribute("tabindex", "-1");
          destination.focus({ preventScroll: true });
        }
      });
    });
    document.addEventListener("keydown", (event) => {
      if (event.key === "Escape" && menu.open) {
        menu.open = false;
        menu.querySelector("summary")?.focus();
      }
    });
    document.addEventListener("click", (event) => {
      if (menu.open && !menu.contains(event.target)) menu.open = false;
    });
  }
  const year = document.getElementById("year");
  if (year) year.textContent = String(new Date().getFullYear());
})();
