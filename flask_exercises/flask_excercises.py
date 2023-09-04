from flask import Flask, request


class FlaskExercise:
    """
    Вы должны создать API для обработки CRUD запросов.
    В данной задаче все пользователи хранятся в одном словаре, где ключ - это имя пользователя,
    а значение - его параметры. {"user1": {"age": 33}, "user2": {"age": 20}}
    Словарь (dict) хранить в памяти, он должен быть пустым при старте flask.
	
    POST /user - создание пользователя.
    В теле запроса приходит JSON в формате {"name": <имя пользователя>}.
    Ответ должен вернуться так же в JSON в формате {"data": "User <имя пользователя> is created!"}
    со статусом 201.
    Если в теле запроса не было ключа "name", то в ответ возвращается JSON
    {"errors": {"name": "This field is required"}} со статусом 422

    GET /user/<name> - чтение пользователя
    В ответе должен вернуться JSON {"data": "My name is <name>"}. Статус 200

    PATCH /user/<name> - обновление пользователя
    В теле запроса приходит JSON в формате {"name": <new_name>}.
    В ответе должен вернуться JSON {"data": "My name is <new_name>"}. Статус 200

    DELETE /user/<name> - удаление пользователя
    В ответ должен вернуться статус 204
    """
    
    @staticmethod
    def configure_routes(app: Flask) -> None:
        users_data = {}
        
        @app.post('/user')
        def post():
            input_data = request.get_json()
            if not "name" in input_data:
                return {"errors": {"name": "This field is required"}}, 422
            
            user = input_data["name"]
            
            users_data[user] = f"My name is {user}"
            return {"data": f"User {user} is created!"}, 201
                
            
        @app.get('/user/<username>')
        def get(username):
            output_data = users_data.get(username, None)
            if output_data:
                return {"data": output_data}, 200
            return {"error": "User not found"}, 404
        
        
        @app.patch('/user/<username>')
        def patch(username):
            user = users_data.get(username, None)
            if user:
                data = request.get_json()
                users_data[username] = f"My name is {data['name']}"
                return {"data": users_data[username]}, 200
            return {"error": "User not found"}, 404
                        
            
        @app.delete('/user/<username>')
        def delete(username):
            user = users_data.get(username, None)
            if user:
                users_data.pop(username)
                return "", 204
            return {"error": "User not found"}, 404
        
        
