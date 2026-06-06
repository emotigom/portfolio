const root = document.documentElement;
const button = document.querySelector(".theme-toggle");
const savedTheme = localStorage.getItem("portfolio-theme");

if (savedTheme === "light") {
  root.classList.add("light");
  button.textContent = "☀";
}

button.addEventListener("click", () => {
  root.classList.toggle("light");
  const isLight = root.classList.contains("light");
  localStorage.setItem("portfolio-theme", isLight ? "light" : "dark");
  button.textContent = isLight ? "☀" : "☾";
});

document.getElementById("year").textContent = new Date().getFullYear();
