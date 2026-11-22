#!/usr/bin/env python3
"""Azura (Cicero, NY) — template v2 T2 page generator (websites lane, 2026-11-22, t_90aa780d).
All copy from verified-facts card body + cited sources only:
- syracuse.com opening report 2026-11-08 (partners, name story, dishes, hours, seats, renovation, Guy Hart, public opening Nov 3)
- cfood.org 2026-11 recap (Italian Food) — same facts, second source
- resy.com venue listing (owner-published: Chef Luca Cardente of Rome, Roman-style pizza, carbonara finished at your table)
- lakeshoreycc.com club page (phone echo, clubhouse location)
- GBP card: NAP + phone + 4.6/56 rating + empty website field (no-site evidence, 2026-11-22 scan)
Unknowns omitted, never guessed: menu prices, private events, parking, social profiles, email (no Azura-branded published email).
Canonical/OG pinned to the -demo host; noindex on every page (demo-host doctrine).
Geo: Google Maps q= resolution of the published address (43.2005428,-76.0522204) — see geo.json.
"""
import json, os

ORIGIN = "https://azura-demo.up.railway.app"
SITE = "Azura"
PHONE = "(315) 715-6895"
TEL = "tel:+13157156895"
RESY = "https://resy.com/cities/cicero-ny-ny/venues/azura"
# Google Maps resolves the published address to this point (output=embed state, curl 2026-11-22);
# OSM club POI agrees within ~40m (43.2016,-76.0527). See geo.json.
GEO_LAT, GEO_LON = 43.2005428, -76.0522204
MAPQ = "6777+Lakeshore+Rd,+Cicero,+NY+13039"
DIRLINK = f"https://www.google.com/maps/dir/?api=1&destination={MAPQ}"
BUILT = "<!-- BUILT-2026-11-22 -->"

SYR = "https://www.syracuse.com/restaurants/2026/11/new-lakeshore-restaurant-opens-in-onondaga-county-suburb.html"
CFOOD = "https://www.cfood.org/815990/azura-restaurant-opens-in-cicero-on-oneida-lake/"
HOOD = "https://hoodline.com/2026/11/cicero-lakefront-restaurant-azura-opens-with-oneida-lake-views-300-seats/"

def discmark():
    return ('<svg class="discmark" viewBox="0 0 24 24" aria-hidden="true" focusable="false">'
            '<circle cx="12" cy="12" r="10.5" fill="none" stroke-width="1.5"/>'
            '<circle cx="12" cy="12" r="6.5" fill="none" stroke-width="1.5"/>'
            '<circle cx="12" cy="12" r="2.6"/></svg>')

def discbig():
    return ('<svg class="discbig" viewBox="0 0 200 200" aria-hidden="true" focusable="false">'
            '<circle cx="100" cy="100" r="92" fill="none" stroke-width="2"/>'
            '<circle cx="100" cy="100" r="64" fill="none" stroke-width="2"/>'
            '<circle cx="100" cy="100" r="36" fill="none" stroke-width="2"/>'
            '<circle cx="100" cy="100" r="12"/></svg>')

HORIZON = ('<svg class="horizon" viewBox="0 0 1100 18" preserveAspectRatio="none" aria-hidden="true" focusable="false">'
           '<circle cx="550" cy="7" r="4.5" fill="currentColor" stroke="none"/>'
           '<line x1="0" y1="12" x2="1100" y2="12" stroke="currentColor" stroke-width="1.2"/></svg>')

MAP_EMBED = (f'<iframe src="https://www.google.com/maps?q={MAPQ}&output=embed" '
              f'title="Map: Azura, 6777 Lakeshore Road, Cicero, NY 13039" loading="lazy"></iframe>')

def head(path, title, desc):
    canonical = ORIGIN + ("" if path == "/" else path)
    out = [
        '<!DOCTYPE html>\n<html lang="en">\n<head>',
        BUILT,
        '<meta charset="utf-8">',
        '<meta name="viewport" content="width=device-width, initial-scale=1">',
        f'<title>{title}</title>',
        f'<meta name="description" content="{desc}">',
        '<meta name="robots" content="noindex, nofollow">',
        f'<link rel="canonical" href="{canonical}">',
        '<meta property="og:type" content="website">',
        '<meta property="og:site_name" content="Azura">',
        f'<meta property="og:title" content="{title}">',
        f'<meta property="og:description" content="{desc}">',
        f'<meta property="og:url" content="{canonical}">',
        f'<meta property="og:image" content="{ORIGIN}/og.png">',
        '<meta name="twitter:card" content="summary_large_image">',
        f'<meta name="twitter:title" content="{title}">',
        f'<meta name="twitter:description" content="{desc}">',
        f'<meta name="twitter:image" content="{ORIGIN}/og.png">',
        '<link rel="icon" href="/favicon.svg" type="image/svg+xml">',
        '<link rel="stylesheet" href="/style.css">\n</head>',
    ]
    return "\n".join(out)

BRAND = (f'<a class="brand" href="/">{discmark()}<span class="brandtext">'
         '<span class="bmark">Azura</span>'
         '<span class="bsub">Roman-Mediterranean &middot; On Oneida Lake</span></span></a>')
NAV = ('<nav aria-label="Main"><ul><li><a href="/menu">Menu</a></li>'
       '<li><a href="/our-story">Our story</a></li><li><a href="/visit">Visit</a></li>'
       '<li><a href="/contact">Contact</a></li>'
       f'<li><a class="btn gold" href="{RESY}" rel="noopener">Reserve a table</a></li></ul></nav>')
HEADER = f'<header class="site"><div class="wrap headwrap">{BRAND}{NAV}</div></header>'

