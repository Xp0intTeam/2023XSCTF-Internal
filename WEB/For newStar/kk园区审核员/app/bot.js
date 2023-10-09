const puppeteer = require('puppeteer')

const CONFIG = {
    FLAG: process.env['FLAG'] || "XSCTF{Y0u_succ3s5ful1y_x55_m3}"
}

exports.visit = async function () {
    try {
        const browser_options = {
          args: [
            '--disable-background-networking',
            '--disable-default-apps',
            '--no-sandbox',
            '--disable-extensions',
            '--disable-gpu',
            '--disable-sync',
            '--disable-translate',
            '--hide-scrollbars',
            '--metrics-recording-only',
            '--mute-audio',
            '--no-first-run',
            '--safebrowsing-disable-auto-update'
          ],
          pipe: true,
          headless: true
        };
        const delay = ms => new Promise(resolve => setTimeout(resolve, ms))
        const browser = await puppeteer.launch(browser_options);
        const page = await browser.newPage();
        await page.setCookie({
            name: "flag",
            url: 'http://127.0.0.1/view',
            value: CONFIG.FLAG
        });
        await page.goto('http://127.0.0.1/view');
        await delay(1000)
        await browser.close();
      } catch (e) {
        console.log(e.message);
      }
}
