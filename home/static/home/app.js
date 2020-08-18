function main() {
  orangeButton();
  blueButton();
}

function orangeButton() {
  if (window.innerWidth > 960) {
    let btn = document.querySelectorAll(".orange-btn");

    for (i = 0; i < btn.length; i++) {
      btn[i].addEventListener("mouseover", (e) => {
        anime({
          targets: e.target,
          background: ["rgb(255,255,255)", "rgb(255,121,63)"],
          color: ["rgb(255,121,63)", "rgb(255,255,255)"],
        });
      });

      btn[i].addEventListener("mouseout", (e) => {
        anime({
          targets: e.target,
          background: ["rgb(255,121,63)", "rgb(255,255,255)"],
          color: ["rgb(255,255,255)", "rgb(255,121,63)"],
        });
      });
    }
  }

  function blueButton() {
    if (window.innerWidth > 960) {
      let btn = document.querySelectorAll(".blue-btn");

      for (i = 0; i < btn.length; i++) {
        btn[i].addEventListener("mouseover", (e) => {
          anime({
            targets: e.target,
            background: ["rgb(255,255,255)", "rgb(5, 183, 250)"],
            color: ["rgb(5, 183, 250)", "rgb(255,255,255)"],
          });
        });

        btn[i].addEventListener("mouseout", (e) => {
          anime({
            targets: e.target,
            background: ["rgb(5, 183, 250)", "rgb(255,255,255)"],
            color: ["rgb(255,255,255)", "rgb(5, 183, 250)"],
          });
        });
      }
    }
  }
}

main();
