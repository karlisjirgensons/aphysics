/**
 * Calcubo «Get early access» -> this Google Sheet.
 *
 * The form on calcubo.lv/play posts here in the background; the visitor
 * never leaves the page and never sees Google.
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
    var sh = ss.getSheetByName(LAPA) || ss.insertSheet(LAPA);
    if (sh.getLastRow() === 0) {
      sh.appendRow(["time", "email", "source", "language", "result"]);
    }
    sh.appendRow([new Date(), drosi(epasts), drosi(p.avots),
                  drosi(p.valoda), drosi(p.r)]);
  } finally {
    lock.releaseLock();
  }
  return ContentService.createTextOutput("ok");
}

/* Short, and never read as a formula (=, +, -, @ at the start). */
function drosi(s) {
  s = String(s || "").slice(0, 254);
  return /^[=+\-@]/.test(s) ? "'" + s : s;
}
