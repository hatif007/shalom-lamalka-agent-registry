<!-- REPORT_ARCHIVE_V1
{"schema_version":"1.0","report_id":"WEBSITE-UX-AUDIT-2026-10-16","role":"website","run_date":"2026-10-16","run_mode":"INSTALLED_AGENT_VERIFIED","payload_type":"FULL_GENERATED_REPORT","task_reference":"WEBSITE-DIRECTOR-V2 — First Professional UX Audit","source_conversation_url":null,"source_evidence":["https://github.com/hatif007/shalom-lamalka-agent-registry/actions/runs/38864670149","https://github.com/hatif007/shalom-lamalka-agent-registry/blob/main/operations/management-system/reports/README.md"],"scope":"READ_ONLY","owner_approval":"Explicit user authorization to archive this Website Improvement Report"}
REPORT_ARCHIVE_V1 -->
# דוח שיפור אתר — ביקורת UX מקצועית ראשונה

**Report ID:** `WEBSITE-UX-AUDIT-2026-10-16`  
**תפקיד:** Website Director V2  
**מצב ריצה:** קריאה בלבד; ללא הרצת Playwright מחדש  
**אתר:** https://www.shalomlamalka.com/  
**זמן יצירת הראיות:** 2026-10-16T07:03:26.622Z  
**זמן הבדיקה:** 2026-10-16T11:37:29Z  
**מקור:** GitHub Actions run `38864670149`, artifact `website-qa-001-evidence`  
**כיסוי:** `report.json`, `summary.md` ושמונה צילומי desktop/mobile

## תקציר מנהלים

הראיות מצביעות בביטחון גבוה על overflow אופקי אחיד של 161px בכל ארבעת צילומי הדסקטופ ועל שכבת הסכמה המכסה תוכן בכל הדפים. רווחים אנכיים ארוכים נראים בבירור בעיקר בדפי tops ו-collection ובמידה שונה ב-men-shirts, אך מהראיות הקיימות לא ניתן לקבוע אם מקורם בגובה מקטע שגוי, lazy loading או מצב אנימציה בזמן הצילום. `bodyDir=ltr` הוא FACT טכני, אך לא נמצאה בצילומים הוכחה מספקת לשיבוש חזותי גורף של עברית; נדרשת בדיקה ברמת רכיב וסדר מקלדת.

העדיפויות להלן הן עדיפויות איכות אתר על בסיס רוחב ההשפעה וחומרת החיכוך החזותי. תעדוף עסקי או החלטת CRO שייכים ל-Growth Manager.

## ממצא 1 — overflow אופקי גלובלי בדסקטופ

**עמודים ותצוגה:** desktop בכל ארבעת הדפים:

- `/טופים-וגופיות` — `tops-desktop.png`
- `/shop-2` — `collection-desktop.png`
- `/blank-1` — `dresses-desktop.png`
- `/copy-of-טבעות-1` — `men-shirts-desktop.png`

**FACT — תצפית מאומתת:** `report.json` מדווח `horizontalOverflowPx: 161` בכל ארבע התוצאות. צילומי המסך ברוחב 1601px מציגים את אזור האתר עד x=1440 ואת 161 הפיקסלים הנוספים כרצועה לבנה מימין. בתוצאות mobile נמדד 0px.

**HYPOTHESIS — סיבת שורש:** רכיב גלובלי, section, transform או רוחב קבוע חורג מ-`window.innerWidth`. לא ניתן לזהות מהצילום לבדו איזה element אחראי.

**השפעת UX:** קיים סיכון לגלילה אופקית, מרכוז שגוי ותחושה של עמוד שבור. עצם החריגה מאומתת; התדירות שבה משתמשים גוללים הצידה וההשפעה העסקית אינן ידועות.

**ביטחון:** גבוה לגבי החריגה; נמוך לגבי סיבת השורש.

