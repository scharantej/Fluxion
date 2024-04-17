## Design for Software Dev Life Cycle Web App Project

### HTML Files

- **index.html**: The main page of the application. It will display a list of software development life cycle phases and provide links to each phase's detailed page.
- **phase1.html**, **phase2.html**, **phase3.html**, ...: Individual pages for each phase of the software development life cycle. These pages will contain detailed information about each phase, including the tasks involved, the deliverables, and the best practices.

### Routes

- **@app.route('/')**: The route for the main page, which will display the list of software development life cycle phases.
- **@app.route('/phase/<phase_number>')**: The route for the detailed page of a specific phase, where `<phase_number>` is the number of the phase (e.g., `/phase/1` for the first phase).
- **@app.route('/phase/<phase_number>/add_task')**: The route for adding a new task to a specific phase, where `<phase_number>` is the number of the phase.
- **@app.route('/phase/<phase_number>/delete_task/<task_id>')**: The route for deleting a task from a specific phase, where `<phase_number>` is the number of the phase and `<task_id>` is the ID of the task.
- **@app.route('/phase/<phase_number>/edit_task/<task_id>')**: The route for editing a task from a specific phase, where `<phase_number>` is the number of the phase and `<task_id>` is the ID of the task.