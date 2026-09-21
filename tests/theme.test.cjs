'use strict';
const test = require('node:test');
const assert = require('node:assert/strict');
const vm = require('node:vm');
const fs = require('node:fs');
const path = require('node:path');
const source = fs.readFileSync(path.join(__dirname, '..', 'script.js'), 'utf8');
function run({light=false, saved=null, storageBlocked=false, hasButton=true}={}) {
  const root={dataset:{}};
  const handlers={}; const attributes={}; const writes=[]; let preferenceChange;
  const button={hidden:true,setAttribute:(k,v)=>{attributes[k]=v;},addEventListener:(k,v)=>{handlers[k]=v;}};
  const document={documentElement:root,querySelector:(s)=>s==='.theme-toggle' && hasButton ? button : null,getElementById:()=>null};
  const localStorage={getItem:()=>{if(storageBlocked)throw Error('blocked');return saved;},setItem:(k,v)=>{if(storageBlocked)throw Error('blocked');writes.push([k,v]);}};
  const window={matchMedia:()=>({matches:light,addEventListener:(k,f)=>{preferenceChange=f;}})};
  vm.runInNewContext(source,{document,localStorage,window});
  return {root,button,attributes,writes,click:()=>handlers.click(),change:(matches)=>preferenceChange({matches})};
}
test('system dark default',()=>assert.equal(run().root.dataset.theme,'dark'));
test('system light default',()=>assert.equal(run({light:true}).root.dataset.theme,'light'));
test('saved preference wins',()=>assert.equal(run({light:true,saved:'dark'}).root.dataset.theme,'dark'));
test('invalid stored theme is ignored',()=>assert.equal(run({light:true,saved:'broken'}).root.dataset.theme,'light'));
test('storage blocked does not break toggle',()=>{const r=run({storageBlocked:true});r.click();assert.equal(r.root.dataset.theme,'light');assert.equal(r.attributes['aria-label'],'어두운 테마로 전환');});
test('toggle stores selection',()=>{const r=run();r.click();assert.deepEqual(r.writes,[['portfolio-theme','light']]);assert.equal(r.attributes['aria-pressed'],'true');});
test('unselected preference follows system',()=>{const r=run();r.change(true);assert.equal(r.root.dataset.theme,'light');});
test('user selection is not overwritten by system',()=>{const r=run();r.click();r.change(false);assert.equal(r.root.dataset.theme,'light');});
test('no button remains safe',()=>assert.equal(run({hasButton:false}).root.dataset.theme,'dark'));
test('theme button is enabled only after script setup',()=>assert.equal(run().button.hidden,false));