**תיקון מומלץ:** לאתר את האלמנט החורג באמצעות השוואת `getBoundingClientRect().right` ל-`innerWidth`; לתקן width/min-width, margin, transform או positioning ברכיב המקור. אין להסתפק ב-`overflow-x:hidden` לפני שהגורם זוהה, כדי לא להסתיר תוכן או focus outline.

**עדיפות:** `HIGH`

**האם נדרשת בדיקת דפדפן חדשה:** כן. בדיקת אבחון desktop ממוקדת חיונית לזיהוי האלמנט, ולאחר תיקון יש לאמת `scrollWidth === clientWidth` בכל ארבעת הנתיבים ובכמה רוחבי desktop.

## ממצא 2 — מקטעים אנכיים ריקים או דהויים

**עמודים ותצוגה:**

- `/טופים-וגופיות` — desktop ו-mobile
- `/shop-2` — desktop ו-mobile
- `/copy-of-טבעות-1` — desktop ו-mobile
- `/blank-1` — mobile מציג אזור תחתון דהוי, אך אינו מציג אותו רווח קיצוני כמו tops/collection

**FACT — תצפית מאומתת:** בצילומי tops ו-collection קיים מרווח בהיר ארוך מאוד בין שורת המוצרים האחרונה שנראית לבין ה-footer, בשתי התצוגות. ב-men-shirts מופיעים תחילה כרטיסים תקינים ובהמשך פריטים דהויים ואז שטח ארוך עד ה-footer. dresses צפוף יותר ולכן הבעיה אינה אחידה בכל הדפים.

**HYPOTHESIS — סיבת שורש:** section עם min-height/גובה קשיח, gallery שאינה מכווצת את המכל לאחר סיום הפריטים, או lazy loading/אנימציית כניסה שלא הושלמו בזמן צילום full-page.

**UNKNOWN:** לא ידוע אם השטח נשאר לאחר המתנה נוספת, גלילה הדרגתית, אינטראקציה או טעינת תמונות מלאה. לכן לא מאומת שזהו פגם חי קבוע.

**השפעת UX:** אם המצב קבוע, המשתמש נדרש לגלילה ארוכה ונראה כאילו הקטלוג הסתיים או נשבר לפני ה-footer. ההשפעה החזותית נצפתה; נטישה או פגיעה במכירות לא נבדקו.

**ביטחון:** גבוה בתצפית; בינוני בכך שמדובר בפגם layout קבוע.

**תיקון מומלץ:** לבדוק את גובה ה-section/gallery ואת מצב טעינת ה-repeater; להשתמש בגובה תוכן אוטומטי, להסיר spacers/min-height שאינם נדרשים, ולוודא שה-footer עוקב מיד אחרי הפריט האחרון. אם זו lazy loading, להבטיח טעינה יציבה בעת scroll ולספק skeleton ברור שאינו משאיר עמוד ריק.

**עדיפות:** `HIGH`

**האם נדרשת בדיקת דפדפן חדשה:** כן, והיא חיונית לפני שינוי. יש לצלם לאחר `networkidle`, לאחר גלילה מדורגת לתחתית ולאחר המתנה קצרה, ולמדוד את המרחק בין תחתית הגריד ל-footer.

## ממצא 3 — banner הסכמה מכסה תוכן

**עמודים ותצוגה:** כל ארבעת הדפים, desktop ו-mobile.

**FACT — תצפית מאומתת:** banner לבן קבוע חוצה את אזור המוצרים בצילומי desktop. ב-mobile הוא נפרס למבנה גבוה יותר עם טקסט ושתי פעולות, ומכסה חלקים מכרטיסי מוצרים בזמן הצילום.

**HYPOTHESIS:** שכבה קבועה ללא שמירת מרווח תחתון מספק בתוכן. לא נבדקו התנהגות לאחר בחירה, persistence, focus trap או קורא מסך.

**השפעת UX:** תוכן, שמות מוצרים או פעולות מוסתרים עד לבחירה. הכיסוי החזותי מאומת; מידת הפגיעה בהשלמת משימה אינה ידועה.

