(function (b) {
  function f(c, a) { 0 < c.timeOut && clearTimeout(a); b("#" + c.overlayId + ", #" + c.messageHolderId).fadeOut("fast", function () { b("#" + c.overlayId + ", #" + c.messageHolderId).remove() }); b(document).unbind("keyup") } b.fn.leaveNotice = function (c) {
    var a = b.extend({
      siteName: "NIST", exitMessage: "<h2><strong>Thank you for visiting {SITENAME}.</strong></h2><p>We hope your visit was informative.</p><p>We have provided this link to a non-NIST site because it has information that may be of interest to our users. NIST does not necessarily endorse the views expressed or the facts presented on this site. Further, NIST does not endorse any commercial products that may be advertised or available on this site.</p>",
      preLinkMessage: "<div class='setoff'><p>You will now be directed to:<br/>{URL}</p></div>", linkString: "", newWindow: !1, timeOut: 1E4, overlayId: "ln-blackout", messageBoxId: "ln-messageBox", messageHolderId: "ln-messageHolder", linkId: "ln-link", displayUrlLength: 50, overlayAlpha: .3
    }, c); return this.each(function () {
      el = b(this); var d = el.attr("href"), g = a.displayUrlLength, e = d.length >= g ? "..." : ""; g = d.substr(0, g) + e; e = el.attr("title"); var h = void 0 === e || "" == e ? g : e; a.timeOut = a.newWindow ? 0 : a.timeOut; el.click(function () {
        b("body").append('<div id="' +
          a.overlayId + '"></div>'); b("body").append('<div id="' + a.messageHolderId + '"><div id="' + a.messageBoxId + '"></div></div>'); !1 !== a.overlayAlpha && b("#" + a.overlayId).css("opacity", a.overlayAlpha); preFilteredContent = a.exitMessage + a.preLinkMessage; msgContent = preFilteredContent.replace(/\{URL\}/g, '<a id="' + a.linkId + '" href="' + d + '" title="' + d + '"' + a.linkString + ">" + h + "</a>"); msgContent = msgContent.replace(/\{SITENAME\}/g, a.siteName); msgContent = 0 < a.timeOut ? msgContent + '<p id="ln-cancelMessage"><a href="#close" id="ln-cancelLink">Cancel</a> or press the ESC key.</p>' :
            msgContent + '<p id="ln-cancelMessage">Click the link above to continue or <a href="#close" id="ln-cancelLink">Cancel</a></p>'; b("#" + a.messageBoxId).append(msgContent); leaveIn = 0 < a.timeOut ? setTimeout(function () { b("#ln-cancelMessage").html("<em>Loading...</em>"); window.location.href = d }, a.timeOut) : !1; a.newWindow && b("a#" + a.linkId).attr("target", "_blank").click(function () { f(a, leaveIn) }); b("#ln-cancelLink").click(function () { f(a, leaveIn); return !1 }); b(document).bind("keyup", function (k) { 27 == k.which && f(a, leaveIn) });
        b(window).on("unload", function () { f(a, leaveIn) }); return !1
      })
    })
  }
})(jQuery);