FOOTER = (f'<footer class="site"><div class="wrap"><div class="foottop">'
 f'<div><p class="fbrand">{discmark()}Azura</p>'
 '<p class="ftag">Roman-inspired Mediterranean &middot; Cicero, NY</p>'
 '<div class="fnaps"><p class="ftown">Find us</p>'
 '<address class="addr">6777 Lakeshore Road, Suite 1<br>Cicero, NY 13039</address>'
 f'<p class="ftel">Phone: <a href="{TEL}">{PHONE}</a></p>'
 '<p class="fhrs">Open daily from noon &middot; until 9&nbsp;p.m. weekdays,<br>10&nbsp;p.m. weekends</p>'
 f'<p>Reservations: <a href="{RESY}" rel="noopener">Resy</a></p></div></div>'
 '<nav aria-label="Footer"><ul><li><a href="/menu">Menu</a></li><li><a href="/lunch">Lunch</a></li>'
 '<li><a href="/dinner">Dinner</a></li><li><a href="/our-story">Our story</a></li><li><a href="/visit">Visit</a></li>'
 '<li><a href="/contact">Contact</a></li><li><a href="/privacy">Privacy</a></li></ul></nav>'
 f'<p class="fpress">In the news:<br><a href="{SYR}" rel="noopener">syracuse.com</a> &middot; '
 f'<a href="{CFOOD}" rel="noopener">cfood.org</a></p>'
 '</div></div><div class="wrap"><p class="footline">&copy; 2026 Azura &middot; Roman-inspired '
 f'Mediterranean &middot; 6777 Lakeshore Road, Cicero, New York 13039 &middot; '
 f'<a href="{TEL}">{PHONE}</a></p></div></footer>')

def ld(obj):
    return '<script type="application/ld+json">\n' + json.dumps(obj, indent=1) + '\n</script>'

BIZ_ID = ORIGIN + "/#restaurant"
BIZ = {
    "@type": "Restaurant",
    "@id": BIZ_ID,
    "name": "Azura",
    "description": ("Roman-inspired Mediterranean restaurant by Chef Luca Cardente inside the renovated "
                    "Lakeshore Yacht & Country Club clubhouse at 6777 Lakeshore Road in Cicero, New York, "
                    "overlooking Oneida Lake. Opened to the public November 3, 2026."),
    "url": ORIGIN + "/",
    "image": ORIGIN + "/og.png",
    "telephone": "+1-315-715-6895",
    "address": {
        "@type": "PostalAddress",
        "streetAddress": "6777 Lakeshore Road, Suite 1",
        "addressLocality": "Cicero",
        "addressRegion": "NY",
        "postalCode": "13039",
        "addressCountry": "US",
    },
    "geo": {"@type": "GeoCoordinates", "latitude": GEO_LAT, "longitude": GEO_LON},
    "servesCuisine": ["Italian", "Mediterranean"],
    "openingDate": "2026-11-03",
    "aggregateRating": {"@type": "AggregateRating", "ratingValue": "4.6", "reviewCount": "56"},
    "sameAs": [RESY],
}

WEBSITE = {"@type": "WebSite", "@id": ORIGIN + "/#website", "name": "Azura", "url": ORIGIN + "/"}

def webpage(path, title, desc, extra=None):
    g = [WEBSITE, {
        "@type": "WebPage",
        "@id": ORIGIN + path + "#webpage",
        "name": title,
        "description": desc,
        "url": ORIGIN + ("" if path == "/" else path),
        "isPartOf": {"@id": ORIGIN + "/#website"},
        "about": {"@id": BIZ_ID},
    }]
    if extra:
        g += extra
    return ld({"@graph": g})

def breadcrumb(items):
    el = [{"@type": "ListItem", "position": i + 1, "name": n, "item": ORIGIN + u} for i, (n, u) in enumerate(items)]
    return {"@type": "BreadcrumbList", "itemListElement": el}

ORG = {"@type": "Organization", "name": "Azura", "url": ORIGIN + "/", "telephone": "+1-315-715-6895"}

def city(name):
    return {"@type": "City", "name": name}

def service(path, name, svc_type, desc):
    return {
        "@type": "Service", "@id": ORIGIN + path + "#service",
        "name": name, "serviceType": svc_type, "description": desc,
        "url": ORIGIN + path,
        "areaServed": city("Cicero"),
        "provider": ORG,
    }

# --------------------------------------------------------------- copy constants

FAQ = {
    "@type": "FAQPage",
    "mainEntity": [
        {"@type": "Question", "name": "When are you open?",
         "acceptedAnswer": {"@type": "Answer", "text": "Every day from noon: until 9 p.m. Monday through Friday, until 10 p.m. on weekends, as reported by syracuse.com at the public opening in November 2026."}},
        {"@type": "Question", "name": "Do I need a reservation?",
         "acceptedAnswer": {"@type": "Answer", "text": "Dinner reservations open on Resy, and the restaurant answers (315) 715-6895."}},
        {"@type": "Question", "name": "When did Azura open?",
         "acceptedAnswer": {"@type": "Answer", "text": "Azura opened to the public on November 3, 2026, after several months serving country-club members, who tested the menu and gave feedback first."}},
        {"@type": "Question", "name": "What kind of food do you serve?",
         "acceptedAnswer": {"@type": "Answer", "text": "Roman-inspired Italian-Mediterranean cooking from Chef Luca Cardente, who grew up in Rome: handmade pasta, rigatoni with vodka sauce, a carbonara finished at your table, Roman-style pizza and fresh seafood, including sea bass and salmon plates."}},
        {"@type": "Question", "name": "Is it really on the lake?",
         "acceptedAnswer": {"@type": "Answer", "text": "Yes — the dining room overlooks Oneida Lake from the renovated clubhouse of the Lakeshore Yacht & Country Club in Cicero, New York. The restaurant is named for the lake's sky-blue color."}},
    ],
}

