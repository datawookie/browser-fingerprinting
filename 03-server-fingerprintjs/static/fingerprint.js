import FingerprintJS from 'https://openfpcdn.io/fingerprintjs/v3/fp.min.js';

(async () => {
  const fp = await FingerprintJS.load();
  const result = await fp.get();

  const payload = {
    visitorId: result.visitorId,
    components: result.components
  };

  document.getElementById('output').textContent = JSON.stringify(payload, null, 2);

  // Send it to the server
  await fetch("/submit", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload)
  });
})();
