/**
 * Calcubo «Get early access» -> this Google Sheet.
 *
 * The forms on calcubo.lv/play, /parent and /smart post here in the
 * background; the visitor never leaves the page and never sees Google.
 *
 * Setup (once, ~2 minutes):
 *  1. Create a Google Sheet (e.g. "Calcubo leads").
 *  2. Extensions -> Apps Script, replace the code with this file, Save.
 *  3. Deploy -> New deployment -> type "Web app":
 *       Execute as: Me
 *       Who has access: Anyone
 *     -> Deploy, allow access, copy the Web app URL (ends with /exec).
 *  4. Paste the URL into _tools/play_forma.py ADRESE and run
 *     python _tools/gen_play.py
 *
 * After editing this script: Deploy -> Manage deployments -> edit ->
 * Version "New version" (the URL stays the same).
 */

var LAPA = "Leads";
var EPASTS = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;

/* Pages with their own tab: source -> [tab, columns after time & email].
   calcubo.lv/parent keeps only email + language; calcubo.lv/smart also the
   grade the parent picked. Everything else (calcubo.lv/play) -> LAPA. */
var CILNES = {
  parent: ["parent", ["language"]],
  smart: ["smart", ["language", "grade"]]
};

function doPost(e) {
  var p = (e && e.parameter) || {};
  var epasts = String(p.epasts || "").trim().toLowerCase();
  // p.web is a hidden field only bots fill in
  if (p.web || epasts.length > 254 || !EPASTS.test(epasts)) {
    return ContentService.createTextOutput("no");
  }
  var lock = LockService.getScriptLock();
  lock.waitLock(10000);
  try {
    var ss = SpreadsheetApp.getActiveSpreadsheet();
    var c = CILNES[p.avots];
    if (c) {
      var vertibas = {language: p.valoda, grade: p.klase};
      cilne(ss, c[0], ["time", "email"].concat(c[1])).appendRow(
        [new Date(), drosi(epasts)].concat(c[1].map(function (k) {
          return drosi(vertibas[k]);
        })));
    } else {
      cilne(ss, LAPA, ["time", "email", "source", "language", "result"])
        .appendRow([new Date(), drosi(epasts), drosi(p.avots),
                    drosi(p.valoda), drosi(p.r)]);
    }
  } finally {
    lock.releaseLock();
  }
  return ContentService.createTextOutput("ok");
}

/* Tab by name (created if missing), header row written if it is empty. */
function cilne(ss, vards, galva) {
  var sh = ss.getSheetByName(vards) || ss.insertSheet(vards);
  if (sh.getLastRow() === 0) sh.appendRow(galva);
  return sh;
}

/* Short, and never read as a formula (=, +, -, @ at the start). */
function drosi(s) {
  s = String(s || "").slice(0, 254);
  return /^[=+\-@]/.test(s) ? "'" + s : s;
}