HOME_FAQ_HTML = "\n".join(
    f'<details><summary>{q}</summary><p>{a["acceptedAnswer"]["text"]}</p></details>'
    for q, a in [(x["name"], x) for x in FAQ["mainEntity"]])


def platecard(num, name, desc, source):
    return (f'<article class="plate"><p class="pnum">{num}</p>'
            f'<h3>{name}</h3><p class="pdesc">{desc}</p>'
            f'<p class="psrc">per {source}</p></article>')

PLATES = [
    ("I", "Pasta, handmade",
     "Rigatoni with vodka sauce. Handmade ravioli. A carbonara finished at your table &mdash; the dishes the "
     "kitchen builds its name on.", "syracuse.com &amp; resy.com"),
    ("II", "From the sea",
     "Fresh seafood on the lakeshore &mdash; sea bass and salmon plates among them, as the opening coverage "
     "describes the menu.", "syracuse.com"),
    ("III", "Roman-style pizza",
     "Roman-style pizza, on the menu alongside the pasta &mdash; &ldquo;the dishes Chef Luca Cardente grew "
     "up with in Rome.&rdquo;", "resy.com"),
]

HOME_PLATES = "\n".join(platecard(*p) for p in PLATES)

HRS_TABLE = ('<table class="hrs"><thead><tr><th>Day</th><th>Hours</th></tr></thead><tbody>'
             '<tr><td>Monday &ndash; Friday</td><td>12:00 noon &ndash; 9:00 p.m.</td></tr>'
             '<tr><td>Saturday &amp; Sunday</td><td>12:00 noon &ndash; 10:00 p.m.</td></tr></tbody></table>')

# ---------------------------------------------------------------- pages

HOME = f"""<body>
<a class="skip" href="#main">Skip to content</a>
{HEADER}
<main id="main">

<section class="band ink hero"><div class="wrap heroinner">
  {discbig()}
  <p class="eyebrow">Open daily from noon &middot; Roman-inspired Mediterranean &middot; Cicero, NY</p>
  <h1>The color of the lake. The cooking of Rome.</h1>
  <p class="lede">Azura is the Roman-inspired Mediterranean restaurant inside the renovated clubhouse of the
  Lakeshore Yacht &amp; Country Club, looking out over Oneida Lake. The kitchen &mdash; led by Chef Luca
  Cardente, who grew up in Rome &mdash; makes the dishes he grew up with: handmade pasta, Roman-style pizza
  and fresh seafood. Opened to the public November 3, 2026, after the menu was previewed with club members
  for months.</p>
  <div class="ctarow"><a class="btn gold" href="{RESY}" rel="noopener">Reserve a table</a>
  <a class="btn" href="/menu">See the menu</a>
  <a class="btn ghost" href="{DIRLINK}" rel="noopener">Get directions</a></div>
  <p class="status"><span>Open daily from noon</span><span>&middot;</span>
  <span>9&nbsp;p.m. weekdays &middot; 10&nbsp;p.m. weekends</span><span>&middot;</span>
  <span>4.6 on Google &mdash; 56 reviews</span></p>
</div></section>

<section class="band cream"><div class="wrap">
  <p class="eyebrow dark">The menu, in brief</p>
  <h2 class="sec">Pasta, the sea and Roman-style pizza.</h2>
  <p class="secsub">What the kitchen and the opening coverage single out &mdash; the full menu, with prices,
  is at the restaurant.</p>
  <div class="plategrid">
    {HOME_PLATES}
  </div>
  <p class="ctaend"><a class="lk" href="/menu">The menu in full &rarr;</a></p>
</div></section>

<section class="band ink"><div class="wrap">
  {HORIZON}
  <p class="eyebrow">The name</p>
  <figure class="quoteblock"><p class="qx">The name Azura refers to the sky-blue look of Oneida Lake
  &mdash; the color of the water the dining room overlooks.</p>
  <figcaption>From syracuse.com&rsquo;s opening report</figcaption></figure>
  <p class="secsub">Two of the four partners behind Inka&rsquo;s and Margarita&rsquo;s in Syracuse built it,
  with nearly 300 covers across the clubhouse, about 200 of them in the main dining room, plus two bars.</p>
  <p class="ctaend"><a class="lk" href="/our-story">The full story &rarr;</a></p>
</div></section>

<section class="band mist"><div class="wrap">
  <p class="eyebrow dark">Lunch and dinner</p>
  <div class="splitgrid">
    <div class="infocard"><h3 class="infh">Lunch</h3>
      <p class="note">We open at noon every day. Lunch is lake views early, pasta and Roman-style pizza
      before the afternoon.</p>
      <p class="bigm"><a href="/lunch">Lunch at Azura</a></p></div>
    <div class="infocard"><h3 class="infh">Dinner</h3>
      <p class="note">Dinner runs until 9&nbsp;p.m. on weekdays and 10&nbsp;p.m. on weekends &mdash; sea bass,
      handmade pasta and a carbonara finished at your table.</p>
      <p class="bigm"><a href="/dinner">Dinner &amp; reservations</a></p></div>
  </div>
</div></section>

<section class="band cream"><div class="wrap">
  <p class="eyebrow dark">Visit</p>
  <div class="splitgrid">
    <div class="infocard"><h3 class="infh">Address</h3>
      <address class="addr">6777 Lakeshore Road, Suite 1<br>Cicero, NY 13039</address>
      <p class="note">Inside the Lakeshore Yacht &amp; Country Club clubhouse, on the Cicero shore of
      Oneida Lake.</p>
      <p class="bigm"><a href="{DIRLINK}" rel="noopener">Get directions</a></p></div>
    <div class="infocard"><h3 class="infh">Hours &amp; phone</h3>
      {HRS_TABLE}
      <p class="bigm"><a href="{TEL}">{PHONE}</a></p></div>
  </div>
  <div class="mapcell">{MAP_EMBED}</div>
  <p class="fineprint">Map: Azura, 6777 Lakeshore Road, Cicero, NY 13039.</p>
</div></section>

<section class="band ink"><div class="wrap narrow center">
  <p class="eyebrow">Come as you are</p>
  <h2 class="sec">Reserve on Resy, or just call.</h2>
  <p class="secsub">Tables open on Resy for dinner service. For anything else &mdash; a big table, a question,
  a correction &mdash; call the restaurant at {PHONE}.</p>
  <div class="ctarow"><a class="btn gold" href="{RESY}" rel="noopener">Reserve on Resy</a>
  <a class="btn ghost" href="/contact">Send a note</a></div>
</div></section>

<section class="band mist"><div class="wrap narrow faq">
  <p class="eyebrow dark">Short answers</p>
  <h2 class="sec">Before you come</h2>
  {HOME_FAQ_HTML}
</div></section>

</main>
{FOOTER}
</body>
</html>"""

