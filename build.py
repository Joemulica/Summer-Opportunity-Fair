# Summer Opportunity Fair site generator. Edit the data below, run: python3 build.py -> ./site and ./preview
import os, shutil, html
from art import hero_scene, ICONS
e = html.escape
WHEN = "Late February 2027"
WHERE = "Northern Westchester"
VENUE = "Venue announced soon"
PRICES = [
  ("TABLE", "Exhibitor table", "$400", "A 6-foot table, two chairs and a spot in the event guide.", None),
  ("DIRECTORY", "Online directory listing", "+$50", "Your program in the Summer Opportunity Fair online directory through summer 2027.", None),
  ("GOLD", "Gold sponsorship", "$200", "Your banner at the fair plus placement on the website home page.", "6 spots"),
  ("PLATINUM", "Platinum sponsorship", "$400", "Placement in every family email plus the website home page.", "3 spots"),
]
ZONES = [("Little Kids", "Day camps and half-day programs for preschool and early elementary."),
         ("Big Kids", "Sleepaway, specialty, sports, arts and STEM camps."),
         ("Teen Zone", "Counselor-in-training spots, summer jobs, pre-college and volunteering.")]
TERMS = ["Your table is confirmed once payment clears. You'll get a receipt by email.",
         "Bank transfer (ACH) at checkout is preferred. It keeps table prices low.",
         "Gold and Platinum are upgrades for exhibitors and are first come, first served.",
         "Full refund until 30 days before the fair. If the fair is snowed out, your table moves to the snow date or you get a full refund."]

def head(title, desc, full=True):
    meta = f'''<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700;12..96,800&family=Geist:wght@400;500;600&display=swap">
<link rel="stylesheet" href="style.css">'''
    if not full: return meta
    return f'<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n{meta}\n</head>\n<body>'

def tail(full=True):
    return '<script src="config.js"></script>\n<script src="site.js"></script>' + ("\n</body>\n</html>\n" if full else "\n")

def nav(active=""):
    links = "".join(f'<a href="{h}"{" aria-current=\"page\"" if active==k else ""}>{t}</a>' for k,h,t in [("home","index.html","The fair"),("dir","directory.html","Directory"),("ex","exhibit.html","Exhibit")])
    return f'''<header class="top"><div class="wrap top-in">
<a class="brand" href="index.html"><span class="mark sun" aria-hidden="true"></span>Summer Opportunity Fair</a>
<nav class="nav">{links}<a class="btn small" href="index.html#rsvp">RSVP free</a></nav>
</div><div class="bunting-strip" aria-hidden="true"></div></header>'''

def footer():
    return f'''<footer class="foot"><div class="wrap foot-in">
<div><a class="brand" href="index.html"><span class="mark sun" aria-hidden="true"></span>Summer Opportunity Fair</a>
<p>{WHEN} · {WHERE}. Free for families. Presented by Resource Commons.</p></div>
<div class="foot-links"><a href="index.html#rsvp">RSVP free</a><a href="directory.html">Online directory</a><a href="exhibit.html">Exhibit or sponsor</a><a href="https://resourcecommons.com">Resource Commons</a></div>
</div></footer>'''

