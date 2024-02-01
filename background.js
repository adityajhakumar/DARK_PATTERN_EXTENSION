// background.js
chrome.runtime.onInstalled.addListener(function () {
  console.log("Dark Pattern Extension installed");
});

chrome.runtime.onMessage.addListener(function (message, sender, sendResponse) {
  if (message.action === "openNewTab") {
    const mlUrl = "http://127.0.0.1:5000/";  // Replace with your ML server URL
    const newTabUrl = mlUrl + "?url=" + encodeURIComponent(message.url);
    chrome.tabs.create({ url: newTabUrl });
  }
});
