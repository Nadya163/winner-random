/* ==========================================================================
   Winner Random — логика выбора победителя
   Всё работает в браузере, никаких запросов на сервер.
   ========================================================================== */
(function () {
  "use strict";

  var SPIN_DURATION = 1800; // мс анимации перебора
  var SPIN_INTERVAL = 80;   // мс между сменой имён при анимации
  var COLORS = ["#c84bff", "#ff4b8b", "#4bffb5", "#ffb84b", "#4b8bff"];

  /* ---- Вспомогательные ---- */

  function getParticipants() {
    var raw = (document.getElementById("participants") || {}).value || "";
    return raw.split("\n")
      .map(function (s) { return s.trim(); })
      .filter(function (s) { return s.length > 0; });
  }

  function shuffle(arr) {
    var a = arr.slice();
    for (var i = a.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1));
      var t = a[i]; a[i] = a[j]; a[j] = t;
    }
    return a;
  }

  function updateCounter() {
    var list = getParticipants();
    var el = document.getElementById("participantCount");
    if (el) el.textContent = list.length;
  }

  /* ---- Конфетти ---- */

  function launchConfetti(container) {
    for (var i = 0; i < 24; i++) {
      (function (i) {
        setTimeout(function () {
          var piece = document.createElement("div");
          piece.className = "confetti-piece";
          piece.style.left = Math.random() * 100 + "%";
          piece.style.top = "0";
          piece.style.background = COLORS[Math.floor(Math.random() * COLORS.length)];
          piece.style.animationDelay = Math.random() * 0.4 + "s";
          piece.style.animationDuration = (0.8 + Math.random() * 0.6) + "s";
          container.appendChild(piece);
          setTimeout(function () { piece.remove(); }, 1600);
        }, i * 30);
      })(i);
    }
  }

  /* ---- Анимация прокрутки ---- */

  function spinAndReveal(winners, allParticipants, onDone) {
    var nameEl = document.getElementById("winnerName");
    if (!nameEl) return;

    nameEl.classList.add("spinning");
    var start = Date.now();
    var interval = setInterval(function () {
      var random = allParticipants[Math.floor(Math.random() * allParticipants.length)];
      nameEl.textContent = random;

      if (Date.now() - start >= SPIN_DURATION) {
        clearInterval(interval);
        nameEl.classList.remove("spinning");
        nameEl.textContent = winners[0];
        onDone();
      }
    }, SPIN_INTERVAL);
  }

  /* ---- Основная логика ---- */

  function draw() {
    var list = getParticipants();
    if (list.length === 0) {
      alert("Добавьте участников — по одному на каждой строке.");
      return;
    }

    var countInput = document.getElementById("winnerCount");
    var removeChecked = document.getElementById("removeWinner");
    var count = Math.min(
      parseInt((countInput || {}).value) || 1,
      list.length
    );

    var btn = document.getElementById("btnDraw");
    if (btn) btn.disabled = true;

    var shuffled = shuffle(list);
    var winners = shuffled.slice(0, count);

    var resultWrap = document.getElementById("resultWrap");
    var multiWrap  = document.getElementById("multipleWinners");
    var singleWrap = document.getElementById("singleWinner");

    if (resultWrap) resultWrap.classList.add("visible");

    if (count === 1) {
      if (singleWrap) singleWrap.style.display = "block";
      if (multiWrap)  multiWrap.style.display  = "none";

      spinAndReveal(winners, list, function () {
        var display = document.getElementById("winnerDisplay");
        if (display) launchConfetti(display);
        if (btn) btn.disabled = false;

        if (removeChecked && removeChecked.checked) {
          var textarea = document.getElementById("participants");
          if (textarea) {
            textarea.value = list
              .filter(function (p) { return p !== winners[0]; })
              .join("\n");
            updateCounter();
          }
        }
      });
    } else {
      if (singleWrap) singleWrap.style.display = "none";
      if (multiWrap)  multiWrap.style.display  = "block";

      var nameEl = document.getElementById("winnerName");
      if (nameEl) { nameEl.textContent = ""; nameEl.classList.remove("spinning"); }

      multiWrap.innerHTML = "";
      winners.forEach(function (w, i) {
        var div = document.createElement("div");
        div.className = "w-item";
        div.innerHTML = '<span class="place">' + (i + 1) + '.</span> ' + escapeHtml(w);
        multiWrap.appendChild(div);
      });

      var display = document.getElementById("winnerDisplay");
      if (display) launchConfetti(display);
      if (btn) btn.disabled = false;

      if (removeChecked && removeChecked.checked) {
        var textarea = document.getElementById("participants");
        if (textarea) {
          var remaining = list.filter(function (p) { return winners.indexOf(p) === -1; });
          textarea.value = remaining.join("\n");
          updateCounter();
        }
      }
    }
  }

  function escapeHtml(s) {
    return s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
  }

  function reset() {
    var resultWrap = document.getElementById("resultWrap");
    if (resultWrap) resultWrap.classList.remove("visible");
    var nameEl = document.getElementById("winnerName");
    if (nameEl) nameEl.textContent = "";
  }

  /* ---- Init ---- */

  document.addEventListener("DOMContentLoaded", function () {
    var textarea = document.getElementById("participants");
    if (textarea) textarea.addEventListener("input", updateCounter);

    var btn = document.getElementById("btnDraw");
    if (btn) btn.addEventListener("click", draw);

    var btnAgain = document.getElementById("btnAgain");
    if (btnAgain) btnAgain.addEventListener("click", reset);

    var countInput = document.getElementById("winnerCount");
    if (countInput) {
      countInput.addEventListener("change", function () {
        var v = parseInt(this.value) || 1;
        if (v < 1) this.value = 1;
        if (v > 100) this.value = 100;
      });
    }

    updateCounter();
  });

})();
