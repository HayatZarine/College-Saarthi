document.addEventListener("DOMContentLoaded", function () {
    const input = document.getElementById("taskInput");
    const list = document.getElementById("todoList");
    const addButton = document.getElementById("addTaskBtn");

    // Function to add a new task
    function addTask() {
        let taskText = input.value.trim();
        if (taskText === "") return;

        let listItem = document.createElement("li");

        // Create label
        let label = document.createElement("label");
        label.className = "checkbox-wrapper";

        // Create checkbox input
        let checkbox = document.createElement("input");
        checkbox.type = "checkbox";
        checkbox.addEventListener("change", function () {
            if (checkbox.checked) {
                labelText.classList.add("completed");
            } else {
                labelText.classList.remove("completed");
            }
        });

        // Create checkmark div
        let checkmark = document.createElement("div");
        checkmark.className = "checkmark";
        checkmark.innerHTML = `
            <svg viewBox="0 0 2 2" fill="none" stroke="currentColor">
                <path d="M20 6L9 17L4 12" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"></path>
            </svg>
        `;

        // Create task label text
        let labelText = document.createElement("span");
        labelText.className = "label";
        labelText.textContent = taskText;

        // Create delete button
        let deleteBtn = document.createElement("button");
        deleteBtn.className = "delete-btn";
        deleteBtn.textContent = "✖";
        deleteBtn.onclick = function () {
            listItem.remove();
        };

        // Append elements together
        label.appendChild(checkbox);
        label.appendChild(checkmark);
        label.appendChild(labelText);
        listItem.appendChild(label);
        listItem.appendChild(deleteBtn);
        list.appendChild(listItem);

        // Clear input field
        input.value = "";
    }

    // Add event listener for "Enter" key
    input.addEventListener("keypress", function (event) {
        if (event.key === "Enter") {
            event.preventDefault();
            addTask();
        }
    });

    // Add event listener for button click
    addButton.addEventListener("click", addTask);
});
