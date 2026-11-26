# Generates the static site (Arabic, RTL). Run: python3 tools/build_site.py  (from the cute-ghost folder)
import re, os, html
BASE = "https://belalmomani.github.io/GitHubPages/cute-ghost/"
EMAIL = "bilalalmomani90@gmail.com"
PKG = "com.companion.theghost"
PLAY_URL = ""   # put the Google Play link here after publishing, then re-run
DATE = "2026-11-26"
NAME = "الشبح اللطيف"
KW = "الشبح اللطيف, Cute Ghost, لعبة أطفال, ألعاب للأطفال الصغار, لعبة شبح, لعبة للأطفال بدون إنترنت, تطبيق أطفال آمن, ألعاب أندرويد للأطفال, Google Play"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PRIV = open(os.path.join(ROOT, "tools", "privacy_ar.md"), encoding="utf-8").read()

NAV = [("index.html","الرئيسية"),("features.html","عن اللعبة"),("parents.html","للأهل"),
       ("privacy.html","الخصوصية"),("delete-data.html","حذف البيانات"),("contact.html","اتصل بنا")]

def md(t):
    out, ul = [], False
    for l in t.split("\n"):
        l = html.escape(l.strip(), quote=False)
        l = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", l)
        l = re.sub(r"(https://[^\s<)]+)", r'<a href="\1" rel="noopener">\1</a>', l)
        if l.startswith("- ") or l.startswith("• "):
            if not ul: out.append("<ul>"); ul = True
            out.append("<li>%s</li>" % l[2:]); continue
        if ul: out.append("</ul>"); ul = False
        if l.startswith("## "): out.append("<h2>%s</h2>" % l[3:])
        elif l.startswith("# "): continue
        elif l: out.append("<p>%s</p>" % l)
    if ul: out.append("</ul>")
    return "\n".join(out)

def page(fn, title, desc, body, jsonld="", h1=None):
    url = BASE + ("" if fn == "index.html" else fn)
    nav = "".join('<a href="%s"%s>%s</a>' % (f, ' aria-current="page"' if f == fn else "", t) for f, t in NAV)
    full = f"{title} | {NAME} - Cute Ghost" if fn != "index.html" else title
    s = f'''<!doctype html>
<html lang="ar" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{full}</title>
<meta name="description" content="{desc}">
<meta name="keywords" content="{KW}">
<meta name="robots" content="index, follow, max-image-preview:large">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#7C5CFF">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{NAME} - Cute Ghost">
<meta property="og:locale" content="ar_AR">
<meta property="og:title" content="{full}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}assets/og-image.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{full}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{BASE}assets/og-image.png">
<link rel="icon" type="image/png" sizes="32x32" href="assets/favicon-32.png">
<link rel="apple-touch-icon" href="assets/apple-touch-icon.png">
<link rel="manifest" href="site.webmanifest">
<link rel="stylesheet" href="assets/style.css">
<!-- Verification (add after creating the properties):
<meta name="google-site-verification" content="CODE">
<meta name="msvalidate.01" content="CODE"> -->
{jsonld}
</head>
<body>
<a class="skip" href="#main">تخطَّ إلى المحتوى</a>
<header><div class="wrap bar">
<a class="brand" href="index.html"><img src="assets/icon-192.png" alt="أيقونة {NAME}" width="40" height="40"><span>{NAME}<small>Cute Ghost</small></span></a>
<nav aria-label="القائمة الرئيسية">{nav}</nav></div></header>
<main id="main">
{body}
</main>
<footer><div class="wrap">
<div class="fcols"><div><strong>{NAME} - Cute Ghost</strong><p>لعبة مرحة وآمنة للأطفال حتى 5 سنوات، بلا حسابات وبلا جمع بيانات.</p></div>
<div><strong>روابط</strong><p><a href="privacy.html">سياسة الخصوصية</a><br><a href="delete-data.html">حذف البيانات</a><br><a href="parents.html">دليل الأهل</a></p></div>
<div><strong>تواصل</strong><p><a href="mailto:{EMAIL}">{EMAIL}</a></p></div></div>
<p class="copy">© 2026 {NAME} - Cute Ghost. جميع الحقوق محفوظة. Google Play علامة تجارية لشركة Google LLC.</p>
</div></footer>
</body></html>'''
    open(os.path.join(ROOT, fn), "w", encoding="utf-8").write(s)

