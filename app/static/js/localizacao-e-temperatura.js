(() => {
  'use strict';

  const temperatura = document.querySelector('#temperatura');
  const cidade = document.querySelector('#cidade');

  navigator.geolocation.getCurrentPosition(function (position) {
    const latitude = position.coords.latitude;
    const longitude = position.coords.longitude;

    Promise.all([
      fetch('/temperatura/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ latitude, longitude }),
      })
        .then((response) => response.json())
        .then((data) => {
          const temperaturaComoInteiro = parseInt(data.temperatura);
          temperatura.innerHTML = `${temperaturaComoInteiro} °C`;
        }),

      fetch('/cidade/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ latitude, longitude }),
      })
        .then((response) => response.json())
        .then((data) => {
          cidade.innerHTML = data.cidade;
        }),
    ]);
  });
})();