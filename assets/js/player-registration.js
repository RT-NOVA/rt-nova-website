(() => {
  const frame = document.querySelector("iframe[data-player-registration]");
  const age = new URLSearchParams(window.location.search).get("age");
  const supportedAges = ["10U", "11U", "12U", "13U", "14U"];
  if (!frame || !supportedAges.includes(age)) return;

  const formURL = new URL(frame.src);
  // Jotform's actual field unique name includes this spelling.
  formURL.searchParams.set("playerCopetition", age);
  frame.src = formURL.toString();
})();
