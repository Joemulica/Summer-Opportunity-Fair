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
  var order = document.getElementById("order");
  if (order) {
    var lines = document.getElementById("sum-lines"), tot = document.getElementById("sum-total"), go = document.getElementById("checkout");
    var base = pay.CHECKOUT || "";
    function calc() {
      var items = [["Exhibitor table", 400]], ref = ["TABLE"];
      order.querySelectorAll("input[type=radio]:checked").forEach(function (r) {
        var p = +r.getAttribute("data-price");
        r.closest(".step").querySelectorAll(".pick").forEach(function (l) { l.classList.toggle("on", l.contains(r)); });
        if (p) { items.push([r.closest(".pick").querySelector("strong").textContent, p]); ref.push(r.value); }
      });
      lines.innerHTML = "";
      var sum = 0;
      items.forEach(function (it) { sum += it[1]; var li = document.createElement("li"); var a = document.createElement("span"); a.textContent = it[0]; var b = document.createElement("span"); b.textContent = "$" + it[1]; li.appendChild(a); li.appendChild(b); lines.appendChild(li); });
      tot.textContent = "$" + sum.toLocaleString("en-US");
      if (base) go.href = base + (base.indexOf("?") > -1 ? "&" : "?") + "client_reference_id=" + encodeURIComponent(ref.join("-"));
    }
    order.addEventListener("change", calc); calc();
  }
})();