MENU = f"""<body>
<a class="skip" href="#main">Skip to content</a>
{HEADER}
<main id="main">

<section class="band ink herol"><div class="wrap">
  <p class="eyebrow">The menu</p>
  <h1>Pasta, pizza and the sea &mdash; the way Rome does them.</h1>
  <p class="lede">Azura&rsquo;s menu is Roman-inspired Mediterranean cooking, built around the dishes Chef
  Luca Cardente grew up with in Rome. Handmade pasta, Roman-style pizza and fresh seafood pour alongside
  wine and the two bars. The full menu, with prices, is at the restaurant.</p>
</div></section>

<section class="band cream"><div class="wrap">
  <p class="eyebrow dark">What the kitchen is known for</p>
  <h2 class="sec">The plates, so far</h2>
  <div class="plategrid">
    {HOME_PLATES}
  </div>
  <p class="fineprint">Plates as described by the restaurant&rsquo;s own Resy listing and by syracuse.com&rsquo;s
  opening report. Prices and the full menu live at the restaurant &mdash; this list names the plates the
  kitchen and the press single out.</p>
</div></section>

<section class="band mist"><div class="wrap">
  {HORIZON}
  <p class="eyebrow dark">Meal times</p>
  <div class="splitgrid">
    <div class="infocard"><h3 class="infh">Lunch &middot; from noon, daily</h3>
      <p class="note">Midday on the lake: pasta, Roman-style pizza and seafood from noon.</p>
      <p class="bigm"><a href="/lunch">Lunch at Azura</a></p></div>
    <div class="infocard"><h3 class="infh">Dinner &middot; until 9 / 10 p.m.</h3>
      <p class="note">Evenings run to 9&nbsp;p.m. on weekdays and 10&nbsp;p.m. on weekends. Reserve ahead
      on Resy.</p>
      <p class="bigm"><a href="/dinner">Dinner &amp; reservations</a></p></div>
  </div>
</div></section>

<section class="band ink"><div class="wrap narrow prose">
  <h2 class="sec">About the kitchen</h2>
  <p class="first">The cooking starts in Rome. Chef Luca Cardente grew up there, and the menu is built from
  the dishes he grew up with &mdash; pasta made by hand, a carbonara finished at your table, Roman-style
  pizza &mdash; laid over the Mediterranean&rsquo;s other traditions, seafood included.</p>
  <p>Before opening to the public on November 3, the menu ran for months in front of Lakeshore Yacht
  &amp; Country Club members, who tested dishes and gave feedback. &ldquo;We have tested our menu, and we
  feel like we have what the community wants,&rdquo; partner Alejandro Gonzalez told syracuse.com.</p>
  <p><a class="lk" href="/our-story">The full story &rarr;</a></p>
</div></section>

<section class="band cream"><div class="wrap narrow center">
  <h2 class="sec">Questions about the menu?</h2>
  <p class="secsub">Ask about a dish or the full list &mdash; the form goes straight to the restaurant&rsquo;s inbox.</p>
  <div class="ctarow"><a class="btn gold" href="/contact">Send a note</a>
  <a class="btn ghost" href="{TEL}">Call {PHONE}</a></div>
</div></section>

</main>
{FOOTER}
</body>
</html>"""

MENU_SCHEMA = {
    "@type": "Menu", "@id": ORIGIN + "/menu#menu", "name": "Azura — menu highlights",
    "inLanguage": "en",
    "hasMenuSection": [
        {"@type": "MenuSection", "name": "Pasta", "hasMenuItem": [
            {"@type": "MenuItem", "name": "Rigatoni with vodka sauce",
             "description": "A signature of the Roman-inspired kitchen, per syracuse.com's opening report."},
            {"@type": "MenuItem", "name": "Handmade ravioli",
             "description": "Pasta made by hand, per syracuse.com's opening report."},
            {"@type": "MenuItem", "name": "Carbonara, finished at your table",
             "description": "The dish the restaurant's own Resy listing singles out."}]},
        {"@type": "MenuSection", "name": "From the sea", "hasMenuItem": [
            {"@type": "MenuItem", "name": "Sea bass",
             "description": "A signature plate, per syracuse.com's opening report."},
            {"@type": "MenuItem", "name": "Salmon plates",
             "description": "Among the dishes featured on the menu, per syracuse.com."}]},
        {"@type": "MenuSection", "name": "Roman-style pizza", "hasMenuItem": [
            {"@type": "MenuItem", "name": "Roman-style pizza",
             "description": "On the menu alongside the pasta, per the restaurant's Resy listing."}]},
    ],
}

