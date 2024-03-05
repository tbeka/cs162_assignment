// Toggle visibility of forms based on their IDs
function toggleAddForm(formId) {
    var form = document.getElementById(formId);
    form.style.display = form.style.display === "none" ? "block" : "none";
}

// Toggle between display and edit mode for tasks
function toggleEditTask(itemId) {
    const titleContainer = document.getElementById(`task-title-container-${itemId}`);
    const editForm = document.getElementById(`edit-task-form-${itemId}`);
    titleContainer.style.display = titleContainer.style.display === "none" ? "block" : "none";
    editForm.style.display = editForm.style.display === "none" ? "block" : "none";
}

// Toggle between display and edit mode for lists
function toggleEditList(listId) {
    const titleContainer = document.getElementById(`list-title-container-${listId}`);
    const editForm = document.getElementById(`edit-form-${listId}`);
    titleContainer.style.display = titleContainer.style.display === "none" ? "block" : "none";
    editForm.style.display = editForm.style.display === "none" ? "block" : "none";
}

// Allow dropping elements into designated drop zones
function allowDrop(ev) {
    ev.preventDefault();
    // Logic to ensure dropping is allowed only on specific targets
}

// Store the id of the dragged element
function drag(ev) {
    ev.dataTransfer.setData("text", ev.target.id);
}

// Handle drop event for draggable elements
function drop(ev) {
    ev.preventDefault();
    // Logic to handle element drop, updating its position on the server
}

// Toggle the visibility of subtasks for a given item
function toggleExpandCollapse(itemId) {
    // Logic to toggle the collapsed state of an item, affecting subtask visibility
}