def cta():
    if PLAY_URL:
        return f'<a class="btn" href="{PLAY_URL}" rel="noopener">حمّلها من Google Play</a>'
    return '<span class="btn soon">قريبًا على Google Play</span>'

feat = [("🍼","اعتنِ بالشبح","أطعمه واسقِه ونظّفه وضعه في السرير، ويشكرك بحركات لطيفة."),
        ("🥚","بيض وأشباح صغار","تفقس الأشباح الصغيرة من البيض، وتكبر ثم تنتقل إلى بيتها في القرية."),
        ("🏠","بيوت وغرف تزيّنها","ستة بيوت بتصاميم مختلفة، وأثاث وألوان وستائر وزينة سحرية."),
        ("🎩","خزانة الأزياء","قبعات وأوشحة وأجنحة وتوهج ملوّن تفتحها بالنجوم."),
        ("🎈","ألعاب قصيرة","أرجوحة وزحليقة ودوامة نجوم ومنطاد، بلا خسارة وبلا ضغط."),
        ("🌙","وضع لطيف للصغار","لا مرض ولا خسارة ولا يختفي الشبح، فقط دمعة صغيرة تنتظر الاهتمام.")]
cards = "".join(f'<article class="card"><span class="ic" aria-hidden="true">{i}</span><h3>{t}</h3><p>{d}</p></article>' for i, t, d in feat)

home_ld = '''<script type="application/ld+json">{"@context":"https://schema.org","@graph":[
{"@type":"WebSite","@id":"%(b)s#site","url":"%(b)s","name":"الشبح اللطيف - Cute Ghost","inLanguage":"ar"},
{"@type":"MobileApplication","name":"الشبح اللطيف - Cute Ghost","alternateName":"Cute Ghost","applicationCategory":"GameApplication","operatingSystem":"ANDROID","inLanguage":"ar","url":"%(b)s","image":"%(b)sassets/icon-512.png","description":"لعبة مرحة وآمنة للأطفال حتى 5 سنوات: شبح لطيف يأكل وينام ويلعب ويكبر. بلا حسابات وبلا جمع بيانات.","audience":{"@type":"PeopleAudience","suggestedMaxAge":5},"offers":{"@type":"Offer","price":"0","priceCurrency":"USD"},"installUrl":"https://play.google.com/store/apps/details?id=%(p)s"}]}</script>''' % {"b": BASE, "p": PKG}

page("index.html", f"{NAME} - Cute Ghost | لعبة أطفال مرحة وآمنة للصغار حتى 5 سنوات",
 "الشبح اللطيف: لعبة أندرويد للأطفال حتى 5 سنوات. شبح صغير يأكل وينام ويلعب ويكبر، بلا حسابات وبلا جمع بيانات، مع وضع للأهل.",
 f'''<section class="hero"><div class="wrap two">
<div><h1>{NAME}<small>Cute Ghost</small></h1>
<p class="lead">رفيق مرح يعيش على شاشة طفلك: يأكل وينام ويلعب ويكبر. لعبة هادئة وآمنة للصغار حتى 5 سنوات.</p>
<p>{cta()} <a class="btn ghost" href="parents.html">دليل الأهل</a></p>
<ul class="pills"><li>بلا حسابات</li><li>بلا جمع بيانات</li><li>وضع لطيف للصغار</li><li>بوابة للأهل</li></ul></div>
<img class="shot" src="assets/og-image.png" alt="الأشباح اللطيفة بين الغيوم والنجوم" width="600" height="315"></div></section>
<section class="wrap"><h2>ماذا في اللعبة؟</h2><div class="grid">{cards}</div></section>
<section class="band"><div class="wrap"><h2>مصمَّمة براحة الأهل</h2>
<p>لا يطلب التطبيق حسابًا ولا يستخدم الكاميرا أو الميكروفون أو الموقع. يُحفظ تقدّم الطفل على الجهاز فقط. أي إعلان اختياري لا يُعرض إلا إذا اختار المستخدم مشاهدته، وهو مضبوط للأطفال.</p>
<p><a href="parents.html">اقرأ دليل الأهل</a> · <a href="privacy.html">سياسة الخصوصية</a></p></div></section>''', home_ld)

