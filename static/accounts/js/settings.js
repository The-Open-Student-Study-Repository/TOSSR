document.addEventListener('DOMContentLoaded', () => {
    const checkboxes = document.querySelectorAll(".theme-check");

    checkboxes.forEach(box => {
        box.addEventListener("change", () => {
            if (box.checked) {
                // Uncheck all other checkboxes
                checkboxes.forEach(other => {
                    if (other !== box) other.checked = false;
                });

                // Save selected theme in cookie
                const theme = box.value;
                document.cookie = `theme=${theme}; path=/; max-age=${60*60*24}`;

                // Reload to apply theme
                location.reload();
            } else {
                // Prevent unchecking active theme (always one selected)
                box.checked = true;
            }
        });
    });
});