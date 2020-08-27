function base_main() {
  navSlide();
}

function navSlide() {
  if (window.innerWidth < 960) {
    const hamburger = document.querySelector(".hamburger");
    let navItems = document.querySelectorAll(".navigation ul li");
    const tl = new TimelineLite({ paused: true, reversed: true });
    const tl2 = new TimelineLite({ paused: true, reversed: true });

    tl.to(
      ".navigation ul",
      1,
      {
        x: "100%",
        ease: Power2.easeOut,
      },
      "-=4" // Does this 4 seconds earlier to gain time for tl2
    );

    for (let i = 0; i < navItems.length; i++) {
      tl2.fromTo(
        navItems[i], // Loops through the whole ul set
        0.15, // Makes its faster for UX
        {
          opacity: 0,
          y: "-30px",
          ease: Power2.easeOut,
        },
        {
          opacity: 1,
          y: "0px",
        },
        "+=0.15"
      );
    }

    hamburger.addEventListener("click", (e) => {
      toggleTween(tl);
      toggleTween(tl2);
    });
  }
}

function toggleTween(tween) {
  tween.reversed() ? tween.play() : tween.reverse();
}

base_main();
