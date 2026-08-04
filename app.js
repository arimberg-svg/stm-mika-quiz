const LETTERS = ["а", "б", "в", "г"];

let questions = [];
let answers = [];
let current = 0;

const el = {
  start: document.getElementById("screen-start"),
  quiz: document.getElementById("screen-quiz"),
  result: document.getElementById("screen-result"),
  name: document.getElementById("user-name"),
  startBtn: document.getElementById("btn-start"),
  prev: document.getElementById("btn-prev"),
  next: document.getElementById("btn-next"),
  restart: document.getElementById("btn-restart"),
  counter: document.getElementById("q-counter"),
  topic: document.getElementById("q-topic"),
  text: document.getElementById("q-text"),
  options: document.getElementById("options"),
  bar: document.getElementById("progress-bar"),
  scoreNum: document.getElementById("score-num"),
  scoreTitle: document.getElementById("score-title"),
  verdict: document.getElementById("score-verdict"),
  topicStats: document.getElementById("topic-stats"),
  review: document.getElementById("review"),
};

function show(screen) {
  el.start.classList.toggle("hidden", screen !== "start");
  el.quiz.classList.toggle("hidden", screen !== "quiz");
  el.result.classList.toggle("hidden", screen !== "result");
}

function letterOf(optionText) {
  const m = String(optionText).trim().match(/^([абвг])\)/i);
  return m ? m[1].toLowerCase() : null;
}

function renderQuestion() {
  const q = questions[current];
  el.counter.textContent = `${current + 1} / ${questions.length}`;
  el.topic.textContent = q.topic;
  el.text.textContent = q.q;
  el.bar.style.width = `${((current + 1) / questions.length) * 100}%`;

  el.options.innerHTML = "";
  q.options.forEach((opt, idx) => {
    const btn = document.createElement("button");
    btn.type = "button";
    btn.className = "option";
    btn.textContent = opt;
    const key = letterOf(opt) || LETTERS[idx];
    if (answers[current] === key) btn.classList.add("selected");
    btn.addEventListener("click", () => {
      answers[current] = key;
      [...el.options.children].forEach((c) => c.classList.remove("selected"));
      btn.classList.add("selected");
      el.next.disabled = false;
    });
    el.options.appendChild(btn);
  });

  el.prev.disabled = current === 0;
  el.next.disabled = !answers[current];
  el.next.textContent = current === questions.length - 1 ? "Завершить" : "Далее";
}

function grade() {
  let correct = 0;
  const byTopic = {};

  questions.forEach((q, i) => {
    const ok = answers[i] === q.answer;
    if (ok) correct += 1;
    if (!byTopic[q.topic]) byTopic[q.topic] = { ok: 0, total: 0 };
    byTopic[q.topic].total += 1;
    if (ok) byTopic[q.topic].ok += 1;
  });

  const name = el.name.value.trim();
  el.scoreNum.textContent = String(correct);
  el.scoreTitle.textContent = name ? `${name}, ваш результат` : "Ваш результат";

  let verdict;
  if (correct >= 24) verdict = "Отлично — материал усвоен уверенно.";
  else if (correct >= 18) verdict = "Хорошо — есть пробелы, стоит повторить слабые темы.";
  else verdict = "Нужно повторить материал по слабым блокам.";
  el.verdict.textContent = verdict;

  el.topicStats.innerHTML = Object.entries(byTopic)
    .map(
      ([topic, s]) =>
        `<div class="topic-row"><span>${topic}</span><strong>${s.ok}/${s.total}</strong></div>`
    )
    .join("");

  el.review.innerHTML = questions
    .map((q, i) => {
      const ok = answers[i] === q.answer;
      const yours = answers[i] ? `${answers[i]})` : "—";
      return `
        <div class="review-item ${ok ? "ok" : "bad"}">
          <div class="mark">${ok ? "Верно" : "Ошибка"} · вопрос ${i + 1}</div>
          <div>${q.q}</div>
          <div class="muted">Ваш ответ: ${yours} · Правильно: ${q.answer})</div>
        </div>`;
    })
    .join("");

  show("result");
  window.scrollTo({ top: 0, behavior: "smooth" });
}

el.startBtn.addEventListener("click", () => {
  answers = Array(questions.length).fill(null);
  current = 0;
  show("quiz");
  renderQuestion();
});

el.prev.addEventListener("click", () => {
  if (current > 0) {
    current -= 1;
    renderQuestion();
  }
});

el.next.addEventListener("click", () => {
  if (!answers[current]) return;
  if (current === questions.length - 1) grade();
  else {
    current += 1;
    renderQuestion();
  }
});

el.restart.addEventListener("click", () => {
  answers = Array(questions.length).fill(null);
  current = 0;
  show("start");
});

fetch("./questions.json")
  .then((r) => {
    if (!r.ok) throw new Error("Не удалось загрузить вопросы");
    return r.json();
  })
  .then((data) => {
    questions = data;
    el.startBtn.disabled = false;
  })
  .catch((err) => {
    el.startBtn.disabled = true;
    el.startBtn.textContent = "Ошибка загрузки";
    console.error(err);
  });
