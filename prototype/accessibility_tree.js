const p=require('puppeteer-core');
(async()=>{
 const b=await p.launch({executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',headless:true});
 const pg=await b.newPage(); await pg.goto('file://'+process.argv[2],{waitUntil:'load'});
 const s=await pg.accessibility.snapshot({interestingOnly:false});
 const out=[];
 (function w(n,d){ if(!n)return; const keep=!['generic','none','InlineTextBox','LineBreak'].includes(n.role);
   if(keep){let t=n.role;if(n.level)t+=' '+n.level;if(n.name)t+=': '+n.name;out.push('  '.repeat(d)+t);}
   (n.children||[]).forEach(c=>w(c,keep?d+1:d));})(s,0);
 console.log(out.join('\n')); await b.close();})().catch(e=>{console.error('ERR',e.message);process.exit(1)});
