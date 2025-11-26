    gsap.registerPlugin(ScrollTrigger);

    const sections = document.querySelectorAll(".section");

    sections.forEach(section => {
      gsap.to(section, {
        opacity: 1,
        scale: 1,
        duration: 0.5,
        ease: "power2.out",
        scrollTrigger: {
          trigger: section,
          start: "top center",
          markers: true,
          toggleActions: "play none none none"
        }
      });
    });