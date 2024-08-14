const aboutCardButtons = document.querySelectorAll('.about-card button');

for (const button of aboutCardButtons) {
    button.addEventListener('click', showContent);
}

/**
 * Get the about content which had the same parent element as the button clicked
 * Switch the class 'opaque' on and off for the about content
 */
function showContent() {
    const aboutContent = this.parentElement.getElementsByClassName('about-content')[0];
    aboutContent.classList.toggle('opaque');
    if (this.innerText === 'Click for more') {
        this.innerText = 'Hide text';
    } else {
        this.innerText = 'Click for more';
    }
}
