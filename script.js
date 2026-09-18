const root = document.documentElement;
const themeButton = document.querySelector(".theme-toggle");
const themeIcon = themeButton?.querySelector("span");
const systemPrefersLight = window.matchMedia("(prefers-color-scheme: light)").matches;

function readSavedTheme() {
  try {
    return localStorage.getItem("portfolio-theme");
  } catch {
    return null;
  }
}

function saveTheme(theme) {
  try {
    localStorage.setItem("portfolio-theme", theme);
  } catch {
    // Theme still works for the current page when storage is unavailable.
  }
}

function applyTheme(theme) {
  const isLight = theme === "light";
  root.classList.toggle("light", isLight);

  if (!themeButton || !themeIcon) return;

  themeButton.setAttribute("aria-pressed", String(isLight));
  themeButton.setAttribute(
    "aria-label",
    isLight ? "어두운 테마로 전환" : "밝은 테마로 전환",
  );
  themeIcon.textContent = isLight ? "☀" : "☾";
}

applyTheme(readSavedTheme() ?? (systemPrefersLight ? "light" : "dark"));

themeButton?.addEventListener("click", () => {
  const nextTheme = root.classList.contains("light") ? "dark" : "light";
  saveTheme(nextTheme);
  applyTheme(nextTheme);
});

const year = document.getElementById("year");
if (year) year.textContent = String(new Date().getFullYear());

const revealTargets = document.querySelectorAll(".reveal");
const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

if (reduceMotion || !("IntersectionObserver" in window)) {
  revealTargets.forEach((target) => target.classList.add("is-visible"));
} else {
  const observer = new IntersectionObserver(
    (entries, currentObserver) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("is-visible");
        currentObserver.unobserve(entry.target);
      });
    },
    { rootMargin: "0px 0px -6%", threshold: 0.08 },
  );

  revealTargets.forEach((target) => observer.observe(target));
}
