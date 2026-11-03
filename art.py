# Original camp-scene illustrations (inline SVG), used by build.py
def kid(x, y, skin, shirt, shorts, hair, pose="wave"):
    arms = {"wave": f'<path d="M{x-14} {y+18} l-14 -22 M{x+14} {y+18} l14 -22" stroke="{skin}" stroke-width="6" stroke-linecap="round"/>',
            "jump": f'<path d="M{x-14} {y+16} l-16 -26 M{x+14} {y+16} l16 -26" stroke="{skin}" stroke-width="6" stroke-linecap="round"/>',
            "ball": f'<path d="M{x-14} {y+20} l-12 14 M{x+14} {y+20} l16 6" stroke="{skin}" stroke-width="6" stroke-linecap="round"/>'}[pose]
    return f'''<g class="kid{' jumper' if pose=='jump' else ''}">
{arms}
<rect x="{x-15}" y="{y+8}" width="30" height="30" rx="10" fill="{shirt}"/>
<rect x="{x-14}" y="{y+34}" width="28" height="14" rx="5" fill="{shorts}"/>
<path d="M{x-8} {y+46} v18 M{x+8} {y+46} v18" stroke="{skin}" stroke-width="6" stroke-linecap="round"/>
<circle cx="{x}" cy="{y-6}" r="14" fill="{skin}"/>
<path d="M{x-14} {y-8} q2 -16 14 -16 q12 0 14 16 q-6 -7 -14 -6 q-8 -1 -14 6z" fill="{hair}"/>
<circle cx="{x-5}" cy="{y-6}" r="1.8" fill="#2a1a10"/><circle cx="{x+5}" cy="{y-6}" r="1.8" fill="#2a1a10"/>
<path d="M{x-5} {y} q5 5 10 0" stroke="#2a1a10" stroke-width="2" fill="none" stroke-linecap="round"/>
</g>'''

def hero_scene():
    pennants = "".join(f'<path d="M{20+i*44} 18 l22 0 l-11 22z" fill="{c}"/>' for i,c in enumerate(["#ff6a3d","#3e7bfa","#22b573","#8a5cf5","#ffb31f"]*3) if 20+i*44 < 600)
    return f'''<svg class="scene" viewBox="0 0 600 440" role="img" aria-label="Illustration of kids playing at a summer camp by a lake, with tents, a canoe and a campfire">
<defs>
<clipPath id="sc"><rect width="600" height="440" rx="28"/></clipPath>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#8fd3ff"/><stop offset="1" stop-color="#d9f1ff"/></linearGradient>
<linearGradient id="lake" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3aa0e8"/><stop offset="1" stop-color="#1f74c4"/></linearGradient>
</defs>
<g clip-path="url(#sc)">
<rect width="600" height="440" fill="url(#sky)"/>
<g class="sun"><circle cx="488" cy="92" r="40" fill="#ffd34d"/>
<g stroke="#ffd34d" stroke-width="7" stroke-linecap="round">{"".join(f'<path d="M488 92 m0 -56 v-14" transform="rotate({a} 488 92)"/>' for a in range(0,360,45))}</g></g>
<g class="cloud"><ellipse cx="130" cy="88" rx="46" ry="18" fill="#fff"/><ellipse cx="160" cy="76" rx="30" ry="20" fill="#fff"/><ellipse cx="104" cy="80" rx="22" ry="14" fill="#fff"/></g>
<g class="cloud c2"><ellipse cx="330" cy="58" rx="34" ry="13" fill="#fff"/><ellipse cx="352" cy="50" rx="22" ry="14" fill="#fff"/></g>
<path d="M0 228 Q120 150 250 214 T520 196 T600 206 V440 H0z" fill="#86cf8f"/>
<path d="M0 258 Q150 206 300 250 T600 236 V440 H0z" fill="#5db56f"/>
<g fill="#2f7d4f">
<path d="M34 252 l26 -74 l26 74z"/><path d="M70 256 l22 -60 l22 60z"/><path d="M528 236 l26 -80 l26 80z"/><path d="M500 244 l20 -56 l20 56z"/></g>
<g fill="#6b4226"><rect x="57" y="250" width="6" height="12"/><rect x="551" y="234" width="6" height="12"/></g>
<path d="M0 372 Q300 352 600 368 V440 H0z" fill="url(#lake)"/>
<g stroke="#bfe6ff" stroke-width="3" stroke-linecap="round" fill="none" opacity=".8"><path d="M60 400 q12 -6 24 0 q12 6 24 0"/><path d="M200 420 q12 -6 24 0 q12 6 24 0"/><path d="M540 410 q12 -6 24 0"/></g>
<g class="canoe"><g transform="translate(-30 50)">
<path d="M380 338 q60 26 130 0 q-10 18 -65 18 q-55 0 -65 -18z" fill="#e2683c"/>
<circle cx="425" cy="322" r="9" fill="#e0ac69"/><rect x="417" y="330" width="16" height="12" rx="4" fill="#ffb31f"/>
<circle cx="465" cy="322" r="9" fill="#8d5524"/><rect x="457" y="330" width="16" height="12" rx="4" fill="#3e7bfa"/>
<path d="M440 314 l28 40" stroke="#6b4226" stroke-width="4" stroke-linecap="round"/><ellipse cx="470" cy="357" rx="5" ry="9" fill="#6b4226" transform="rotate(-35 470 357)"/>
</g></g>
<g><path d="M150 268 l46 -64 l46 64z" fill="#ff6a3d"/><path d="M196 204 l0 64 l-14 0z" fill="#d94f26"/><path d="M186 268 l10 -26 l10 26z" fill="#fff2d6"/></g>
<g><path d="M250 272 l34 -46 l34 46z" fill="#3e7bfa"/><path d="M278 272 l6 -16 l6 16z" fill="#e8f1ff"/></g>
<g><rect x="340" y="176" width="4" height="100" fill="#6b4226"/><path class="flag" d="M344 180 q20 -6 40 4 q-20 8 -40 4z" fill="#22b573"/></g>
<g class="fire"><path d="M338 300 l30 -10 M338 290 l30 10" stroke="#6b4226" stroke-width="7" stroke-linecap="round"/>
<path d="M353 290 q-14 -16 -2 -34 q2 12 8 12 q-2 -10 6 -18 q6 22 -4 40z" fill="#ff8a1f"/><path d="M354 288 q-6 -8 0 -18 q4 8 6 6 q2 8 -6 12z" fill="#ffd34d"/></g>
{kid(110, 270, "#f1c27d", "#8a5cf5", "#1f3a5f", "#5a3825", "wave")}
{kid(210, 282, "#8d5524", "#ffb31f", "#22b573", "#1b1b1b", "jump")}
{kid(286, 290, "#e0ac69", "#ff6a3d", "#3e7bfa", "#c77d2a", "ball")}
<circle cx="316" cy="342" r="9" fill="#fff"/><path d="M309 338 l14 8 M316 333 v18" stroke="#1b1b1b" stroke-width="1.6"/>
<path d="M0 22 Q300 52 600 22" stroke="#6b4226" stroke-width="2" fill="none"/>
<g class="bunting">{pennants}</g>
</g></svg>'''

