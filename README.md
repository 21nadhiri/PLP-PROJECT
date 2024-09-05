# PLP-PROJECT
# Nadhiri Time Management
#Code
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nadhiri Time Management</title>
    <style>
        :root {
            --primary-color: #3a7bd5;
            --secondary-color: #00d2ff;
            --bg-color: #f0f4f8;
            --text-color: #2c3e50;
            --light-text: #7f8c8d;
            --alert-color: #e74c3c;
            --success-color: #2ecc71;
        }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
            color: var(--text-color);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .container {
            max-width: 800px;
            width: 90%;
            background: var(--bg-color);
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        }
        h1 {
            color: var(--primary-color);
            text-align: center;
            margin-bottom: 30px;
            font-size: 2.5em;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
        }
        input, select, button {
            width: 100%;
            padding: 12px;
            margin: 10px 0;
            border: 1px solid #ddd;
            border-radius: 5px;
            font-size: 16px;
            transition: all 0.3s ease;
        }
        input:focus, select:focus {
            outline: none;
            border-color: var(--primary-color);
            box-shadow: 0 0 5px rgba(58, 123, 213, 0.5);
        }
        button {
            background: var(--primary-color);
            color: white;
            border: none;
            cursor: pointer;
            transition: background 0.3s ease;
        }
        button:hover {
            background: var(--secondary-color);
        }
        #taskList {
            list-style-type: none;
            padding: 0;
        }
        #taskList li {
            background: white;
            margin: 15px 0;
            padding: 20px;
            border-radius: 10px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 5px 15px rgba(0,0,0,0.05);
            transition: all 0.3s ease;
        }
        #taskList li:hover {
            transform: translateY(-3px);
            box-shadow: 0 7px 20px rgba(0,0,0,0.1);
        }
        .task-content {
            flex-grow: 1;
        }
        .task-info {
            font-size: 0.9em;
            color: var(--light-text);
            margin-top: 8px;
        }
        .task-alert {
            color: var(--alert-color);
            font-weight: bold;
        }
        .delete-btn, .complete-btn, .start-btn {
            padding: 8px 15px;
            margin-left: 10px;
            cursor: pointer;
            border: none;
            border-radius: 5px;
            font-size: 14px;
            transition: all 0.3s ease;
        }
        .delete-btn {
            background: var(--alert-color);
            color: white;
        }
        .complete-btn {
            background: var(--success-color);
            color: white;
        }
        .start-btn {
            background: var(--primary-color);
            color: white;
        }
        .completed {
            text-decoration: line-through;
            opacity: 0.6;
        }
        #filters {
            display: flex;
            justify-content: space-between;
            margin-bottom: 20px;
        }
        #filters select {
            width: 48%;
        }
        #stats {
            text-align: center;
            margin-top: 20px;
            font-size: 1em;
            color: var(--light-text);
            background: white;
            padding: 15px;
            border-radius: 10px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.05);
        }
        #addTaskBtn {
            display: block;
            width: 100%;
            padding: 15px;
            margin: 20px 0;
            background: var(--primary-color);
            color: white;
            border: none;
            border-radius: 5px;
            font-size: 18px;
            cursor: pointer;
            transition: background 0.3s ease;
        }
        #addTaskBtn:hover {
            background: var(--secondary-color);
        }
        .clock-icon {
            font-size: 3em;
            text-align: center;
            margin-bottom: 20px;
            color: var(--primary-color);
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="clock-icon">⏰</div>
        <h1>Nadhiri Time Management</h1>
        <input type="text" id="taskInput" placeholder="Enter a new task">
        <select id="categorySelect">
            <option value="">Select Category</option>
            <option value="Work">Work</option>
            <option value="Personal">Personal</option>
            <option value="Study">Study</option>
        </select>
        <input type="datetime-local" id="dueDateInput">
        <button id="addTaskBtn" onclick="addTask()">Add Task</button>
        
        <div id="filters">
            <select id="categoryFilter" onchange="filterTasks()">
                <option value="">All Categories</option>
                <option value="Work">Work</option>
                <option value="Personal">Personal</option>
                <option value="Study">Study</option>
            </select>
            <select id="statusFilter" onchange="filterTasks()">
                <option value="">All Status</option>
                <option value="active">Active</option>
                <option value="completed">Completed</option>
            </select>
        </div>
        
        <ul id="taskList"></ul>
        
        <div id="stats">
            <span id="totalTasks">Total tasks: 0</span> |
            <span id="completedTasks">Completed tasks: 0</span>
        </div>
    </div>

    <script>
        let tasks = [];

        function addTask() {
            const taskInput = document.getElementById('taskInput');
            const categorySelect = document.getElementById('categorySelect');
            const dueDateInput = document.getElementById('dueDateInput');
            
            if (taskInput.value !== '') {
                const task = {
                    id: Date.now(),
                    text: taskInput.value,
                    category: categorySelect.value,
                    dueDate: new Date(dueDateInput.value),
                    completed: false,
                    startTime: null,
                    timeSpent: 0
                };
                tasks.push(task);
                renderTasks();
                taskInput.value = '';
                categorySelect.value = '';
                dueDateInput.value = '';
            }
        }

        function deleteTask(id) {
            tasks = tasks.filter(task => task.id !== id);
            renderTasks();
        }

        function toggleComplete(id) {
            const task = tasks.find(task => task.id === id);
            if (task) {
                task.completed = !task.completed;
                if (task.completed && task.startTime) {
                    task.timeSpent += (new Date() - task.startTime) / 1000;
                    task.startTime = null;
                }
                renderTasks();
            }
        }

        function startTask(id) {
            const task = tasks.find(task => task.id === id);
            if (task && !task.startTime) {
                task.startTime = new Date();
                renderTasks();
            }
        }

        function formatTime(seconds) {
            const hours = Math.floor(seconds / 3600);
            const minutes = Math.floor((seconds % 3600) / 60);
            return `${hours}h ${minutes}m`;
        }

        function renderTasks() {
            const taskList = document.getElementById('taskList');
            const categoryFilter = document.getElementById('categoryFilter').value;
            const statusFilter = document.getElementById('statusFilter').value;
            
            taskList.innerHTML = '';
            
            const filteredTasks = tasks.filter(task => {
                if (categoryFilter && task.category !== categoryFilter) return false;
                if (statusFilter === 'active' && task.completed) return false;
                if (statusFilter === 'completed' && !task.completed) return false;
                return true;
            });

            filteredTasks.forEach(task => {
                const li = document.createElement('li');
                const now = new Date();
                const timeLeft = (task.dueDate - now) / 1000; // in seconds
                const isOverdue = timeLeft < 0;
                const isNearDue = timeLeft > 0 && timeLeft < 24 * 60 * 60; // less than 24 hours

                let timeSpent = task.timeSpent;
                if (task.startTime) {
                    timeSpent += (now - task.startTime) / 1000;
                }

                li.innerHTML = `
                    <div class="task-content ${task.completed ? 'completed' : ''}">
                        ${task.text}
                        <div class="task-info">
                            <span>Category: ${task.category}</span>
                            <span>Due: ${task.dueDate.toLocaleString()}</span>
                            <span>Time spent: ${formatTime(timeSpent)}</span>
                            ${task.startTime ? `<span>Started: ${task.startTime.toLocaleString()}</span>` : ''}
                            ${isOverdue ? '<span class="task-alert">Overdue!</span>' : ''}
                            ${isNearDue ? '<span class="task-alert">Due soon!</span>' : ''}
                        </div>
                    </div>
                    ${!task.completed ? `<button class="start-btn" onclick="startTask(${task.id})">${task.startTime ? 'In Progress' : 'Start'}</button>` : ''}
                    <button class="complete-btn" onclick="toggleComplete(${task.id})">
                        ${task.completed ? 'Undo' : 'Complete'}
                    </button>
                    <button class="delete-btn" onclick="deleteTask(${task.id})">Delete</button>
                `;
                taskList.appendChild(li);
            });

            updateStats();
        }

        function filterTasks() {
            renderTasks();
        }

        function updateStats() {
            const totalTasks = tasks.length;
            const completedTasks = tasks.filter(task => task.completed).length;
            document.getElementById('totalTasks').textContent = `Total tasks: ${totalTasks}`;
            document.getElementById('completedTasks').textContent = `Completed tasks: ${completedTasks}`;
        }

        // Update tasks every minute to refresh time information
        setInterval(renderTasks, 60000);

        // Initial render
        renderTasks();
    </script>
</body>
</html>
## Project Overview

Nadhiri Time Management is a web-based application designed to help professionals efficiently manage their tasks and time. Built with HTML, CSS, and JavaScript, this app offers a clean, intuitive interface for tracking tasks, deadlines, and time spent on various activities.

## Key Features

- **Task Management**: Easily add, edit, and delete tasks with customizable categories.
- **Time Tracking**: Monitor time spent on each task with a built-in timer function.
- **Due Date Alerts**: Receive visual alerts for upcoming and overdue tasks.
- **Category Filtering**: Organize and view tasks by categories such as Work, Personal, or Study.
- **Progress Tracking**: Mark tasks as complete and view overall progress statistics.
- **Responsive Design**: Access and manage tasks seamlessly across various devices.

## Technical Highlights

- Pure HTML, CSS, and JavaScript implementation
- No external libraries or frameworks required
- Clean and professional UI with a focus on user experience
- Local storage functionality for persistent data (feature to be added)

## Target Audience

Nadhiri Time Management is ideal for professionals, students, and anyone looking to enhance their productivity through better time management and task organization.

## Future Enhancements

- User authentication and cloud sync
- Detailed analytics and reporting features
- Integration with calendar applications
- Mobile app versions for iOS and Android

Nadhiri Time Management aims to simplify the complexities of time management, helping users focus on what matters most in their professional and personal lives.
