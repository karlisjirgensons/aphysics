# -*- coding: utf-8 -*-
"""Word faila (.docx) rakstītājs pārlūkprogrammā - JavaScript teksts.

Šis modulis neko nezina ne par testiem, ne par fiziku: tas dod lapai vienu
rīku, kas no vienkārša rindkopu un tabulu saraksta uzbūvē īstu .docx failu
tieši pārlūkā, bez servera un bez svešām bibliotēkām (vietne ir statiska).

.docx ir ZIP arhīvs ar XML failiem, tāpēc te ir divas daļas (SRP):
    zip()   - saspiešanas nav, ieraksti glabājas "stored" veidā, tāpēc
              pietiek ar CRC32 un galvenēm;
    build() - no blokiem uzbūvē word/document.xml un iesaiņo pilnu paketi.

Bloku valoda ir apzināti šaura - tikai tas, kas vajadzīgs darba lapai:
    {t:"p", text|parts, size, bold, italic, color, before, after, left, align}
    {t:"tbl", widths:[cm], plain:bool, rows:[{height, cells:[{text,...}]}]}
    {t:"pb"}                         - lappuses pārtraukums
Mērvienības: size punktos, before/after punktos, left un widths centimetros.

Noformējuma vērtības (fonts, krāsas, lapas izmērs) nāk no fd_stils.py, lai
Word fails un ekrāns izskatītos vienādi (DRY).
"""