OURSTORY = f"""<body>
<a class="skip" href="#main">Skip to content</a>
{HEADER}
<main id="main">

<section class="band ink herol"><div class="wrap">
  <p class="eyebrow">Our story</p>
  <h1>A Rome kitchen, on a New York lake.</h1>
  <p class="lede">Azura began as the clubhouse of the Lakeshore Yacht &amp; Country Club in Cicero &mdash;
  renovated this year into a restaurant of nearly 300 covers that looks straight out over Oneida Lake.</p>
</div></section>

<section class="band cream"><div class="wrap">
  <ol class="tl">
    <li><span class="tyear">The club</span><span class="tbody"><strong>A lakeshore clubhouse.</strong>
      The building sits on the Cicero shore of Oneida Lake, part of the Lakeshore Yacht &amp; Country Club.
      Building owner Guy Hart spent about $500,000 renovating the clubhouse for the restaurant, the
      syracuse.com opening report says.</span></li>
    <li><span class="tyear">The partners</span><span class="tbody"><strong>The Inka&rsquo;s team, at the
      lake.</strong> Jose Avalos-Rios and Alejandro Gonzalez &mdash; two of the four partners behind
      Inka&rsquo;s and Margarita&rsquo;s in Syracuse &mdash; took on Azura, with Andrew McDermott and
      Sebastian Ramirez running day-to-day operations.</span></li>
    <li><span class="tyear">The kitchen</span><span class="tbody"><strong>A chef from Rome.</strong> Chef
      Luca Cardente grew up in Rome; the menu is built around the dishes he grew up with &mdash; handmade
      pasta, a carbonara finished at your table, Roman-style pizza, fresh seafood.</span></li>
    <li><span class="tyear">2026</span><span class="tbody"><strong>First the members, then everyone.</strong>
      For several months Azura served only country-club members, who tested dishes and gave feedback. It
      opened to the public on Tuesday, November 3, 2026.</span></li>
  </ol>
</div></section>

<section class="band ink"><div class="wrap">
  {HORIZON}
  <p class="eyebrow">The name</p>
  <figure class="quoteblock"><p class="qx">&ldquo;It&rsquo;s all very exciting. We have tested our menu,
  and we feel like we have what the community wants.&rdquo;</p>
  <figcaption>Alejandro Gonzalez, partner &mdash; syracuse.com, November 2026</figcaption></figure>
  <div class="prose">
    <p class="first">The name Azura refers to the sky-blue look of Oneida Lake, Gonzalez told
    syracuse.com &mdash; the color of the water the dining room overlooks.</p>
    <p>The room itself is big by Upstate clubhouse standards: nearly 200 seats in the main dining room,
    nearly 300 across the whole space, with two bars. The restaurant is the first piece of a planned
    lakeshore redevelopment &mdash; owner Guy Hart has said shops and apartments are coming to the
    property down the road.</p>
  </div>
</div></section>

<section class="band mist"><div class="wrap">
  <p class="eyebrow dark">In the news</p>
  <ul class="presslist">
    <li><span class="pout">syracuse.com</span>
      <a href="{SYR}" rel="noopener">&ldquo;New lakeshore restaurant opens in Onondaga County suburb&rdquo;
      &mdash; the November 8, 2026 opening report</a></li>
    <li><span class="pout">cfood.org</span>
      <a href="{CFOOD}" rel="noopener">&ldquo;Azura Restaurant Opens in Cicero on Oneida Lake&rdquo;</a></li>
    <li><span class="pout">Hoodline</span>
      <a href="{HOOD}" rel="noopener">&ldquo;Cicero lakefront restaurant Azura opens with Oneida Lake
      views, 300 seats&rdquo;</a></li>
  </ul>
  <p class="fineprint">Story details, dates and menu descriptions as reported by these outlets and by the
  restaurant&rsquo;s own Resy listing.</p>
</div></section>

<section class="band cream"><div class="wrap narrow center">
  <h2 class="sec">Come see the lake at table height.</h2>
  <p class="secsub">Dinner reservations open on Resy &mdash; or call {PHONE} and talk to a person.</p>
  <div class="ctarow"><a class="btn gold" href="{RESY}" rel="noopener">Reserve on Resy</a>
  <a class="btn ghost" href="/menu">See the menu</a></div>
</div></section>

</main>
{FOOTER}
</body>
</html>"""

LUNCH = f"""<body>
<a class="skip" href="#main">Skip to content</a>
{HEADER}
<main id="main">

<section class="band ink herol"><div class="wrap">
  <p class="eyebrow">Lunch &middot; from noon, every day</p>
  <h1>Noon on the lake.</h1>
  <p class="lede">Azura opens at noon every day &mdash; early tables face Oneida Lake, and the kitchen starts
  with the Roman plates: handmade pasta, Roman-style pizza, fresh seafood. The two bars are pouring while
  you decide.</p>
</div></section>

<section class="band cream"><div class="wrap">
  <p class="eyebrow dark">Lunch at Azura</p>
  <div class="plategrid">
    {HOME_PLATES}
  </div>
  <p class="fineprint">Plates as described by the restaurant and syracuse.com. The full lunch menu, with
  prices, is at the restaurant.</p>
</div></section>

<section class="band mist"><div class="wrap">
  <p class="eyebrow dark">When</p>
  <div class="splitgrid">
    <div class="infocard"><h3 class="infh">Hours</h3>
      {HRS_TABLE}
      <p class="note">Lunch starts at noon on every day of the week.</p>
      <p class="bigm"><a href="{TEL}">{PHONE}</a></p></div>
    <div class="infocard"><h3 class="infh">Where</h3>
      <address class="addr">6777 Lakeshore Road, Suite 1<br>Cicero, NY 13039</address>
      <p class="note">The Lakeshore Yacht &amp; Country Club clubhouse, Cicero shore of Oneida Lake.</p>
      <p class="bigm"><a href="{DIRLINK}" rel="noopener">Get directions</a></p></div>
  </div>
  <div class="mapcell">{MAP_EMBED}</div>
  <p class="fineprint">Map: Azura, 6777 Lakeshore Road, Cicero, NY 13039.</p>
</div></section>

<section class="band ink"><div class="wrap narrow center">
  <h2 class="sec">Lunch, then the afternoon on the water.</h2>
  <p class="secsub">Questions about lunch &mdash; the form goes straight to the restaurant&rsquo;s inbox.</p>
  <div class="ctarow"><a class="btn gold" href="/contact">Send a note</a>
  <a class="btn ghost" href="/dinner">Dinner &amp; reservations</a></div>
</div></section>

</main>
{FOOTER}
</body>
</html>"""

