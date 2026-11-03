(function () {
  var C = window.SOF || {}, pay = C.pay || {};
  document.querySelectorAll("[data-link]").forEach(function (a) {
    var k = a.getAttribute("data-link"), url = k.indexOf("pay-") === 0 ? pay[k.slice(4)] : C[k];
    if (url) { a.href = url; a.rel = "noopener"; }
    else { a.removeAttribute("href"); a.setAttribute("aria-disabled", "true"); a.classList.add("soon"); a.textContent += " · opening soon"; }
  });
  var art = document.getElementById("hero-art");
  if (art && C.heroPhoto) { art.innerHTML = ""; var im = new Image(); im.src = C.heroPhoto; im.alt = "Kids at summer camp"; im.className = "hero-photo"; art.appendChild(im); }
  var form = document.getElementById("kit-form");
  if (form) {
    var msg = document.getElementById("f-msg"), btn = document.getElementById("f-submit");
    if (!C.kitFormId) { btn.disabled = true; btn.classList.add("soon"); btn.textContent = "RSVP opening soon"; }
    form.addEventListener("submit", function (ev) {
      ev.preventDefault(); if (!C.kitFormId) return;
      var email = document.getElementById("f-email");
      if (!email.value || !email.checkValidity()) { msg.textContent = "Enter a valid email address."; email.focus(); return; }
      var picks = Array.prototype.map.call(form.querySelectorAll("input[name=interest]:checked"), function (c) { return c.value; });
      var body = new URLSearchParams();
      body.append("email_address", email.value);
      body.append("fields[first_name]", document.getElementById("f-name").value);
      body.append("fields[interests]", picks.join(", "));
      btn.disabled = true; msg.textContent = "Saving your RSVP...";
      fetch("https://app.kit.com/forms/" + C.kitFormId + "/subscriptions", { method: "POST", body: body, headers: { Accept: "application/json" } })
        .then(function (r) { if (!r.ok) throw new Error(); form.reset(); msg.textContent = "You're on the list. Check your inbox to confirm."; })
        .catch(function () { msg.textContent = "That didn't go through. Please try again in a minute."; })
        .then(function () { btn.disabled = false; });
    });
  }
  var list = document.getElementById("dir-list");
  if (list) {
    var items = C.directory || [], q = document.getElementById("d-q"), age = document.getElementById("d-age");
    document.getElementById("dir-empty").hidden = items.length > 0;
    document.querySelector(".dir-tools").hidden = items.length === 0;
    function draw() {
      var t = (q.value || "").toLowerCase(), a = age.value;
      list.innerHTML = "";
      items.filter(function (x) {
        var hay = [x.name, x.town, x.type].join(" ").toLowerCase();
        return (!t || hay.indexOf(t) > -1) && (!a || (x.ages || []).indexOf(a) > -1);
      }).forEach(function (x) {
        var d = document.createElement("a"); d.className = "dir-item"; if (x.url) { d.href = x.url; d.rel = "noopener"; }
        var h = document.createElement("strong"); h.textContent = x.name; d.appendChild(h);
        var p = document.createElement("span"); p.textContent = [x.type, x.town, (x.ages || []).join(", ")].filter(Boolean).join(" · "); d.appendChild(p);
        list.appendChild(d);
      });
    }
    q.addEventListener("input", draw); age.addEventListener("change", draw); draw();
  }
})();