**ביטחון:** גבוה בכיסוי החזותי; בינוני לגבי התנהגות אינטראקטיבית.

**תיקון מומלץ:** לצמצם גובה mobile, לשמור על טקסט משפטי קריא ועל הפעולות `אישור` ו-`הגדרות עוגייה`, ולהוסיף offset/padding כך שתוכן פעיל לא יישב מאחור. יש לשמור focus ברור, סדר מקלדת תקין וכפתור סגירה נגיש, בכפוף לדרישות ההסכמה.

**עדיפות:** `HIGH`

**האם נדרשת בדיקת דפדפן חדשה:** כן. לבדוק 360/390/430px ו-desktop, כיסוי CTA, ניווט מקלדת, פתיחת הגדרות, אישור ו-persistence לאחר reload.

## ממצא 4 — RTL: ערך computed לעומת תצוגה בפועל

**עמודים ותצוגה:** כל ארבעת הדפים, desktop ו-mobile.

**FACT — תצפית מאומתת:** `htmlLang=he` ו-`bodyDir=ltr` בכל שמונה הרשומות. טקסטי המוצרים בעברית נראים קריאים ובסדר אותיות תקין בצילומים, ורוב כרטיסי המוצרים ממורכזים. לא נראתה הוכחה מספקת להיפוך טקסט או לכשל RTL חזותי גורף.

**HYPOTHESIS:** ירושת `ltr` עלולה להשפיע על סדר flex/grid, יישור, אייקונים, breadcrumbs או סדר focus גם אם הטקסט עצמו נראה תקין.

**UNKNOWN:** סדר DOM מול סדר חזותי, ניווט מקלדת, התנהגות תפריט, רכיבי form ותמיכה בקורא מסך לא נבדקו.

**השפעת UX:** כרגע לא ניתן לטעון לפגם RTL חזותי מאומת. קיים סיכון לחוסר עקביות ברכיבים אינטראקטיביים ולסדר ניווט שאינו טבעי לקורא עברית.

**ביטחון:** גבוה לגבי הערכים הטכניים; נמוך לגבי פגם משתמש בפועל.

**תיקון מומלץ:** להגדיר `dir="rtl"` ברמת המסמך או מעטפת התוכן העברי רק לאחר בדיקת השפעה, ולשמור `ltr` נקודתי למספרים, כתובות דוא"ל ותוכן אנגלי כשנדרש. יש להתאים DOM order לסדר חזותי ולא להסתמך רק על `row-reverse`.

**עדיפות:** `MEDIUM`

**האם נדרשת בדיקת דפדפן חדשה:** כן. נדרשת בדיקת computed direction ברמת רכיב, tab order, menu, sort/filter ו-focus; אין הצדקה לשינוי גורף על סמך `bodyDir` בלבד.

## ממצא 5 — היררכיית mobile וגרידי מוצרים

**עמודים ותצוגה:** mobile בכל ארבעת הדפים; בולט במיוחד ב-`/blank-1` וב-`/copy-of-טבעות-1`.

**FACT — תצפית מאומתת:** הגריד מוצג בשתי עמודות עם תמונות דומיננטיות, בעוד שם, מחיר וכפתור נדחסים לשטח צר. ה-header שומר על שורת ניווט מלאה עם מספר קישורים ואייקונים במקום מעבר חזותי ברור לניווט mobile קומפקטי. ה-banner מוסיף שכבת הפרעה מעל הגריד.

**HYPOTHESIS:** צפיפות הכותרת וכרטיסי שתי העמודות עשויה להקטין קריאות ויעדי מגע. גודל font ויעדי מגע לא נמדדו ולכן אינם פגם נגישות מאומת.

**השפעת UX:** היררכיית `תמונה → שם → מחיר → פעולה` קיימת, אך פרטי ההחלטה והניווט המשני מקבלים משקל חזותי נמוך. ההשלכה על רכישה או conversion אינה בתחום בדיקה זו ולא נבדקה.

