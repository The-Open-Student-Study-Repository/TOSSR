document.addEventListener('DOMContentLoaded', () => {
    const root = document.getElementById('create-quiz-root');
    const CSRF_TOKEN = root.dataset.csrfToken;
    const API_URL = root.dataset.apiUrl;
    const REDIRECT_URL = root.dataset.redirectUrl;
    const questions = [];

    const answersContainer = document.getElementById('answers-container');
    const questionTextInput = document.getElementById('question-text');

    function escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }

    function showMessage(text, type) {
        const msg = document.getElementById('message');
        msg.textContent = text;
        msg.className = 'message show ' + type;
        setTimeout(() => { msg.textContent = ''; msg.className = 'message'; }, 4000);
    }

    function renderQuestions() {
        const container = document.getElementById('quiz-questions-list');
        if (questions.length === 0) {
            container.innerHTML = '<div class="empty-state"><div class="empty-state-icon">📋</div><p>No questions added yet. Create your first question above!</p></div>';
            return;
        }
        container.innerHTML = '<h3>Questions in Quiz (' + questions.length + ')</h3>';
        questions.forEach((q, i) => {
            const qDiv = document.createElement('div');
            qDiv.className = 'question-item';

            let answersHtml = '<div class="answers-list"><strong>Answers:</strong>';
            q.answers.forEach(a => {
                const badge = a.is_correct ? '<span class="answer-badge">✓</span>' : '';
                answersHtml += `<div class="answer-item${a.is_correct ? ' correct' : ''}">${badge}${escapeHtml(a.answer_text)}</div>`;
            });
            answersHtml += '</div>';

            qDiv.innerHTML = `
                <div class="question-header">
                    <div class="question-text">
                        <span class="question-index">${i+1}</span>
                        <strong>Question:</strong>
                        <p>${escapeHtml(q.question_text)}</p>
                    </div>
                    <button type="button" class="remove-question-btn" data-index="${i}">Remove</button>
                </div>
                ${answersHtml}
            `;
            container.appendChild(qDiv);
        });
        // attach remove listeners
        container.querySelectorAll('.remove-question-btn').forEach(btn => {
            btn.addEventListener('click', () => {
                questions.splice(parseInt(btn.dataset.index), 1);
                renderQuestions();
                showMessage('Question removed', 'success');
            });
        });
    }

    // Add Answer
    document.querySelector('.add-answer-btn').addEventListener('click', () => {
        const index = answersContainer.children.length + 1;
        const div = document.createElement('div');
        div.className = 'answer-input';
        div.innerHTML = `
            <input type="text" class="answer-text" placeholder="Answer option ${index}">
            <input type="checkbox" class="answer-correct" title="Mark as correct answer">
            <label>Correct</label>
            <button type="button" class="remove-answer-btn">Remove</button>
        `;
        answersContainer.appendChild(div);
        div.querySelector('.remove-answer-btn').addEventListener('click', () => div.remove());
    });

    // Remove default answers
    answersContainer.querySelectorAll('.remove-answer-btn').forEach(btn => {
        btn.addEventListener('click', () => btn.parentElement.remove());
    });

    // Add Question
    document.getElementById('addQuestionBtn').addEventListener('click', () => {
        const qText = questionTextInput.value.trim();
        if (!qText) return showMessage('Please enter a question', 'error');

        const answerInputs = answersContainer.querySelectorAll('.answer-input');
        const answers = [];
        let hasCorrect = false;

        for (const input of answerInputs) {
            const text = input.querySelector('.answer-text').value.trim();
            const correct = input.querySelector('.answer-correct').checked;
            if (!text) return showMessage('Please fill in all answer options', 'error');
            if (correct) hasCorrect = true;
            answers.push({ answer_text: text, is_correct: correct });
        }

        if (!hasCorrect) return showMessage('Please mark at least one answer as correct', 'error');

        questions.push({ question_text: qText, question_type: 'single', answers });

        // reset form
        questionTextInput.value = '';
        answersContainer.innerHTML = `
            <div class="answer-input">
                <input type="text" class="answer-text" placeholder="Answer option 1">
                <input type="checkbox" class="answer-correct" title="Mark as correct answer">
                <label>Correct</label>
                <button type="button" class="remove-answer-btn">Remove</button>
            </div>
            <div class="answer-input">
                <input type="text" class="answer-text" placeholder="Answer option 2">
                <input type="checkbox" class="answer-correct" title="Mark as correct answer">
                <label>Correct</label>
                <button type="button" class="remove-answer-btn">Remove</button>
            </div>
        `;
        answersContainer.querySelectorAll('.remove-answer-btn').forEach(btn => btn.addEventListener('click', () => btn.parentElement.remove()));

        renderQuestions();
        showMessage('Question added to quiz!', 'success');
    });

    // Submit Quiz
    document.getElementById('submitBtn').addEventListener('click', async () => {
        const title = document.getElementById('title').value.trim();
        const moduleId = document.getElementById('module').value;
        if (!title) return showMessage('Please enter a title for your quiz', 'error');
        if (!questions.length) return showMessage('Please add at least one question', 'error');

        const payload = { title, module_id: moduleId || null, is_published: document.getElementById('publish').checked, questions };

        const btn = document.getElementById('submitBtn');
        btn.disabled = true;
        btn.textContent = 'Creating...';

        try {
            const res = await fetch(API_URL, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json', 'X-CSRFToken': CSRF_TOKEN },
                body: JSON.stringify(payload)
            });
            const data = await res.json();
            if (res.ok) {
                    showMessage('✓ Quiz created successfully!', 'success');
                    setTimeout(() => { window.location.href = REDIRECT_URL; }, 1500);
                } else {
                showMessage('Error: ' + data.error, 'error');
                btn.disabled = false;
                btn.textContent = 'Create Quiz';
            }
        } catch (err) {
            showMessage('Error: ' + err.message, 'error');
            btn.disabled = false;
            btn.textContent = 'Create Quiz';
        }
    });
});