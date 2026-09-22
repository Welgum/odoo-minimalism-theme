// SPDX-License-Identifier: LGPL-3.0-or-later
const {chromium}=require('playwright');
const assert=require('node:assert/strict');
const path=require('node:path');
const {pathToFileURL}=require('node:url');
(async()=>{
 const browser=await chromium.launch({headless:true,...(process.env.MIN_CHROME_PATH?{executablePath:process.env.MIN_CHROME_PATH}:{})});
 try {
  const page=await browser.newPage();
  const errors=[];page.on('pageerror',e=>errors.push(e.message));
  for(const width of [1440,390]){
   await page.setViewportSize({width,height:960});
   for(const name of ['listing','thumbnail']){
    await page.goto(pathToFileURL(path.resolve(__dirname,`../dist/${name}-preview.html`)).href);
    await page.evaluate(()=>Promise.all([...document.images].map(img=>img.decode())));
    assert.ok(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),`${name}/${width}: horizontal overflow`);
    await page.screenshot({path:path.resolve(__dirname,`../dist/${name}-${width}.png`),fullPage:true});
   }
  }
  assert.deepEqual(errors,[]);
  console.log('PASS: listing and portrait thumbnail at 1440px and 390px; all images decoded; no overflow or script errors');
 }finally{await browser.close();}
})().catch(e=>{console.error(e);process.exit(1)});
