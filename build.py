# Summer Opportunity Fair site generator. Edit the data below, run: python3 build.py -> ./site and ./preview
import os, shutil, html
from art import hero_scene, ICONS
e = html.escape
WHEN = "Late February 2027"
WHERE = "Northern Westchester"
VENUE = "Venue announced soon"
TABLE = ("Exhibitor table", 400, "A 6-foot table, two chairs, and a free listing in the printed fair directory.")
# Directory ad add-ons (draft prices - confirm). Printed directory: 5.5 x 8.5 in booklet.
ADS = [("QUARTER", "Quarter-page ad", 75, "2.375 x 3.875 in"),
       ("HALF", "Half-page ad", 125, "5 x 3.875 in"),
       ("FULL", "Full-page ad", 225, "5 x 8 in")]
SPONSORS = [("GOLD", "Gold sponsorship", 200, "Your banner at the fair plus placement on the website home page.", 6),
            ("PLATINUM", "Platinum sponsorship", 400, "Placement in every family email plus the website home page.", 3)]
DIRECTORY_PRICE = 20
PREORDER_PRICE = 15
AD_DEADLINE = "February 1, 2027"
TERMS = ["Your table is confirmed once payment clears. You'll get a receipt by email.",
         "Bank transfer (ACH) at checkout is preferred. It keeps table prices low.",
         "Gold and Platinum are upgrades for exhibitors and are first come, first served.",
         f"Listing details and ad artwork are due {AD_DEADLINE}. You'll get the upload form right after checkout.",
         "Full refund until 30 days before the fair. If the fair is snowed out, your table moves to the snow date or you get a full refund."]

def head(title, desc, full=True):
    meta = f'''<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Montserrat:wght@600;700;800;900&family=Geist:wght@400;500;600&display=swap">
<link rel="icon" href="favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="favicon-32.png">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<meta name="theme-color" content="#0b2348">
<link rel="stylesheet" href="style.css">'''
    if not full: return meta
    return f'<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n{meta}\n</head>\n<body>'

def tail(full=True):
    return '<script src="config.js"></script>\n<script src="site.js"></script>' + ("\n</body>\n</html>\n" if full else "\n")

def nav(active=""):
    links = "".join(f'<a href="{h}"{" aria-current=\"page\"" if active==k else ""}>{t}</a>' for k,h,t in [("home","index.html","The fair"),("ex","exhibit.html","Exhibit")])
    return f'''<header class="top"><div class="wrap top-in">
<a class="brand" href="index.html"><img class="brand-tiles" src="logo-tiles.png" alt="" width="82" height="20"><span>Summer Opportunity Fair</span></a>
<nav class="nav">{links}<a class="btn small" href="index.html#rsvp">RSVP free</a></nav>
</div><div class="bunting-strip" aria-hidden="true"></div></header>'''

def footer():
    return f'''<footer class="foot"><div class="wrap foot-in">
<div><a class="brand" href="index.html"><img class="brand-tiles" src="logo-tiles.png" alt="" width="82" height="20"><span>Summer Opportunity Fair</span></a>
<p>{WHEN} · {WHERE}. Free for families. Presented by Resource Commons.</p></div>
<div class="foot-links"><a href="index.html#rsvp">RSVP free</a><a href="exhibit.html">Exhibit or sponsor</a><a href="https://resourcecommons.com">Resource Commons</a></div>
</div></footer>'''

