document.addEventListener('DOMContentLoaded', () => {
    const container = document.getElementById('flashcard-container');
    const flashcards = JSON.parse(container.dataset.flashcards || '[]');

    let currentIndex = 0;
    let isFlipped = false;

    const flashcardContent = document.getElementById('flashcard-content');
    const flashcardInner = document.getElementById('flashcard-inner');
    const currentCardElem = document.getElementById('current-card');
    const prevBtn = document.getElementById('prev-btn');
    const nextBtn = document.getElementById('next-btn');
    const flipBtn = document.getElementById('flip-btn');

    function updateCard() {
        if (!flashcards.length) {
            flashcardContent.textContent = 'No cards available';
            return;
        }

        const card = flashcards[currentIndex];
        flashcardContent.textContent = isFlipped ? card.back : card.front;

        flashcardInner.className = isFlipped ? 'flashcard-inner flipped' : 'flashcard-inner';
        currentCardElem.textContent = currentIndex + 1;

        prevBtn.disabled = currentIndex === 0;
        nextBtn.disabled = currentIndex === flashcards.length - 1;
    }

    prevBtn.addEventListener('click', () => {
        if (currentIndex > 0) { currentIndex--; isFlipped = false; updateCard(); }
    });

    nextBtn.addEventListener('click', () => {
        if (currentIndex < flashcards.length - 1) { currentIndex++; isFlipped = false; updateCard(); }
    });

    flipBtn.addEventListener('click', () => {
        isFlipped = !isFlipped; updateCard();
    });

    updateCard();
});