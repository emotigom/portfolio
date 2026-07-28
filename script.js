const root = document.documentElement;
const themeButton = document.querySelector(".theme-toggle");
const themeIcon = themeButton?.querySelector("span");
const savedTheme = localStorage.getItem("portfolio-theme");
const systemPrefersLight = window.matchMedia("(prefers-color-scheme: light)").matches;

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

applyTheme(savedTheme ?? (systemPrefersLight ? "light" : "dark"));

themeButton?.addEventListener("click", () => {
  const nextTheme = root.classList.contains("light") ? "dark" : "light";
  localStorage.setItem("portfolio-theme", nextTheme);
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
    { rootMargin: "0px 0px -8%", threshold: 0.12 },
  );

  revealTargets.forEach((target) => observer.observe(target));
}
