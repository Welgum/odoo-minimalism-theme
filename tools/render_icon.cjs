// SPDX-License-Identifier: LGPL-3.0-or-later
// Original vector monogram, rasterized locally; no remote fonts or images.
const {chromium}=require('playwright');
const path=require('node:path');
(async()=>{
 const browser=await chromium.launch({headless:true,...(process.env.MIN_CHROME_PATH?{executablePath:process.env.MIN_CHROME_PATH}:{})});
 try {
  const page=await browser.newPage({viewport:{width:256,height:256},deviceScaleFactor:1});
  await page.setContent(`<style>body{margin:0;background:#18181b;display:grid;place-items:center;height:100vh}svg{width:164px;height:164px}</style><svg viewBox="0 0 164 164" xmlns="http://www.w3.org/2000/svg"><path d="M32 118V46l50 43 50-43v72" fill="none" stroke="#fafafa" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/><circle cx="132" cy="126" r="6" fill="#60a5fa"/></svg>`);
  await page.screenshot({path:path.resolve(__dirname,'../minimalism_theme/static/description/icon.png')});
 } finally {await browser.close();}
})().catch(e=>{console.error(e);process.exit(1)});