page("features.html", "عن اللعبة", "تعرّف على لعبة الشبح اللطيف: رعاية الشبح، البيض والأشباح الصغار، البيوت والأثاث، خزانة الأزياء، والألعاب القصيرة للصغار.",
 f'''<section class="wrap prose"><h1>عن لعبة {NAME}</h1>
<p class="lead">الشبح اللطيف لعبة رفيق للأطفال الصغار (حتى 5 سنوات). يعيش الشبح على شاشة الهاتف، ويحتاج طفلك إلى الاعتناء به بلطف.</p></section>
<section class="wrap"><div class="grid">{cards}</div></section>
<section class="wrap prose"><h2>كيف تعمل؟</h2>
<ul><li>يوافق أحد الأهل على إذن «الظهور فوق التطبيقات الأخرى» لتظهر الأشباح العائمة على الشاشة.</li>
<li>يلمس الطفل الشبح ليأكل أو يشرب أو يستحم أو ينام عندما يحتاج لذلك.</li>
<li>يكسب الطفل نجومًا من الرعاية والألعاب، ويستخدمها في تزيين البيت وفتح الأزياء.</li>
<li>تنتقل الأشباح الكبيرة إلى القرية، ويحلّ محلها أشباح جديدة.</li></ul>
<h2>لمن هي؟</h2><p>للأطفال من عمر 5 سنوات فما دون، بإشراف الأهل. اللغة العربية بسيطة وواضحة.</p></section>''')

page("parents.html", "دليل الأهل", "دليل الأهل للعبة الشبح اللطيف: الأمان، بوابة الأهل، وقت اللعب، الخصوصية والإعلانات المناسبة للأطفال.",
 '''<section class="wrap prose"><h1>دليل الأهل</h1>
<h2>الأمان والخصوصية</h2><ul><li>لا حسابات ولا بريد ولا أسماء حقيقية.</li><li>لا كاميرا ولا ميكروفون ولا موقع ولا جهات اتصال.</li><li>يُحفظ التقدّم على الجهاز فقط، ويُحذف بحذف التطبيق.</li></ul>
<h2>بوابة الأهل</h2><p>الإعدادات خلف زر «للأهل» وسؤال حسابي لا يستطيع الصغير حلّه.</p>
<h2>وقت اللعب</h2><p>يمكنكم تحديد مدة لعب (حتى 3 ساعات) أو جدول يومي، وإنهاؤه في أي وقت من لوحة الأهل.</p>
<h2>الوضع اللطيف</h2><p>مفعّل افتراضيًا للصغار: لا يمرض الشبح ولا يختفي، فقط يبكي بلطف حتى يُعتنى به.</p>
<h2>الإعلانات</h2><p>قد يُعرض إعلان مكافئ اختياري عبر Google AdMob عند اختيار المشاهدة فقط، وبانر واحد داخل لوحة الأهل فقط. الإعلانات مضبوطة للأطفال (محتوى G، بلا إعلانات مخصّصة، وبلا معرّف إعلانات).</p>
<h2>الأذونات</h2><ul><li><strong>الظهور فوق التطبيقات:</strong> لعرض الأشباح العائمة، وهي ميزة اللعبة الأساسية.</li><li><strong>الإشعار والخدمة:</strong> لإبقاء الأشباح ظاهرة وتشغيل وقت اللعب.</li><li><strong>الإنترنت:</strong> للإعلان الاختياري فقط.</li></ul>
<p>للأسئلة: <a href="contact.html">اتصلوا بنا</a>.</p></section>''')