**ביטחון:** בינוני-גבוה לגבי ההיררכיה החזותית; נמוך לגבי מידות CSS מדויקות.

**תיקון מומלץ:** לעבור ל-header mobile קומפקטי עם menu נגיש; לשמר שתי עמודות רק כאשר כל כרטיס עומד ברוחב מינימלי, טקסט קריא ויעד מגע של לפחות 44×44 CSS px. אחרת לעבור לעמודה אחת. לחזק הבדל בין שם, מחיר ו-CTA ולשמור גובה עקבי לכרטיסים.

**עדיפות:** `HIGH`

**האם נדרשת בדיקת דפדפן חדשה:** כן. יש למדוד CSS pixels, touch targets, wrapping ויציבות layout ברוחבי 360/390/430px לפני החלטה בין עמודה אחת לשתיים.

## שלוש הפעולות בעלות הערך הגבוה ביותר

1. **לתקן את חריגת הרוחב הגלובלית בדסקטופ.** היא מופיעה בכל ארבעת הדפים ומרמזת על רכיב משותף; אבחון אחד עשוי לפתור פגם רוחבי במספר תבניות.
2. **לאמת ולתקן את גובה אזור הקטלוג והטעינה הדינמית.** לבצע retest קצר וממוקד שמבדיל בין layout קבוע לבין lazy loading, ואז לכווץ את המקטע או לייצב את הטעינה. זו הפעולה החשובה ביותר לפני עריכת תוכן או עיצוב.
3. **להפחית חסימת תוכן במובייל.** לתקן תחילה את גובה/מיקום banner ההסכמה, ואז לאמת header קומפקטי וקריאות כרטיסי המוצרים ברוחבי mobile נפוצים.

## Backlog תפעולי

| מזהה | סטטוס | עדיפות | Evidence | Owner | תלות | פעולה הבאה |
|---|---|---|---|---|---|---|
| WEB-UX-01 | PROPOSED | HIGH | report.json + 4 desktop screenshots | WEBSITE_ACTION | אישור בעלים לשינוי | targeted overflow diagnosis |
| WEB-UX-02 | EVIDENCE_REQUIRED | HIGH | tops/collection/men screenshots | WEBSITE_ACTION | browser retest ממוקד | distinguish fixed height from lazy state |
| WEB-UX-03 | PROPOSED | HIGH | 8 screenshots | WEBSITE_ACTION | דרישות consent + אישור בעלים | responsive banner specification |
| WEB-UX-04 | EVIDENCE_REQUIRED | MEDIUM | bodyDir/htmlLang + screenshots | WEBSITE_ACTION | keyboard/component QA | component-level RTL audit |
| WEB-UX-05 | PROPOSED | HIGH | 4 mobile screenshots | WEBSITE_ACTION | Growth business prioritization | mobile header/card spec |

## קבלה, אישורים וגבולות

- אין המלצה לפתוח מחדש את `GROW-SEO-01`; הסטטוס נשאר `HOLD`.
- SEO strategy, conversion analytics ו-CRO experiment decisions לא בוצעו.
- לפני כל תיקון חי נדרש `OWNER_APPROVAL` מדויק, הרשאות מתאימות, מצב recoverable, קריטריוני קבלה ו-rollback.
- `MANUAL_APPROVAL_REQUIRED: YES` לכל יישום עתידי; לא נדרש אישור נוסף ליצירת דוח זה שאושרה במפורש.

## Side-effect audit

Wix reads=0 בריצה זו (נעשה שימוש בארטיפקט קיים); Wix writes=0; published changes=0; content/blog publications=0; product/price/inventory changes=0; orders/checkout actions=0; analytics/funnel analysis=0; Slack messages=0; scheduled tasks=0; Playwright reruns=0; GitHub writes=1 (קובץ דוח זה בלבד); PR/merge/delete/branch creation=0.