def home(full=True):
    zones = "".join(f'<div class="zone">{ICONS[a]}<h3>{e(a)}</h3><p>{e(b)}</p></div>' for a,b in ZONES)
    body = f'''{nav("home")}
<main class="summer">
<section class="ev-hero"><div class="wrap"><div class="panel hero-split"><div class="hero-text">
<p class="eyebrow"><span class="live" aria-hidden="true"></span>{WHEN} · {WHERE}</p>
<h1>Plan the whole summer in one afternoon.</h1>
<p class="lede">Day camps, sleepaway camps, classes and teen summer programs, all in one room. Meet the directors, ask your questions, and leave with a plan. Free for families.</p>
<p class="hero-note">{VENUE} · Free for families · RSVP requested</p>
<div class="cta"><a class="btn" href="#rsvp">RSVP free</a><a class="btn ghost" href="exhibit.html">Exhibit at the fair</a></div>
</div><div class="hero-art" id="hero-art">{hero_scene()}</div></div></div></section>
<section class="band"><div class="wrap">
<div class="sec-h"><h2>Three zones, every age</h2><p>Walk straight to the programs that fit your kids.</p></div>
<div class="three cards">{zones}</div>
</div></section>
<section class="band"><div class="wrap two">
<div><h2>What to expect</h2><ul class="talks"><li>Camp directors and program leaders, face to face</li><li>Ten-minute camp demos on the stage</li><li>A play area and activities for the kids</li><li>Early sign-up deals from exhibitors</li></ul></div>
<div><h2>Can't wait for February?</h2><p class="small-note">The online directory lists every exhibiting program, with ages, location and how to sign up.</p><a class="btn ghost" href="directory.html">Browse the directory</a></div>
</div></section>
<section class="band" id="rsvp"><div class="wrap">
<div class="signup-card">
<div class="sec-h"><h2>RSVP and get the exhibitor list first</h2><p>We'll email you the date, venue, exhibitor list and stage schedule before the fair. Nothing else.</p></div>
<form id="kit-form" class="kit" novalidate>
<fieldset><legend>My kids are</legend><div class="chks">
<label class="chk"><input type="checkbox" name="interest" value="Little Kids" id="i-little"><span>Preschool to 2nd grade</span></label>
<label class="chk"><input type="checkbox" name="interest" value="Big Kids" id="i-big"><span>3rd to 8th grade</span></label>
<label class="chk"><input type="checkbox" name="interest" value="Teens" id="i-teen"><span>High school</span></label></div></fieldset>
<div class="row"><label class="fld"><span>First name</span><input id="f-name" name="first_name" autocomplete="given-name"></label>
<label class="fld"><span>Email</span><input id="f-email" name="email_address" type="email" autocomplete="email" required></label></div>
<div class="row end"><button class="btn" type="submit" id="f-submit">RSVP free</button><p class="small-note" id="f-msg" role="status">We never sell or share your email.</p></div>
</form></div>
</div></section>
<section class="band"><div class="wrap">
<div class="sec-h"><h2>Questions</h2></div>
<div class="faq">
<details><summary>Does it cost anything for families?</summary><p>No. The fair is always free for families.</p></details>
<details><summary>Can I bring my kids?</summary><p>Yes. There's a play area and activities so parents can talk with camp directors.</p></details>
<details><summary>Is the venue accessible?</summary><p>Yes. We choose venues with step-free access, accessible restrooms and nearby parking.</p></details>
<details><summary>What if it snows?</summary><p>There's a published snow date. Everyone who RSVPs gets an email if anything changes.</p></details>
</div></div></section>
</main>
{footer()}'''
    return head("Summer Opportunity Fair", "Westchester's summer camp and teen opportunity fair. Day camps, sleepaway camps, classes and teen programs in one room. Free for families.", full) + "\n" + body + "\n" + tail(full)