DINNER = f"""<body>
<a class="skip" href="#main">Skip to content</a>
{HEADER}
<main id="main">

<section class="band ink herol"><div class="wrap">
  <p class="eyebrow">Dinner &middot; until 9 p.m. weekdays, 10 p.m. weekends</p>
  <h1>Dinner, and the sun going out over Oneida Lake.</h1>
  <p class="lede">Dinner at Azura runs to 9&nbsp;p.m. on weekdays and 10&nbsp;p.m. on weekends. Order the
  rigatoni with vodka sauce, the sea bass, the handmade ravioli &mdash; and let the kitchen finish your
  carbonara at the table.</p>
</div></section>

<section class="band cream"><div class="wrap">
  <p class="eyebrow dark">The table</p>
  <div class="plategrid">
    {HOME_PLATES}
  </div>
  <p class="fineprint">Plates as described by the restaurant and syracuse.com. The full dinner menu, with
  prices, is at the restaurant.</p>
</div></section>

<section class="band mist"><div class="wrap">
  <p class="eyebrow dark">Reserve dinner</p>
  <div class="splitgrid">
    <div class="infocard"><h3 class="infh">Resy</h3>
      <p class="note">Azura&rsquo;s dinner reservations open on Resy &mdash; pick the date, the time and the
      party, and you&rsquo;re set.</p>
      <p class="bigm"><a href="{RESY}" rel="noopener">Reserve on Resy</a></p></div>
    <div class="infocard"><h3 class="infh">Hours</h3>
      {HRS_TABLE}
      <p class="bigm"><a href="{TEL}">{PHONE}</a></p></div>
  </div>
  <div class="mapcell">{MAP_EMBED}</div>
  <p class="fineprint">Map: Azura, 6777 Lakeshore Road, Cicero, NY 13039.</p>
</div></section>

<section class="band ink"><div class="wrap narrow center">
  <h2 class="sec">A big table, or something to ask?</h2>
  <p class="secsub">Call {PHONE}, or send a note &mdash; the form goes straight to the restaurant&rsquo;s inbox.</p>
  <div class="ctarow"><a class="btn gold" href="/contact">Send a note</a>
  <a class="btn ghost" href="/menu">See the menu</a></div>
</div></section>

</main>
{FOOTER}
</body>
</html>"""

VISIT = f"""<body>
<a class="skip" href="#main">Skip to content</a>
{HEADER}
<main id="main">

<section class="band ink herol"><div class="wrap">
  <p class="eyebrow">Visit</p>
  <h1>6777 Lakeshore Road.</h1>
  <p class="lede">Azura sits inside the renovated Lakeshore Yacht &amp; Country Club clubhouse, on the Cicero
  shore of Oneida Lake &mdash; open daily from noon, until 9&nbsp;p.m. weekdays and 10&nbsp;p.m. weekends.</p>
</div></section>

<section class="band cream"><div class="wrap">
  <div class="splitgrid">
    <div class="infocard"><h3 class="infh">Address</h3>
      <address class="addr">6777 Lakeshore Road, Suite 1<br>Cicero, NY 13039</address>
      <p class="note">The clubhouse of the Lakeshore Yacht &amp; Country Club, facing Oneida Lake.</p>
      <p class="bigm"><a href="{DIRLINK}" rel="noopener">Get directions</a></p></div>
    <div class="infocard"><h3 class="infh">Hours</h3>
      {HRS_TABLE}
      <p class="bigm"><a href="{TEL}">{PHONE}</a></p></div>
    <div class="infocard"><h3 class="infh">Reservations</h3>
      <p class="note">Dinner tables open on Resy. For anything Resy doesn&rsquo;t cover, call the restaurant.</p>
      <p class="bigm"><a href="{RESY}" rel="noopener">Reserve on Resy</a></p></div>
  </div>
</div></section>

<section class="band mist"><div class="wrap">
  <div class="mapcell">{MAP_EMBED}</div>
  <p class="fineprint">Map: Azura, 6777 Lakeshore Road, Cicero, NY 13039.</p>
</div></section>

<section class="band ink"><div class="wrap narrow center">
  <h2 class="sec">Coming for the first time?</h2>
  <p class="secsub">The main dining room holds nearly 200, the whole space nearly 300 &mdash; ask for a
  lake-facing table when you book.</p>
  <div class="ctarow"><a class="btn gold" href="{RESY}" rel="noopener">Reserve on Resy</a>
  <a class="btn ghost" href="/contact">Send a note</a></div>
</div></section>

</main>
{FOOTER}
</body>
</html>"""

