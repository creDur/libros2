    gsap.registerPlugin(ScrollTrigger);

    const sections = document.querySelectorAll(".seleccionar");

    sections.forEach(seleccionar => {
      gsap.to(seleccionar, {
        opacity: 1,
        scale: 1,
        duration: 0.5,
        ease: "power2.out",
        scrollTrigger: {
          trigger: seleccionar,
          start: "top center",
          markers: true,
          toggleActions: "play none none none"
        }
      });
    });