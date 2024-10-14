function scrollToSection(sectionId) {
    const section = document.getElementById(sectionId);
    section.scrollIntoView({ behavior: 'smooth' });
}

function setImage(imageSrc) {
    const currentImage = document.getElementById('gallery-image');
    currentImage.src = imageSrc;
}