priv_ar = PRIV.split("\n---")[0].replace("[ضع بريدك الإلكتروني هنا]", EMAIL)
page("privacy.html", "سياسة الخصوصية", "سياسة خصوصية لعبة الشبح اللطيف: لا نجمع بيانات شخصية، ويُحفظ التقدّم على الجهاز، وإعلانات مضبوطة للأطفال.",
 '<section class="wrap prose"><h1>سياسة الخصوصية</h1>' + md(priv_ar) + '<p>لحذف البيانات: <a href="delete-data.html">صفحة حذف البيانات</a>.</p></section>')

page("delete-data.html", "حذف البيانات", "كيفية حذف بيانات لعبة الشبح اللطيف: البيانات محفوظة على جهازك فقط، ويمكنك حذفها بمسح بيانات التطبيق أو إلغاء تثبيته.",
 f'''<section class="wrap prose"><h1>حذف البيانات</h1>
<p>لا يملك {NAME} خوادم ولا حسابات، فلا توجد بيانات عنك أو عن طفلك لدينا. كل ما يحفظه التطبيق (النجوم، الأثاث، أسماء الأشباح، الإعدادات) موجود على جهازك فقط.</p>
<h2>كيف تحذف بيانات التطبيق؟</h2>
<ol><li>على الهاتف: الإعدادات ← التطبيقات ← الشبح اللطيف ← التخزين ← «مسح البيانات». يعيد هذا اللعبة كما كانت أول مرة.</li>
<li>أو احذف التطبيق نهائيًا (إلغاء التثبيت)، فتُحذف بياناته كلها.</li></ol>
<h2>بيانات الإعلانات</h2><p>إن عُرض إعلان مكافئ، فقد تعالج Google بيانات تقنية لتقديمه. يمكنكم إدارة ذلك من إعدادات حساب جوجل: <a href="https://myadcenter.google.com" rel="noopener">myadcenter.google.com</a>.</p>
<h2>طلب خاص؟</h2><p>إن كانت لديكم أي طلب يخص الخصوصية أو الحذف، راسلونا على <a href="mailto:{EMAIL}">{EMAIL}</a> وسنرد في أقرب وقت.</p></section>''')

page("contact.html", "اتصل بنا", "تواصل مع فريق الشبح اللطيف للدعم أو الاقتراحات أو طلبات الخصوصية عبر البريد الإلكتروني.",
 f'''<section class="wrap prose"><h1>اتصل بنا</h1>
<p>يسعدنا سماع رأيكم أو مساعدتكم.</p>
<p class="mail"><a class="btn" href="mailto:{EMAIL}?subject=الشبح اللطيف">{EMAIL}</a></p>
<h2>عند مراسلتنا اذكروا</h2><ul><li>نوع الهاتف وإصدار أندرويد.</li><li>وصفًا قصيرًا للمشكلة أو الاقتراح.</li></ul>
<p>معرّف التطبيق على Google Play: <code>{PKG}</code></p></section>''')

page("404.html", "الصفحة غير موجودة", "الصفحة المطلوبة غير موجودة. عد إلى الصفحة الرئيسية للعبة الشبح اللطيف.",
 '<section class="wrap prose"><h1>الصفحة غير موجودة</h1><p><a class="btn" href="index.html">العودة للرئيسية</a></p></section>')

# SEO files
urls = [("", "1.0")] + [(f, "0.8" if f in ("features.html", "parents.html") else "0.6") for f, _ in NAV[1:]]
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(
    f"<url><loc>{BASE}{u}</loc><lastmod>{DATE}</lastmod><priority>{p}</priority></url>\n" for u, p in urls) + "</urlset>\n"
open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8").write(sm)
open(os.path.join(ROOT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {BASE}sitemap.xml\n")
open(os.path.join(ROOT, "site.webmanifest"), "w", encoding="utf-8").write(
 '{"name":"الشبح اللطيف - Cute Ghost","short_name":"الشبح اللطيف","lang":"ar","dir":"rtl","start_url":"./","display":"browser","theme_color":"#7C5CFF","background_color":"#F5F3FF","icons":[{"src":"assets/icon-192.png","sizes":"192x192","type":"image/png"},{"src":"assets/icon-512.png","sizes":"512x512","type":"image/png"}]}')
print("built", len(urls) + 1, "pages")
