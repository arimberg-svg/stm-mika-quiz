/* Mini self-check quizzes on presentation pages */
(function () {
  function grade(form) {
    const items = [...form.querySelectorAll(".q-item")];
    let correct = 0;
    items.forEach((item) => {
      const answer = item.dataset.answer;
      const checked = item.querySelector('input[type="radio"]:checked');
      item.querySelectorAll("label").forEach((lab) => {
        lab.classList.remove("is-correct", "is-wrong");
      });
      if (!checked) return;
      const val = checked.value;
      const lab = checked.closest("label");
      if (val === answer) {
        correct += 1;
        lab.classList.add("is-correct");
      } else {
        lab.classList.add("is-wrong");
        const right = item.querySelector(`input[value="${answer}"]`);
        if (right) right.closest("label").classList.add("is-correct");
      }
    });
    const total = items.length;
    const out = form.querySelector(".quiz-result");
    const pct = total ? correct / total : 0;
    out.classList.remove("ok", "mid", "bad");
    if (pct >= 0.8) {
      out.classList.add("ok");
      out.textContent = `Отлично: ${correct} из ${total}. Можно идти дальше.`;
    } else if (pct >= 0.5) {
      out.classList.add("mid");
      out.textContent = `Неплохо: ${correct} из ${total}. Перечитайте блок выше и попробуйте ещё.`;
    } else {
      out.classList.add("bad");
      out.textContent = `Повторите материал: ${correct} из ${total}.`;
    }
  }

  document.querySelectorAll("[data-mini-quiz]").forEach((form) => {
    form.addEventListener("submit", (e) => {
      e.preventDefault();
      grade(form);
    });
    const reset = form.querySelector("[data-reset]");
    if (reset) {
      reset.addEventListener("click", () => {
        form.reset();
        form.querySelectorAll("label").forEach((lab) => {
          lab.classList.remove("is-correct", "is-wrong");
        });
        const out = form.querySelector(".quiz-result");
        out.textContent = "";
        out.classList.remove("ok", "mid", "bad");
      });
    }
  });

  // mark active nav link
  const path = location.pathname.split("/").pop() || "index.html";
  document.querySelectorAll(".nav-links a").forEach((a) => {
    const href = a.getAttribute("href");
    if (href === path || (path === "" && href === "index.html")) {
      a.classList.add("active");
    }
  });
})();
