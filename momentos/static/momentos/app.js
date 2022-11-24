function init() {
  const LAT = 24.14437;
  const LNG = -110.3005;
  const map = L.map("map").setView([LAT, LNG], 13);
  const modal = new bootstrap.Modal("#staticBackdrop", {
    focus: true,
    keyboard: false,
  });

  L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
    attribution:
      '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
  }).addTo(map);
  map.on("click", function (e) {
    const {
      latlng: { lat, lng },
    } = e;
    document.querySelector("#latHidden").value = lat;
    document.querySelector("#lngHidden").value = lng;
    modal.show();
  });

  const str = document.querySelector("#momentosData").textContent;
  const data = parseData(parseData(str));

  data.forEach(function (d) {
    const {
      fields: { content, lat, lng },
    } = d;
    L.marker([lat, lng]).addTo(map).bindPopup(content);
  });
}

function parseData(str) {
  return JSON.parse(str);
}

window.addEventListener("load", init);
