/* Training site: nav + self-check quiz */
(function () {
  function gradeForm(form) {
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
    const out = form.querySelector(".quiz-result") || document.getElementById("quiz-result");
    if (!out) return;
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

  function renderQuiz(root) {
    const raw = root.getAttribute("data-questions");
    if (!raw) return;
    let questions;
    try {
      questions = JSON.parse(raw);
    } catch (e) {
      return;
    }
    const host = root.querySelector("#quiz-questions") || root;
    host.innerHTML = "";
    const form = document.createElement("form");
    form.setAttribute("data-mini-quiz", "");
    form.id = "quiz-form";
    questions.forEach((q, i) => {
      const item = document.createElement("div");
      item.className = "q-item";
      item.dataset.answer = q.answer;
      const h = document.createElement("h3");
      h.textContent = `${i + 1}. ${q.q}`;
      item.appendChild(h);
      const opts = document.createElement("div");
      opts.className = "q-options";
      Object.entries(q.options).forEach(([key, label]) => {
        const lab = document.createElement("label");
        const input = document.createElement("input");
        input.type = "radio";
        input.name = `q${i}`;
        input.value = key;
        lab.appendChild(input);
        lab.appendChild(document.createTextNode(" " + label));
        opts.appendChild(lab);
      });
      item.appendChild(opts);
      form.appendChild(item);
    });
    host.appendChild(form);

    let result = document.getElementById("quiz-result");
    if (!result) {
      result = document.createElement("div");
      result.className = "quiz-result";
      result.id = "quiz-result";
      result.setAttribute("aria-live", "polite");
      const actions = root.querySelector(".quiz-actions");
      if (actions && actions.parentNode) {
        actions.parentNode.insertBefore(result, actions.nextSibling);
      } else {
        form.appendChild(result);
      }
    }

    const check = document.getElementById("quiz-check");
    const reset = document.getElementById("quiz-reset");
    if (check) {
      check.addEventListener("click", () => gradeForm(form));
    }
    if (reset) {
      reset.addEventListener("click", () => {
        form.reset();
        form.querySelectorAll("label").forEach((lab) => {
          lab.classList.remove("is-correct", "is-wrong");
        });
        result.textContent = "";
        result.classList.remove("ok", "mid", "bad");
      });
    }
  }

  document.querySelectorAll("[data-mini-quiz]").forEach((form) => {
    form.addEventListener("submit", (e) => {
      e.preventDefault();
      gradeForm(form);
    });
    const reset = form.querySelector("[data-reset]");
    if (reset) {
      reset.addEventListener("click", () => {
        form.reset();
        form.querySelectorAll("label").forEach((lab) => {
          lab.classList.remove("is-correct", "is-wrong");
        });
        const out = form.querySelector(".quiz-result");
        if (out) {
          out.textContent = "";
          out.classList.remove("ok", "mid", "bad");
        }
      });
    }
  });

  const quizRoot = document.getElementById("quiz");
  if (quizRoot && quizRoot.getAttribute("data-questions")) {
    renderQuiz(quizRoot);
  }

  const path = location.pathname.split("/").pop() || "index.html";
  document.querySelectorAll(".nav-links a").forEach((a) => {
    const href = a.getAttribute("href");
    if (href === path || (path === "" && href === "index.html")) {
      a.classList.add("active");
    }
  });

  document.querySelectorAll("[data-tabs]").forEach((root) => {
    const buttons = [...root.querySelectorAll(".tab-btn")];
    const panels = [...root.querySelectorAll(".tab-panel")];
    function activate(id) {
      buttons.forEach((btn) => {
        const on = btn.getAttribute("data-tab") === id;
        btn.classList.toggle("is-active", on);
        btn.setAttribute("aria-selected", on ? "true" : "false");
      });
      panels.forEach((panel) => {
        const on = panel.id === "tab-" + id;
        panel.classList.toggle("is-active", on);
        if (on) panel.removeAttribute("hidden");
        else panel.setAttribute("hidden", "");
      });
      try {
        history.replaceState(null, "", "#" + id);
      } catch (e) {}
    }
    buttons.forEach((btn) => {
      btn.addEventListener("click", () => activate(btn.getAttribute("data-tab")));
    });
    const hash = (location.hash || "").replace(/^#/, "");
    if (hash && buttons.some((b) => b.getAttribute("data-tab") === hash)) {
      activate(hash);
    }
  });
})();