def home(full=True):
    body = f'''{nav("home")}
<main class="summer">
<section class="ev-hero"><div class="wrap"><div class="panel hero-split"><div class="hero-text">
<img class="hero-logo" src="logo.png" alt="Summer Opportunity Fair" width="829" height="506">
<p class="kicker">{WHEN} · {WHERE}</p>
<h1>Plan the <span class="tl">whole summer</span> in one afternoon.</h1>
<p class="lede">Day camps, sleepaway camps, classes and teen summer programs, all in one room. Meet the directors, ask your questions, and leave with a plan. Free for families.</p>
<p class="hero-note">{VENUE} · Free for families · RSVP requested</p>
<div class="cta"><a class="btn" href="#rsvp">RSVP free</a><a class="btn ghost" href="exhibit.html">Exhibit at the fair</a></div>
</div><div class="hero-art" id="hero-art">{hero_scene()}</div></div></div></section>
<section class="band"><div class="wrap">
<div class="sec-h"><p class="kicker">Every kind of summer</p><h2>Find the right fit</h2><p>Classic camps, sports, science and the arts, plus programs for every budget and schedule.</p></div>
<div class="cats">
<div class="cat orange"><img src="tile-camp.png" alt="" width="80" height="80"><h3>Camp & outdoors</h3><p>Day camps, sleepaway camps and outdoor adventure.</p></div>
<div class="cat blue"><img src="tile-sports.png" alt="" width="80" height="80"><h3>Swim & sports</h3><p>Swim lessons, sports camps and leagues.</p></div>
<div class="cat green"><img src="tile-nature.png" alt="" width="80" height="80"><h3>Nature & STEM</h3><p>Science, coding, gardening and nature programs.</p></div>
<div class="cat purple"><img src="tile-arts.png" alt="" width="80" height="80"><h3>Arts & theater</h3><p>Theater, music, dance and art studios.</p></div>
</div></div></section>
<section class="band"><div class="wrap two">
<div><h2>What to expect</h2><ul class="talks"><li>Camp directors and program leaders, face to face</li><li>Day, sleepaway, specialty and teen programs in one room</li><li>Time to ask about dates, costs, hours and transportation</li><li>Programs for a range of ages, interests and budgets</li></ul></div>
<div><h2>Take the whole fair home</h2><p class="small-note">The printed fair directory lists every exhibitor, with ages, location and how to sign up. Pre-order for ${PREORDER_PRICE} and pick it up at check-in, or buy it at the fair for ${DIRECTORY_PRICE}.</p><div class="cta"><a class="btn" data-link="pay-PREORDER" href="#">Pre-order for ${PREORDER_PRICE}</a></div></div>
</div></section>
<section class="band" id="rsvp"><div class="wrap">
<div class="signup-card">
<div class="sec-h"><h2>RSVP and get the exhibitor list first</h2><p>We'll email you the date, venue, exhibitor list and stage schedule before the fair. Nothing else.</p></div>
<form id="kit-form" class="kit" novalidate>
<fieldset><legend>My kids are</legend><div class="chks">
<label class="chk"><input type="checkbox" name="interest" value="Preschool to 2nd grade" id="i-little"><span>Preschool to 2nd grade</span></label>
<label class="chk"><input type="checkbox" name="interest" value="3rd to 8th grade" id="i-big"><span>3rd to 8th grade</span></label>
<label class="chk"><input type="checkbox" name="interest" value="High school" id="i-teen"><span>High school</span></label></div></fieldset>
<div class="row"><label class="fld"><span>First name</span><input id="f-name" name="first_name" autocomplete="given-name"></label>
<label class="fld"><span>Email</span><input id="f-email" name="email_address" type="email" autocomplete="email" required></label></div>
<div class="row end"><button class="btn" type="submit" id="f-submit">RSVP free</button><p class="small-note" id="f-msg" role="status">We never sell or share your email.</p></div>
</form></div>
</div></section>
<section class="band"><div class="wrap">
<div class="sec-h"><h2>Questions</h2></div>
<div class="faq">
<details><summary>Does it cost anything for families?</summary><p>No. The fair is always free for families.</p></details>
<details><summary>Can I bring my kids?</summary><p>Yes, kids are welcome.</p></details>
<details><summary>Is there a directory?</summary><p>Yes. The printed fair directory lists every exhibitor. Pre-order it online for ${PREORDER_PRICE} and pick it up at check-in, or buy it at the fair for ${DIRECTORY_PRICE}.</p></details>
<details><summary>Is the venue accessible?</summary><p>Yes. We choose venues with step-free access, accessible restrooms and nearby parking.</p></details>
<details><summary>What if it snows?</summary><p>There's a published snow date. Everyone who RSVPs gets an email if anything changes.</p></details>
</div></div></section>
</main>
{footer()}'''
    return head("Summer Opportunity Fair", "Westchester's summer camp and teen opportunity fair. Day camps, sleepaway camps, classes and teen programs in one room. Free for families.", full) + "\n" + body + "\n" + tail(full)

