@app.route('/todos', methods=['GET'])
def get_todos():
    todos = Todo.query.all()
    todos = list(map(lambda todo: todo.serialize(), todos))
    return jsonify(todos), 200

@app.route('/todos', methods=['POST'])
def add_todo():
    data = request.get_json()
    new_todo = Todo(label=data['label'], done=data['done'])
    db.session.add(new_todo)
    db.session.commit()
    todos = Todo.query.all()
    todos = list(map(lambda todo: todo.serialize(), todos))
    return jsonify(todos), 201

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todo = Todo.query.get(position)
    if todo is None:
        return jsonify({"error": "Todo not found"}), 404

    db.session.delete(todo)
    db.session.commit()
    todos = Todo.query.all()
    todos = list(map(lambda todo: todo.serialize(), todos))
    return jsonify(todos), 200
