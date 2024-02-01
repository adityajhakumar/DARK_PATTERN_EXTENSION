// content.js

// Function to send a message to the background script with the current URL
function sendUrlToBackgroundScript() {
    chrome.runtime.sendMessage({ action: 'sendUrl', url: window.location.href });
}

// Function to open a new tab with the provided URL
function openNewTab(url) {
    chrome.tabs.create({ url: url });
}

// Listen for messages from the background script
chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    if (request.action === 'openNewTab') {
        openNewTab(request.url);  // Change 'request.data' to 'request.url'
    }
});

// Call the function to send the current URL to the background script
sendUrlToBackgroundScript();