def exhibit():
    adopts = '<label class="pick"><input type="radio" name="ad" value="" data-price="0" id="ad-none" checked><span class="pick-b"><strong>No ad</strong><span>Free listing only</span></span><span class="pick-p">$0</span></label>' + "".join(
        f'<label class="pick"><input type="radio" name="ad" value="{k}" data-price="{p}" id="ad-{k.lower()}"><span class="pick-b"><strong>{e(n)}</strong><span>{e(sz)}</span></span><span class="pick-p">${p}</span></label>' for k,n,p,sz in ADS)
    spopts = '<label class="pick"><input type="radio" name="sp" value="" data-price="0" id="sp-none" checked><span class="pick-b"><strong>No sponsorship</strong><span>&nbsp;</span></span><span class="pick-p">$0</span></label>' + "".join(
        f'<label class="pick"><input type="radio" name="sp" value="{k}" data-price="{p}" id="sp-{k.lower()}"><span class="pick-b"><strong>{e(n)}</strong><span>{e(d)} {c} spots.</span></span><span class="pick-p">${p}</span></label>' for k,n,p,d,c in SPONSORS)
    terms = "".join(f"<li>{e(t)}</li>" for t in TERMS)
    specs = "".join(f"<tr><td>{e(n)}</td><td>{e(sz)}</td><td class='num'>${p}</td></tr>" for k,n,p,sz in ADS)
    body = f"""{nav("ex")}
<main class="summer">
<section class="ev-hero"><div class="wrap"><div class="panel slim">
<p class="kicker">Exhibitors and sponsors · {WHEN}</p>
<h1>Meet the families planning their summer.</h1>
<p class="lede">Camps, classes and teen programs get a table in front of Westchester families at the moment they're choosing. Every exhibitor gets a free listing in the printed fair directory.</p>
</div></div></section>
<section class="band"><div class="wrap">
<div class="sec-h"><p class="kicker">Reserve your table</p><h2>Build your order</h2><p>Pick your add-ons, then continue to secure checkout.</p></div>
<div class="order">
<form class="steps" id="order" novalidate>
<fieldset class="step"><legend><span class="n">1</span>Exhibitor table</legend>
<label class="pick on"><input type="checkbox" checked disabled id="tbl"><span class="pick-b"><strong>{e(TABLE[0])}</strong><span>{e(TABLE[2])}</span></span><span class="pick-p">${TABLE[1]}</span></label></fieldset>
<fieldset class="step"><legend><span class="n">2</span>Featured ad in the printed directory <em>optional</em></legend>{adopts}</fieldset>
<fieldset class="step"><legend><span class="n">3</span>Sponsorship <em>optional</em></legend>{spopts}</fieldset>
</form>
<aside class="summary" aria-live="polite">
<h3>Your order</h3>
<ul id="sum-lines"></ul>
<div class="sum-total"><span>Total</span><strong id="sum-total">${TABLE[1]}</strong></div>
<a class="btn" id="checkout" data-link="pay-CHECKOUT" href="#">Continue to checkout</a>
<p class="small-note">You'll confirm these add-ons on the secure Stripe checkout page. Card or bank transfer.</p>
</aside>
</div>
<div class="ach"><span class="ic" aria-hidden="true">ACH</span><div><h3>Pay by bank if you can</h3><p>Bank transfer keeps fees, and table prices, low.</p></div></div>
</div></section>
<section class="band"><div class="wrap two">
<div><h2>Directory ad sizes</h2><div class="tbl"><table><thead><tr><th>Ad</th><th>Size</th><th class="num">Price</th></tr></thead><tbody>{specs}</tbody></table></div>
<p class="small-note">The directory is a 5.5 x 8.5 in booklet. Send a print-ready PDF or high-resolution image by {AD_DEADLINE}. Need help with a design? Ask us.</p></div>
<div><h2>Payment terms</h2><ul class="talks">{terms}</ul></div>
</div></section>
<section class="band"><div class="wrap two">
<div><h2>Local business?</h2><p class="small-note">Pediatric practices, banks, realtors and other local businesses can sponsor the whole fair. Ask about presenting sponsorship.</p><a class="btn ghost" data-link="contact" href="#">Ask about sponsorship</a></div>
<div><h2>Need an invoice?</h2><p class="small-note">Schools, districts and nonprofits can pay by check or ACH invoice.</p><a class="btn ghost" data-link="contact" href="#">Request an invoice</a></div>
</div></section>
</main>
{footer()}"""
    return head("Exhibit · Summer Opportunity Fair", "Reserve an exhibitor table, directory ad or sponsorship for the Summer Opportunity Fair in Westchester.") + "\n" + body + "\n" + tail()

CONFIG = """// Summer Opportunity Fair settings. Paste links here; blank ones show "opening soon".
window.SOF = {
  heroPhoto: "",            // optional: a real photo (e.g. "images/hero.jpg") replaces the illustration
  kitFormId: "",            // Kit form number, from app.kit.com/forms/1234567
  contact: "",              // sponsorship / invoice request form (Tally or Google Forms)
  // One Stripe Payment Link for the table. In Stripe, add the ad sizes and sponsorships
  // to that link as optional items so camps can tick them at checkout.
  // Name products "SOF27 Exhibitor table", "SOF27 Quarter-page ad", etc. for the reconciliation workbook.
  pay: { CHECKOUT: "", PREORDER: "" },  // PREORDER = Stripe link for the $15 directory pre-order ("SOF27 Directory pre-order")
  // After checkout, Stripe should send camps here to submit listing details and ad artwork:
  listingForm: "",
};
"""
SITEJS = r"""(function () {
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
"""
if __name__ == "__main__":
    for d in ("site", "preview"):
        shutil.rmtree(d, ignore_errors=True); os.makedirs(d)
    pages = {"exhibit.html": exhibit()}
    for n, t in pages.items():
        for d in ("site", "preview"): open(f"{d}/{n}", "w").write(t)
    open("site/index.html", "w").write(home()); open("preview/index.html", "w").write(home(False))
    for d in ("site", "preview"):
        shutil.copy("style.css", f"{d}/style.css"); open(f"{d}/config.js", "w").write(CONFIG); open(f"{d}/site.js", "w").write(SITEJS)
    for d in ("site", "preview"):
        for f in ("logo.png","logo-tiles.png","tile-camp.png","tile-sports.png","tile-nature.png","tile-arts.png","favicon.ico","favicon-32.png","apple-touch-icon.png","icon-512.png"):
            shutil.copy(f"brand/{f}", f"{d}/{f}")
    open("site/CNAME", "w").write("summeropportunityfair.com\n")
    print("built")
