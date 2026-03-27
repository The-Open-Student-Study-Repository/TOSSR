document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.view-btn').forEach(btn => {
        btn.addEventListener('click', function() {
            const materialId = this.dataset.materialId;
            const materialType = this.dataset.materialType;

            let url = '';
            if (materialType === 'flashcard') {
                url = `/materials/flashcard/${materialId}/`;
            } else if (materialType === 'quiz') {
                url = `/materials/quiz/${materialId}/`;
            }

            if (url) {
                window.location.href = url;
            }
        });
    });
});