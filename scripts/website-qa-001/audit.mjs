import { chromium } from 'playwright';
import { mkdir, writeFile } from 'node:fs/promises';

const BASE = 'https://www.shalomlamalka.com';
const paths = [
  ['tops', '/טופים-וגופיות'],
  ['collection', '/shop-2'],
  ['dresses', '/blank-1'],
  ['men-shirts', '/copy-of-טבעות-1'],
];
const devices = [
  { name: 'desktop', width: 1440, height: 900 },
  { name: 'mobile', width: 375, height: 812 },
];
const output = 'website-qa-output';
await mkdir(output, { recursive: true });
const browser = await chromium.launch({ headless: true });
const results = [];
try {
  for (const [key, pathname] of paths) {
    for (const device of devices) {
      const context = await browser.newContext({
        viewport: { width: device.width, height: device.height },
        locale: 'he-IL',
        timezoneId: 'Asia/Jerusalem',
        isMobile: device.name === 'mobile',
        hasTouch: device.name === 'mobile',
      });
      const page = await context.newPage();
      const entry = {
        key, pathname, viewport: device.name,
        requestedUrl: new URL(pathname, BASE).href,
        status: 'UNKNOWN', httpStatus: null, finalUrl: null,
        error: null, title: null, bodyDir: null, htmlLang: null,
        horizontalOverflowPx: null, visibleLinks: null,
        screenshot: null,
      };
      try {
        const response = await page.goto(entry.requestedUrl, {
          waitUntil: 'domcontentloaded', timeout: 45000,
        });
        await page.waitForTimeout(2500);
        entry.httpStatus = response?.status() ?? null;
        entry.finalUrl = page.url();
        entry.title = await page.title();
        const dom = await page.evaluate(() => {
          const dir = (element) => element?.getAttribute('dir') || getComputedStyle(element).direction || null;
          return {
            htmlLang: document.documentElement.lang || null,
            bodyDir: dir(document.body),
            horizontalOverflowPx: Math.max(0, document.documentElement.scrollWidth - innerWidth),
            visibleLinks: [...document.querySelectorAll('a[href]')].filter(a => a.getClientRects().length).length,
          };
        });
        Object.assign(entry, dom);
        entry.status = entry.httpStatus && entry.httpStatus >= 400 ? 'HTTP_ERROR' : 'RENDERED';
        entry.screenshot = key + '-' + device.name + '.png';
        await page.screenshot({ path: output + '/' + entry.screenshot, fullPage: true, timeout: 20000 });
      } catch (error) {
        entry.status = 'UNKNOWN';
        entry.error = String(error?.message ?? error).slice(0, 1000);
      } finally {
        results.push(entry);
        await context.close();
      }
    }
  }
} finally {
  await browser.close();
}
const report = {
  id: 'WEBSITE-QA-001',
  scope: 'PUBLIC_SITE_READ_ONLY',
  testedAt: new Date().toISOString(),
  note: 'Failures to navigate, DNS errors and timeouts are UNKNOWN, not proof of a broken live website. Screenshot and dir checks are indicators, not full RTL or accessibility certification.',
  results,
};
await writeFile(output + '/report.json', JSON.stringify(report, null, 2) + '\n');
const rows = results.map(r => '| ' + [r.key, r.viewport, r.status, r.httpStatus ?? '—', r.horizontalOverflowPx ?? '—', r.bodyDir ?? '—', r.error ? r.error.replace(/[|\n]/g,' ').slice(0,90) : '—'].join(' | ') + ' |');
await writeFile(output + '/summary.md', [
  '# WEBSITE-QA-001 — Public Wix Site Audit', '',
  '**Read-only / Synthetic QA / No cart, checkout, Wix API or edits.**', '',
  '| Page | Viewport | Result | HTTP | Overflow (px) | Direction | Error |',
  '|---|---|---|---|---|---|---|', ...rows, '',
  'UNKNOWN means not verified; it must not be interpreted as a live site failure.',
  'Visual RTL, mobile menu and accessibility require screenshot review and follow-up tests.',
  ''
].join('\n'));
console.log('WEBSITE-QA-001:', results.length, 'checks; report saved in', output);