JS = r"""
window.DOCX=(function(){
"use strict";

/* ------------------------------------------------------------ ZIP (stored) */
var CRC=(function(){var t=new Int32Array(256),c,i,k;
  for(i=0;i<256;i++){c=i;for(k=0;k<8;k++)c=(c&1)?(0xEDB88320^(c>>>1)):(c>>>1);
    t[i]=c;}
  return t;})();
function crc32(b){var c=-1,i;
  for(i=0;i<b.length;i++)c=CRC[(c^b[i])&255]^(c>>>8);
  return (c^-1)>>>0;}

var ENC=new TextEncoder();
function utf8(s){return ENC.encode(s);}
function dosTime(d){return (d.getHours()<<11)|(d.getMinutes()<<5)|
                           (d.getSeconds()>>1);}
function dosDate(d){return ((d.getFullYear()-1980)<<9)|((d.getMonth()+1)<<5)|
                           d.getDate();}

function zip(files){
  var now=new Date(),tm=dosTime(now),dt=dosDate(now);
  var chunks=[],dir=[],offset=0,i;
  for(i=0;i<files.length;i++){
    var name=utf8(files[i].name),data=files[i].data,sum=crc32(data);
    var lh=new DataView(new ArrayBuffer(30));
    lh.setUint32(0,0x04034b50,true);lh.setUint16(4,20,true);
    lh.setUint16(6,0x0800,true);lh.setUint16(8,0,true);
    lh.setUint16(10,tm,true);lh.setUint16(12,dt,true);
    lh.setUint32(14,sum,true);lh.setUint32(18,data.length,true);
    lh.setUint32(22,data.length,true);
    lh.setUint16(26,name.length,true);lh.setUint16(28,0,true);
    chunks.push(new Uint8Array(lh.buffer),name,data);
    var ch=new DataView(new ArrayBuffer(46));
    ch.setUint32(0,0x02014b50,true);ch.setUint16(4,20,true);
    ch.setUint16(6,20,true);ch.setUint16(8,0x0800,true);
    ch.setUint16(10,0,true);ch.setUint16(12,tm,true);ch.setUint16(14,dt,true);
    ch.setUint32(16,sum,true);ch.setUint32(20,data.length,true);
    ch.setUint32(24,data.length,true);
    ch.setUint16(28,name.length,true);
    ch.setUint32(42,offset,true);
    dir.push(new Uint8Array(ch.buffer),name);
    offset+=30+name.length+data.length;
  }
  var dirSize=0;
  for(i=0;i<dir.length;i++)dirSize+=dir[i].length;
  var end=new DataView(new ArrayBuffer(22));
  end.setUint32(0,0x06054b50,true);
  end.setUint16(8,files.length,true);end.setUint16(10,files.length,true);
  end.setUint32(12,dirSize,true);end.setUint32(16,offset,true);
  return new Blob(chunks.concat(dir,[new Uint8Array(end.buffer)]),
    {type:"application/vnd.openxmlformats-officedocument."+
          "wordprocessingml.document"});
}

/* ------------------------------------------------------------------- XML */
function esc(s){return String(s==null?"":s)
  .replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;");}
function tw(cm){return Math.round(cm*567);}          /* cm -> twips */
function pt(v){return Math.round(v*20);}             /* pt -> 1/20 pt */
function half(v){return Math.round(v*2);}            /* pt -> 1/2 pt */

var CFG=window.FD_STILS.docx;

function rPr(o){
  var x='<w:rFonts w:ascii="'+CFG.font+'" w:hAnsi="'+CFG.font+'"/>';
  if(o.bold)x+='<w:b/>';
  if(o.italic)x+='<w:i/>';
  x+='<w:color w:val="'+(o.color||"000000")+'"/>';
  x+='<w:sz w:val="'+half(o.size||CFG.size)+'"/>'+
     '<w:szCs w:val="'+half(o.size||CFG.size)+'"/>';
  /* Aizpildāmā vieta ir tukšums ar svītru apakšā, nevis punktu virkne -
     uz punktiem rakstīt nevar, uz tukšuma var. */
  if(o.underline)x+='<w:u w:val="'+o.underline+'"/>';
  if(o.sub)x+='<w:vertAlign w:val="subscript"/>';
  return '<w:rPr>'+x+'</w:rPr>';
}
function pPr(o){
  var x='<w:spacing w:before="'+pt(o.before||0)+'" w:after="'+
        pt(o.after==null?3:o.after)+'" w:line="240" w:lineRule="auto"/>';
  if(o.left)x+='<w:ind w:left="'+tw(o.left)+'"/>';
  if(o.align)x+='<w:jc w:val="'+o.align+'"/>';
  return '<w:pPr>'+x+'</w:pPr>';
}
/* Daļa un sakne Word failā ir Office formula (OMML), tāpēc skaitītājs
   paliek virs saucēja un vinkuls pāri visai izteiksmei arī tad, ja
   skolotājs failu pēc tam labo. Atomus sagatavo FD_MATH (sk. fd_math.py). */
function mrun(t,r){
  return '<m:r>'+r+'<m:t xml:space="preserve">'+esc(t)+'</m:t></m:r>';
}
function mtext(t,r){
  /* Teksts formulā ar indeksiem: "s(kopā)" -> īsts OMML apakšindekss.
     Bāze ir iepriekšējā teksta pēdējā zīme, tāpēc to pārceļ zem sSub. */
  var list=window.FD_MATH.indeksi(t),x="",i,g,baze,gaida=null;
  function izliet(){if(gaida){x+=mrun(gaida,r);}gaida=null;}
  for(i=0;i<list.length;i++){
    g=list[i];
    if(g.sub==null){izliet();gaida=g.text;continue;}
    baze="";
    if(gaida){
      baze=gaida.charAt(gaida.length-1);
      if(gaida.length>1)x+=mrun(gaida.slice(0,-1),r);
      gaida=null;
    }
    x+='<m:sSub><m:sSubPr><m:ctrlPr>'+r+'</m:ctrlPr></m:sSubPr><m:e>'+
       mrun(baze,r)+'</m:e><m:sub>'+mrun(g.sub,r)+'</m:sub></m:sSub>';
  }
  izliet();
  return x;
}
function wtext(t,st){
  /* Word teksts ar indeksiem: indekss ir gabals ar vertAlign="subscript". */
  return window.FD_MATH.indeksi(t).map(function(g){
    var ir=g.sub!=null,pr=st,k;
    if(ir){pr={};for(k in st)if(st.hasOwnProperty(k))pr[k]=st[k];pr.sub=true;}
    return '<w:r>'+rPr(pr)+'<w:t xml:space="preserve">'+
           esc(ir?g.sub:g.text)+'</w:t></w:r>';
  }).join("");
}
function mrad(izteiksme,r){
  return '<m:rad><m:radPr><m:degHide m:val="1"/><m:ctrlPr>'+r+
         '</m:ctrlPr></m:radPr><m:deg/><m:e>'+mtext(izteiksme,r)+'</m:e>'+
         '</m:rad>';
}
function mf(g,r){
  return '<m:f><m:fPr><m:ctrlPr>'+r+'</m:ctrlPr></m:fPr>'+
         '<m:num>'+mbody(g[0],r)+'</m:num>'+
         '<m:den>'+mbody(g[1],r)+'</m:den></m:f>';
}
function mbody(list,r){
  /* Atomu saraksts -> OMML saturs (teksts, sakne, daļa). */
  var x="",i,g;
  for(i=0;i<list.length;i++){
    g=list[i];
    x+=g.frac?mf(g.frac,r):(g.root!=null?mrad(g.root,r):mtext(g.text,r));
  }
  return x;
}
function omath(saturs){return '<m:oMath>'+saturs+'</m:oMath>';}

function runs(o){
  /* Rindkopa ir vai nu viens teksts, vai vairāki gabali ar savu izskatu. */
  var list=o.parts||[{text:o.text}],x="",i;
  for(i=0;i<list.length;i++){
    var r=list[i];
    var st={bold:r.bold==null?o.bold:r.bold,
            italic:r.italic==null?o.italic:r.italic,
            color:r.color==null?o.color:r.color,
            size:r.size==null?o.size:r.size,
            underline:r.underline};
    if(r.frac){x+=omath(mf(r.frac,rPr(st)));continue;}
    if(r.root!=null){x+=omath(mrad(r.root,rPr(st)));continue;}
    if(r.text==null||r.text==="")continue;
    x+=wtext(r.text,st);
  }
  return x;
}
function para(o){return '<w:p>'+pPr(o)+runs(o)+'</w:p>';}
function pageBreak(){return '<w:p><w:r><w:br w:type="page"/></w:r></w:p>';}

var BORDER=["top","left","bottom","right","insideH","insideV"].map(
  function(s){return '<w:'+s+' w:val="single" w:sz="4" w:color="A6A6A6"/>';}
).join("");

function cell(c,width){
  var x='<w:tcPr><w:tcW w:w="'+tw(width)+'" w:type="dxa"/>';
  if(c.fill)x+='<w:shd w:val="clear" w:color="auto" w:fill="'+c.fill+'"/>';
  x+='<w:vAlign w:val="center"/></w:tcPr>';
  /* Šūnā var būt vairākas rindkopas (ATGĀDNE), tāpēc vienmēr saraksts. */
  var ps=c.paras||[c],body="",i;
  for(i=0;i<ps.length;i++){
    var p=ps[i];
    body+=para({text:p.text,parts:p.parts,size:p.size,bold:p.bold,
                italic:p.italic,color:p.color,align:p.align,
                before:i?0:1,after:i<ps.length-1?0:1});
  }
  return '<w:tc>'+x+body+'</w:tc>';
}
function table(o){
  var w=o.widths,grid="",i,x="";
  for(i=0;i<w.length;i++)grid+='<w:gridCol w:w="'+tw(w[i])+'"/>';
  x+='<w:tbl><w:tblPr><w:tblW w:w="0" w:type="auto"/>';
  x+=o.plain?"":'<w:tblBorders>'+BORDER+'</w:tblBorders>';
  x+='<w:tblLayout w:type="fixed"/></w:tblPr><w:tblGrid>'+grid+'</w:tblGrid>';
  for(i=0;i<o.rows.length;i++){
    var row=o.rows[i],j,tr='<w:tr>';
    if(row.height)tr+='<w:trPr><w:trHeight w:hRule="atLeast" w:val="'+
      tw(row.height)+'"/></w:trPr>';
    var cells=row.cells||row;
    for(j=0;j<w.length;j++)tr+=cell(cells[j]||{text:""},w[j]);
    x+=tr+'</w:tr>';
  }
  return x+'</w:tbl>';
}

function sectPr(){
  var m=CFG.margin;
  return '<w:sectPr><w:pgSz w:w="'+tw(CFG.page[0])+'" w:h="'+
         tw(CFG.page[1])+'"/><w:pgMar w:top="'+tw(m[0])+'" w:right="'+
         tw(m[1])+'" w:bottom="'+tw(m[2])+'" w:left="'+tw(m[3])+
         '" w:header="0" w:footer="0" w:gutter="0"/></w:sectPr>';
}

function body(blocks){
  var x="",i;
  for(i=0;i<blocks.length;i++){
    var b=blocks[i];
    if(b.t==="tbl"){
      x+=table(b);
      /* Aiz tabulas vajag rindkopu, citādi Word salīmē divas tabulas kopā. */
      x+=para({text:"",size:2,after:2});
    }
    else if(b.t==="pb")x+=pageBreak();
    else x+=para(b);
  }
  return x;
}

var NS='xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/'+
       'main" xmlns:m="http://schemas.openxmlformats.org/officeDocument/'+
       '2006/math"';
var HEAD='<?xml version="1.0" encoding="UTF-8" standalone="yes"?>';

var TYPES=HEAD+'<Types xmlns="http://schemas.openxmlformats.org/package/'+
  '2006/content-types">'+
  '<Default Extension="rels" ContentType="application/vnd.openxmlformats-'+
  'package.relationships+xml"/>'+
  '<Default Extension="xml" ContentType="application/xml"/>'+
  '<Override PartName="/word/document.xml" ContentType="application/vnd.'+
  'openxmlformats-officedocument.wordprocessingml.document.main+xml"/>'+
  '<Override PartName="/word/styles.xml" ContentType="application/vnd.'+
  'openxmlformats-officedocument.wordprocessingml.styles+xml"/></Types>';

var RELS=HEAD+'<Relationships xmlns="http://schemas.openxmlformats.org/'+
  'package/2006/relationships"><Relationship Id="rId1" Type="http://'+
  'schemas.openxmlformats.org/officeDocument/2006/relationships/'+
  'officeDocument" Target="word/document.xml"/></Relationships>';

var DRELS=HEAD+'<Relationships xmlns="http://schemas.openxmlformats.org/'+
  'package/2006/relationships"><Relationship Id="rId1" Type="http://'+
  'schemas.openxmlformats.org/officeDocument/2006/relationships/styles" '+
  'Target="styles.xml"/></Relationships>';

function styles(){
  return HEAD+'<w:styles '+NS+'><w:docDefaults><w:rPrDefault><w:rPr>'+
    '<w:rFonts w:ascii="'+CFG.font+'" w:hAnsi="'+CFG.font+'"/>'+
    '<w:sz w:val="'+half(CFG.size)+'"/><w:szCs w:val="'+half(CFG.size)+
    '"/><w:lang w:val="lv-LV"/></w:rPr></w:rPrDefault><w:pPrDefault>'+
    '<w:pPr><w:spacing w:after="'+pt(3)+'"/></w:pPr></w:pPrDefault>'+
    '</w:docDefaults></w:styles>';
}

function build(blocks){
  var doc=HEAD+'<w:document '+NS+'><w:body>'+body(blocks)+sectPr()+
          '</w:body></w:document>';
  return zip([
    {name:"[Content_Types].xml",data:utf8(TYPES)},
    {name:"_rels/.rels",data:utf8(RELS)},
    {name:"word/_rels/document.xml.rels",data:utf8(DRELS)},
    {name:"word/document.xml",data:utf8(doc)},
    {name:"word/styles.xml",data:utf8(styles())}
  ]);
}

function save(blob,name){
  var url=URL.createObjectURL(blob),a=document.createElement("a");
  a.href=url;a.download=name;document.body.appendChild(a);a.click();
  document.body.removeChild(a);
  setTimeout(function(){URL.revokeObjectURL(url);},2000);
}

return {build:build,save:save};
})();
"""