CONTACT = f"""<body>
<a class="skip" href="#main">Skip to content</a>
{HEADER}
<main id="main">

<section class="band ink herol"><div class="wrap">
  <p class="eyebrow">Contact</p>
  <h1>Talk to the restaurant.</h1>
  <p class="lede">Call {PHONE} &mdash; or use the form and your note goes straight to the
  restaurant&rsquo;s inbox. No newsletter, no mailing list &mdash; just a reply.</p>
</div></section>

<section class="band cream"><div class="wrap contactgrid">
  <div class="formside"><form class="cform" method="post" action="/contact" accept-charset="utf-8">
    <h2 class="infh">Leave a note</h2>
    <div class="fields">
      <div class="field"><label for="f-name">Name</label><input id="f-name" name="name" required autocomplete="name"></div>
      <div class="field"><label for="f-phone">Phone <span class="opt">(optional)</span></label><input id="f-phone" name="phone" type="tel" autocomplete="tel"></div>
      <div class="field full"><label for="f-email">Email <span class="opt">(optional &mdash; so we can answer)</span></label><input id="f-email" name="email" type="email" autocomplete="email"></div>
      <div class="field full"><label for="f-msg">Your message</label><textarea id="f-msg" name="message" required></textarea></div>
    </div>
    <button class="btn gold" type="submit">Send note</button>
    <p class="fineprint">We read every note and answer from the restaurant&rsquo;s inbox. Nothing is added
    to a mailing list &mdash; the inbox never becomes one.</p>
  </form></div>
  <div class="infoside">
    <div class="infocard"><h3 class="infh">Phone</h3>
      <p class="bigm"><a href="{TEL}">{PHONE}</a></p>
      <p class="note">Published on the restaurant&rsquo;s Google listing.</p></div>
    <div class="infocard"><h3 class="infh">Reservations</h3>
      <p class="note">Dinner tables book on Resy.</p>
      <p class="bigm"><a href="{RESY}" rel="noopener">Reserve on Resy</a></p></div>
    <div class="infocard"><h3 class="infh">Address</h3>
      <address class="addr">6777 Lakeshore Road, Suite 1<br>Cicero, NY 13039</address>
      <p class="note"><a class="lk" href="{DIRLINK}" rel="noopener">Directions</a> &middot;
      <a class="lk" href="/visit">Visiting details</a></p></div>
  </div>
</div></section>

<section class="band mist"><div class="wrap">
  <div class="mapcell">{MAP_EMBED}</div>
  <p class="fineprint">Map: Azura, 6777 Lakeshore Road, Cicero, NY 13039.</p>
</div></section>

</main>
{FOOTER}
</body>
</html>"""

PRIVACY = f"""<body>
<a class="skip" href="#main">Skip to content</a>
{HEADER}
<main id="main">

<section class="band ink herol"><div class="wrap">
  <p class="eyebrow">Privacy</p>
  <h1>Plain words about your data.</h1>
</div></section>

<section class="band cream"><div class="wrap narrow prose">
  <p class="first"><strong>Last updated November 22, 2026.</strong> This website is published for Azura.
  It sets no cookies of its own, runs no third-party scripts, and keeps no analytics &mdash; pages are
  plain text and one stylesheet.</p>
  <h3 class="h4">The note form</h3>
  <p>When you submit the contact form, the name, phone, email and message you type are sent to the
  restaurant&rsquo;s inbox through an email-delivery service, so a person can answer. That is the entire
  purpose. Nothing is sold, rented, or added to a mailing list.</p>
  <h3 class="h4">Maps</h3>
  <p>Pages with a map load a Google Maps embed, which may set Google&rsquo;s own cookies once you look at
  it. Google&rsquo;s privacy policy covers what Google does with those.</p>
  <h3 class="h4">Your choices</h3>
  <p>Want a note deleted after it&rsquo;s answered? Reply to the email you receive and say so.</p>
  <h3 class="h4">Questions</h3>
  <p>Call <a href="{TEL}">{PHONE}</a>, or remember the address: 6777 Lakeshore Road, Suite 1, Cicero,
  NY 13039.</p>
</div></section>

</main>
{FOOTER}
</body>
</html>"""

THANKS = f"""<body>
<a class="skip" href="#main">Skip to content</a>
{HEADER}
<main id="main">

<section class="band ink herol"><div class="wrap narrow center">
  <p class="eyebrow">Note received</p>
  <h1>Your note landed.</h1>
  <p class="lede">The team reads every one from the restaurant&rsquo;s inbox. If you wrote about a table,
  expect a reply with the details.</p>
  <div class="ctarow"><a class="btn gold" href="/">Back to the front page</a>
  <a class="btn ghost" href="/menu">See the menu</a></div>
</div></section>

</main>
{FOOTER}
</body>
</html>"""

NOTFOUND = f"""<body>
<a class="skip" href="#main">Skip to content</a>
{HEADER}
<main id="main">

<section class="band ink herol"><div class="wrap narrow center">
  <p class="eyebrow">404</p>
  <h1>This page is out on the water.</h1>
  <p class="lede">We couldn&rsquo;t find it. Try one of these:</p>
  <div class="ctarow"><a class="btn gold" href="/">Front page</a>
  <a class="btn ghost" href="/menu">Menu</a>
  <a class="btn ghost" href="/contact">Contact</a></div>
</div></section>

</main>
{FOOTER}
</body>
</html>"""

