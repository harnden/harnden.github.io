document.addEventListener('DOMContentLoaded', function() {
    // Get the main elements
    const track = document.querySelector('.career-slider-track');
    const cards = document.querySelectorAll('.career-card');
    const prevBtn = document.querySelector('.prev-btn');
    const nextBtn = document.querySelector('.next-btn');
    
    // Set initial state
    let currentIndex = 0;
    const totalCards = cards.length;

    // Function to update the slider position
    function updateSlider() {
        // Calculate the distance to move (in percentage)
        // e.g., Card 1: 0%, Card 2: -100%, Card 3: -200%
        const offset = -currentIndex * 100;
        track.style.transform = `translateX(${offset}%)`;

        // Update button disabled state
        prevBtn.disabled = currentIndex === 0;
        nextBtn.disabled = currentIndex === totalCards - 1;
    }

    // Event listener for the "Next" button
    nextBtn.addEventListener('click', () => {
        if (currentIndex < totalCards - 1) {
            currentIndex++;
            updateSlider();
        }
    });

    // Event listener for the "Previous" button
    prevBtn.addEventListener('click', () => {
        if (currentIndex > 0) {
            currentIndex--;
            updateSlider();
        }
    });

  
// Get modal elements after the cards and track are defined
const modal = document.getElementById('full-image-modal');
const modalImage = document.getElementById('modal-image');
const closeBtn = document.getElementById('modal-close-btn');

cards.forEach(card => {
    const imageWrapper = card.querySelector('.card-image-wrapper');
    const image = card.querySelector('.card-image-wrapper img');
    
    if (imageWrapper) {
        imageWrapper.addEventListener('click', () => {
            // 1. Get the source URL of the clicked image
            const imageSource = image.src;
            
            // 2. Set the modal's image source and alternate text
            modalImage.src = imageSource;
            modalImage.alt = image.alt;

            // 3. Display the modal (overriding the initial 'display: none;')
            modal.style.display = 'flex'; 
        });
    }
});

// Event listener to close the modal when the 'X' is clicked
closeBtn.addEventListener('click', () => {
    modal.style.display = 'none';
});

// Event listener to close the modal when the background is clicked
modal.addEventListener('click', (event) => {
    // Check if the click happened directly on the modal background, not the image inside
    if (event.target === modal) {
        modal.style.display = 'none';
    }
});

// Initialize the slider position and button state on page load
updateSlider();
});

