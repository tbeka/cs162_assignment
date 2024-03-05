
// Visibility of add new element form
function toggleAddForm(formId) {
    var form = document.getElementById(formId);
    form.style.display = form.style.display === "none" ? "block" : "none";
}
// Visibility of the edit task form
function toggleEditTask(itemId) {
    const titleContainer = document.getElementById(`task-title-container-${itemId}`);
    const editForm = document.getElementById(`edit-task-form-${itemId}`);
    if (editForm.style.display === "none") {
        editForm.style.display = "block";
        titleContainer.style.display = "none";
    } else {
        editForm.style.display = "none";
        titleContainer.style.display = "block";
    }
}

// Visibility of the edit list form
function toggleEditList(listId) {
    const titleContainer = document.getElementById(`list-title-container-${listId}`);
    const editForm = document.getElementById(`edit-form-${listId}`);
    if (editForm.style.display === "none") {
        editForm.style.display = "block";
        titleContainer.style.display = "none";
    } else {
        editForm.style.display = "none";
        titleContainer.style.display = "block";
    }
}

// Handle the dragover event for droppable elements
function allowDrop(ev) {
    ev.preventDefault();
    var target = ev.target;
    while(target && target.getAttribute('data-list-id') === null) {
        target = target.parentNode;
        if(target.nodeName === "BODY") {
            ev.stopPropagation();
            return false;
        }
    }
}

// Handle drag event for draggable elements
function drag(ev) {
    ev.dataTransfer.setData("text", ev.target.id);
}


// Handle drop event for draggable elements
function drop(ev) {
    ev.preventDefault();
    var data = ev.dataTransfer.getData("text");
    var target = ev.target;
    while(target && target.getAttribute('data-list-id') === null) {
        target = target.parentNode;
        if(target.nodeName === "BODY") return;
    }

    var droppedElement = document.getElementById(data);
    if(target && target.classList.contains('box')) {
        target.appendChild(droppedElement);
        var itemId = data.split('-')[1];
        var newListId = target.getAttribute('data-list-id');
        fetch('/update_item_position', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
            },
            body: JSON.stringify({item_id: itemId, new_list_id: newListId}),
        })
        .then(response => response.json())
        .then(data => console.log('Success:', data))
        .catch((error) => console.error('Error:', error));
    }
}

// Toggle the visibility of subtasks for a given item
function toggleExpandCollapse(itemId) {
    fetch(`/toggle-collapse/${itemId}`, { method: 'POST' })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                const subtasks = document.getElementById(`subtasks-${itemId}`);
                subtasks.style.display = data.is_collapsed ? 'none' : 'block';
            } else {
                console.error('Failed to toggle the collapsed state.');
            }
        })
        .catch(error => console.error('Error:', error));
}