# titles / descs
TITLES = {
    "/": ("Azura &mdash; Roman-Inspired Mediterranean Restaurant on Oneida Lake | Cicero, NY",
          "Azura serves Roman-inspired Mediterranean cooking &mdash; handmade pasta, Roman-style pizza and fresh seafood &mdash; overlooking Oneida Lake in Cicero, NY. Open daily from noon. (315) 715-6895."),
    "/menu": ("The Menu &mdash; Pasta, Roman-Style Pizza &amp; Fresh Seafood | Azura, Cicero, NY",
              "Handmade pasta, rigatoni with vodka sauce, carbonara finished at your table, Roman-style pizza and fresh seafood from Chef Luca Cardente's Rome. Azura, Cicero, NY."),
    "/lunch": ("Lunch from Noon, Every Day &mdash; Azura, Cicero, NY",
               "Azura opens at noon daily on the Cicero shore of Oneida Lake: handmade pasta, Roman-style pizza and fresh seafood for lunch, with lake-facing tables."),
    "/dinner": ("Dinner &amp; Reservations on Resy &mdash; Azura, Cicero, NY",
                "Dinner at Azura runs to 9 p.m. weekdays and 10 p.m. weekends: sea bass, handmade pasta and a carbonara finished at your table. Reserve dinner on Resy."),
    "/our-story": ("Our Story &mdash; Rome, Oneida Lake &amp; the Lakeshore Clubhouse | Azura, Cicero, NY",
                   "The partners behind Inka's and Margarita's, a chef from Rome and a $500,000 clubhouse renovation: how Azura came to the Cicero shore of Oneida Lake."),
    "/visit": ("Visit &mdash; Hours, Directions &amp; Reservations | Azura, Cicero, NY",
               "Azura at 6777 Lakeshore Road, Cicero, NY 13039: hours daily from noon, directions to the Lakeshore Yacht & Country Club clubhouse, phone and Resy reservations."),
    "/contact": ("Contact Azura &mdash; (315) 715-6895, Cicero, NY",
                 "Call (315) 715-6895 or use the form &mdash; Azura answers from the restaurant's inbox. 6777 Lakeshore Road, Suite 1, Cicero, NY 13039."),
    "/privacy": ("Privacy &mdash; Azura, Cicero, NY",
                 "No cookies, no third-party scripts, no analytics. Contact-form notes go straight to the restaurant's inbox and nowhere else."),
    "/thanks": ("Note received &mdash; Azura, Cicero, NY",
                "Your note went straight to the Azura inbox. The team reads and answers every one."),
    "/404": ("Page not found &mdash; Azura, Cicero, NY",
             "That page couldn't be found. Head back to the front page, the menu, or contact."),
}

def plain(s):
    return (s.replace("&rsquo;", "'").replace("&ldquo;", "\u201c").replace("&rdquo;", "\u201d")
             .replace("&mdash;", "\u2014").replace("&middot;", "\u00b7").replace("&amp;", "&")
             .replace("&nbsp;", " ").replace("&rarr;", "\u2192").replace("&ndash;", "\u2013"))

def ld_webpage(path, extra=None):
    t, d = TITLES[path]
    return webpage(path, plain(t), plain(d), extra=extra)

PAGES = [
    ("/", "index.html", HOME, [BIZ, FAQ]),
    ("/menu", "menu.html", MENU, [
        service("/menu", "Azura menu — Roman-inspired Mediterranean plates", "Food service",
                "Handmade pasta, Roman-style pizza, fresh seafood and a carbonara finished at your table, from Chef Luca Cardente's Rome."),
        MENU_SCHEMA,
        breadcrumb([("Home", "/"), ("Menu", "/menu")])]),
    ("/lunch", "lunch.html", LUNCH, [
        service("/lunch", "Lunch at Azura, Cicero NY", "Lunch service",
                "Lunch daily from noon at Azura — handmade pasta, Roman-style pizza and fresh seafood overlooking Oneida Lake, Cicero, NY."),
        breadcrumb([("Home", "/"), ("Lunch", "/lunch")])]),
    ("/dinner", "dinner.html", DINNER, [
        service("/dinner", "Dinner and reservations at Azura, Cicero NY", "Dinner service",
                "Dinner at Azura to 9 p.m. weekdays and 10 p.m. weekends; dinner reservations open on Resy."),
        breadcrumb([("Home", "/"), ("Dinner", "/dinner")])]),
    ("/our-story", "our-story.html", OURSTORY, [
        breadcrumb([("Home", "/"), ("Our story", "/our-story")])]),
    ("/visit", "visit.html", VISIT, [
        service("/visit", "Visit Azura, Cicero NY", "Restaurant visit information",
                "Hours, directions to 6777 Lakeshore Road and dinner reservations for Azura on the Cicero shore of Oneida Lake."),
        breadcrumb([("Home", "/"), ("Visit", "/visit")])]),
    ("/contact", "contact.html", CONTACT, [
        breadcrumb([("Home", "/"), ("Contact", "/contact")])]),
    ("/privacy", "privacy.html", PRIVACY, None),
    ("/thanks", "thanks.html", THANKS, None),
    ("/404", "404.html", NOTFOUND, None),
]

CORE = ["/", "/menu", "/lunch", "/dinner", "/our-story", "/visit", "/contact", "/privacy"]

for path, fname, body, extra in PAGES:
    t, d = TITLES[path]
    if path in ["/", "/menu", "/our-story", "/visit", "/contact", "/privacy", "/lunch", "/dinner"]:
        doc = head(path, t, d) + "\n" + ld_webpage(path, extra=extra) + "\n" + body
    else:
        doc = head(path, t, d) + "\n" + body
    with open(os.path.join("public", fname), "w", encoding="utf-8") as f:
        f.write(doc)

today = "2026-11-22"
urls = "\n".join(f'<url><loc>{ORIGIN}{p}</loc><lastmod>{today}</lastmod></url>' for p in CORE)
sitemap = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + urls + "\n</urlset>\n")
open("public/sitemap.xml", "w").write(sitemap)
open("public/robots.txt", "w").write(
    f"User-agent: *\nDisallow: /thanks\nDisallow: /404\n\nSitemap: {ORIGIN}/sitemap.xml\n")

print("wrote", len(PAGES) + 2, "files")
