document.addEventListener('DOMContentLoaded', () => {
    const container = document.getElementById('quiz-container');
    const questions = JSON.parse(container.dataset.questions || '[]');

    let currentIndex = 0;
    const answeredQuestions = {};

    function showQuestion() {
        if (!questions.length) return;
        const question = questions[currentIndex];

        document.getElementById('current-question').textContent = currentIndex + 1;
        document.getElementById('question-content').textContent = question.question_text;

        const aContent = document.getElementById('answers-content');
        aContent.innerHTML = '';
        const isAnswered = answeredQuestions[currentIndex];

        question.answers.forEach(answer => {
            const div = document.createElement('div');
            div.className = 'answer-option';
            if (isAnswered) {
                if (answer.id === isAnswered.selectedId) {
                    div.classList.add(answer.is_correct ? 'correct' : 'incorrect');
                }
                if (answer.is_correct) div.classList.add('show-correct');
            }
            div.innerHTML = `
                <input type="radio" id="answer-${answer.id}" name="quiz-answer" value="${answer.id}" ${isAnswered ? 'disabled' : ''}>
                <label for="answer-${answer.id}">${answer.answer_text}</label>
            `;
            aContent.appendChild(div);
        });

        document.getElementById('prev-btn').disabled = currentIndex === 0;
        document.getElementById('next-btn').disabled = currentIndex === questions.length - 1;

        document.getElementById('check-btn').disabled = !document.querySelector('input[name="quiz-answer"]:checked') || isAnswered;
        document.getElementById('reset-btn').disabled = !isAnswered;
    }

    function checkAnswer() {
        const selectedRadio = document.querySelector('input[name="quiz-answer"]:checked');
        if (!selectedRadio) return;
        answeredQuestions[currentIndex] = { selectedId: parseInt(selectedRadio.value) };
        showQuestion();
    }

    function resetQuestion() {
        delete answeredQuestions[currentIndex];
        document.querySelectorAll('input[name="quiz-answer"]').forEach(r => r.checked = false);
        showQuestion();
    }

    document.getElementById('prev-btn').addEventListener('click', () => {
        if (currentIndex > 0) { currentIndex--; showQuestion(); }
    });

    document.getElementById('next-btn').addEventListener('click', () => {
        if (currentIndex < questions.length - 1) { currentIndex++; showQuestion(); }
    });

    document.getElementById('check-btn').addEventListener('click', checkAnswer);
    document.getElementById('reset-btn').addEventListener('click', resetQuestion);

    document.addEventListener('change', (e) => {
        if (e.target.name === 'quiz-answer') {
            document.getElementById('check-btn').disabled = false;
        }
    });

    showQuestion();
});