def exhibit():
    opts = "".join(f'''<div class="opt"><div class="opt-h"><h3>{e(n)}</h3><span class="opt-p">{e(p)}</span></div>
<p>{e(d)}</p>{f'<span class="pill cap">{e(cap)}</span>' if cap else ''}<a class="btn" data-link="pay-{k}" href="#">{"Reserve a table" if k=="TABLE" else "Add " + e(n.split(" ")[0].lower()) if k!="DIRECTORY" else "Add a listing"}</a></div>''' for k,n,p,d,cap in PRICES)
    terms = "".join(f"<li>{e(t)}</li>" for t in TERMS)
    body = f'''{nav("ex")}
<main class="summer">
<section class="ev-hero"><div class="wrap"><div class="panel slim">
<p class="eyebrow">Exhibitors and sponsors · {WHEN}</p>
<h1>Meet the families planning their summer.</h1>
<p class="lede">Camps, classes and teen programs get a table in front of Westchester families at the moment they're choosing.</p>
</div></div></section>
<section class="band"><div class="wrap">
<div class="sec-h"><h2>Pricing</h2><p>Start with a table, then add what you need.</p></div>
<div class="opts">{opts}</div>
<div class="ach"><span class="ic" aria-hidden="true">ACH</span><div><h3>Pay by bank if you can</h3><p>Checkout offers card or bank transfer. Bank transfer keeps fees, and table prices, low.</p></div></div>
</div></section>
<section class="band"><div class="wrap two">
<div><h2>Payment terms</h2><ul class="talks">{terms}</ul></div>
<div><h2>Local business?</h2><p class="small-note">Pediatric practices, banks, realtors and other local businesses can sponsor the whole fair. Ask about presenting sponsorship.</p><a class="btn ghost" data-link="contact" href="#">Ask about sponsorship</a>
<h2>Need an invoice?</h2><p class="small-note">Schools, districts and nonprofits can pay by check or ACH invoice.</p><a class="btn ghost" data-link="contact" href="#">Request an invoice</a></div>
</div></section>
</main>
{footer()}'''
    return head("Exhibit · Summer Opportunity Fair", "Exhibitor tables, directory listings and sponsorships for the Summer Opportunity Fair in Westchester.") + "\n" + body + "\n" + tail()

def directory():
    body = f'''{nav("dir")}
<main class="summer">
<section class="hero"><div class="wrap">
<p class="eyebrow">Online directory · Summer 2027</p>
<h1>Every program at the fair, <span class="hl">in one list.</span></h1>
<p class="lede">Filter by age and type of program. Listings go up as exhibitors sign on.</p>
</div></section>
<section class="band"><div class="wrap">
<div class="dir-tools"><label class="fld"><span>Search</span><input id="d-q" placeholder="Camp name, town or activity"></label>
<label class="fld"><span>Ages</span><select id="d-age"><option value="">All ages</option><option>Little Kids</option><option>Big Kids</option><option>Teens</option></select></label></div>
<div id="dir-list" class="dir-list"></div>
<div id="dir-empty" class="split"><div><h2>Listings open soon</h2><p>Camps and programs can add a listing for $50 when they reserve a table. RSVP and we'll email you when the directory goes live.</p></div><div class="cta"><a class="btn" href="index.html#rsvp">RSVP free</a><a class="btn ghost" href="exhibit.html">List your program</a></div></div>
</div></section>
</main>
{footer()}'''
    return head("Directory · Summer Opportunity Fair", "Online directory of camps, classes and teen programs exhibiting at the Summer Opportunity Fair.") + "\n" + body + "\n" + tail()

CONFIG = """// Summer Opportunity Fair settings. Paste links here; blank ones show "opening soon".
window.SOF = {
  heroPhoto: "",            // optional: a real photo (e.g. "images/hero.jpg") replaces the illustration
  kitFormId: "",            // Kit form number, from app.kit.com/forms/1234567
  contact: "",              // sponsorship / invoice request form (Tally or Google Forms)
  pay: {                    // Stripe Payment Links. Name products "SOF27 ..." for the reconciliation workbook.
    TABLE: "", DIRECTORY: "", GOLD: "", PLATINUM: ""
  },
  // Directory listings. Add one line per paid listing, e.g.
  // { name: "Camp Example", ages: ["Big Kids"], town: "Ossining", type: "Day camp", url: "https://..." },
  directory: []
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
"""
if __name__ == "__main__":
    for d in ("site", "preview"):
        shutil.rmtree(d, ignore_errors=True); os.makedirs(d)
    pages = {"exhibit.html": exhibit(), "directory.html": directory()}
    for n, t in pages.items():
        for d in ("site", "preview"): open(f"{d}/{n}", "w").write(t)
    open("site/index.html", "w").write(home()); open("preview/index.html", "w").write(home(False))
    for d in ("site", "preview"):
        shutil.copy("style.css", f"{d}/style.css"); open(f"{d}/config.js", "w").write(CONFIG); open(f"{d}/site.js", "w").write(SITEJS)
    open("site/CNAME", "w").write("summeropportunityfair.com\n")
    print("built")