ICONS = {
"Little Kids": '''<svg viewBox="0 0 64 64" class="zi" aria-hidden="true"><rect x="2" y="2" width="60" height="60" rx="18" fill="#fff3d1"/><path d="M18 30 h26 l-4 22 h-18z" fill="#ff6a3d"/><path d="M18 30 q13 -14 26 0" stroke="#d94f26" stroke-width="3" fill="none"/><path d="M46 14 l-6 24" stroke="#3e7bfa" stroke-width="4" stroke-linecap="round"/><ellipse cx="47" cy="12" rx="5" ry="7" fill="#3e7bfa"/></svg>''',
"Big Kids": '''<svg viewBox="0 0 64 64" class="zi" aria-hidden="true"><rect x="2" y="2" width="60" height="60" rx="18" fill="#dff4e6"/><path d="M10 48 l22 -32 l22 32z" fill="#22b573"/><path d="M32 16 v32 l-8 0z" fill="#178a56"/><path d="M27 48 l5 -12 l5 12z" fill="#fff"/><circle cx="50" cy="16" r="6" fill="#ffb31f"/></svg>''',
"Teen Zone": '''<svg viewBox="0 0 64 64" class="zi" aria-hidden="true"><rect x="2" y="2" width="60" height="60" rx="18" fill="#ece4ff"/><path d="M20 12 l12 22 l12 -22" stroke="#8a5cf5" stroke-width="5" fill="none" stroke-linecap="round"/><rect x="20" y="32" width="24" height="20" rx="5" fill="#fff" stroke="#8a5cf5" stroke-width="3"/><path d="M26 40 h12 M26 46 h8" stroke="#8a5cf5" stroke-width="3" stroke-linecap="round"/></svg>'''}

BUNTING = "url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='120' height='26' viewBox='0 0 120 26'%3E%3Cpath d='M0 2 Q60 10 120 2' stroke='%236b4226' stroke-width='1.5' fill='none'/%3E%3Cpath d='M6 4 h18 l-9 18z' fill='%23ff6a3d'/%3E%3Cpath d='M34 6 h18 l-9 18z' fill='%233e7bfa'/%3E%3Cpath d='M64 6 h18 l-9 18z' fill='%2322b573'/%3E%3Cpath d='M94 4 h18 l-9 18z' fill='%23ffb31f'/%3E%3C/svg%3E\")"
