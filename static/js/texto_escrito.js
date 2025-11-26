  	const text = "Recordando los pasos pequeños, compartiendo las cosas de  nuestras vidas, atesorando cada momento.";
    const container = document.getElementById("sparkText");

    const words = text.split(" ");
    words.forEach(word => {
      const wordSpan = document.createElement("span");
      wordSpan.className = "word";

      word.split("").forEach(char => {
        const letterSpan = document.createElement("span");
        letterSpan.textContent = char;
        letterSpan.className = "letter";
        wordSpan.appendChild(letterSpan);
      });

      container.appendChild(wordSpan);
    });

    // Animación con GSAP al hacer scroll
    gsap.registerPlugin(ScrollTrigger);

    gsap.fromTo(".letter", {
      opacity: 0,
      scale: 0.5,
      rotation: 0,
      textShadow: "0 0 0px #000000ff"
    }, {
      opacity: 1,
      scale: 1,
      rotation: 0,
      /*textShadow: "0 0 5px #000000ff, 0 0 15px #ff0, 0 0 25px #f0f, 0 0 35px #0ff",*/
      stagger: 0.05,
      duration: 0.6,
      ease: "power2.out",
      scrollTrigger: {
        trigger: "#sparkText",
        start: "top 550px ",
		markers: true,
		end: "bottom 10px",
		toggleActions: "play pause restart play"

       /* once: true*/
      }
    });