const puppeteer = require('puppeteer');
(async () => {
  const b = await puppeteer.launch({headless: 'new'});
  const p = await b.newPage();
  await p.setUserAgent('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36');
  const r = await p.goto(process.argv[2], {waitUntil: 'networkidle2', timeout: 60000});
  console.log('status', r.status(), await p.title());
  const links = await p.$$eval('a', as => as.map(a => [a.innerText.trim().slice(0,40), a.href]).filter(x => /download|unduh|pdf/i.test(x[0]+x[1])));
  console.log(JSON.stringify(links.slice(0,15), null, 0));
  await b.close();
})().catch(e => { console.error('ERR', e.message); process.exit(1); });
