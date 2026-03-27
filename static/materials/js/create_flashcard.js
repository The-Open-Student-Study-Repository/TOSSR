// create_flashcard.js
const cards = [];

// Add a new card
document.getElementById('addCardBtn').addEventListener('click', function() {
    const front = document.getElementById('front').value.trim();
    const back = document.getElementById('back').value.trim();

    if (!front || !back) {
        showMessage('Please fill in both front and back', 'error');
        return;
    }

    cards.push({ front, back });
    document.getElementById('front').value = '';
    document.getElementById('back').value = '';
    document.getElementById('front').focus();

    renderCards();
    showMessage('Card added to set!', 'success');
});

// Render cards
function renderCards() {
    const container = document.getElementById('flashcard-list');

    if (cards.length === 0) {
        container.innerHTML = `
            <div class="empty-state">
                <div class="empty-state-icon">📋</div>
                <p>No cards added yet. Create your first card above!</p>
            </div>
        `;
        return;
    }

    container.innerHTML = `<h3>Cards in Set (${cards.length})</h3>`;

    cards.forEach((card, index) => {
        const cardDiv = document.createElement('div');
        cardDiv.className = 'flashcard-item';
        cardDiv.innerHTML = `
            <div class="flashcard-content">
                <span class="flashcard-index">${index + 1}</span>
                <strong>Front:</strong>
                <p>${escapeHtml(card.front)}</p>
                <div style="margin-top: 12px;">
                    <strong>Back:</strong>
                    <p>${escapeHtml(card.back)}</p>
                </div>
            </div>
            <button type="button" class="remove-card-btn" onclick="removeCard(${index})">Remove</button>
        `;
        container.appendChild(cardDiv);
    });
}

// Remove a card
function removeCard(index) {
    cards.splice(index, 1);
    renderCards();
    showMessage('Card removed', 'success');
}

// Escape HTML
function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

// Show messages
function showMessage(text, type) {
    const messageDiv = document.getElementById('message');
    messageDiv.textContent = text;
    messageDiv.className = 'message show ' + type;
    setTimeout(() => {
        messageDiv.textContent = '';
        messageDiv.className = 'message';
    }, 4000);
}

// Submit flashcard set
document.getElementById('submitBtn').addEventListener('click', async function() {
    const title = document.getElementById('title').value.trim();
    const moduleId = document.getElementById('module').value;

    if (!title) {
        showMessage('Please enter a title for your flashcard set', 'error');
        return;
    }

    if (cards.length === 0) {
        showMessage('Please add at least one card', 'error');
        return;
    }

    const payload = {
        title: title,
        module_id: moduleId || null,
        is_published: document.getElementById('publish').checked,
        cards: cards.map((card, index) => ({...card, order: index + 1}))
    };

    this.disabled = true;
    this.textContent = 'Creating...';

    try {
        const response = await fetch('/materials/api/flashcards/create/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify(payload)
        });

        const data = await response.json();

        if (response.ok) {
            showMessage('✓ Flashcard set created successfully!', 'success');
            setTimeout(() => {
                window.location.href = '/materials/my-resources/';
            }, 1500);
        } else {
            showMessage('Error: ' + (data.error || 'Unknown error'), 'error');
            this.disabled = false;
            this.textContent = 'Create Flashcard Set';
        }
    } catch (error) {
        showMessage('Error: ' + error.message, 'error');
        this.disabled = false;
        this.textContent = 'Create Flashcard Set';
    }
});

// Get CSRF token from cookie
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}