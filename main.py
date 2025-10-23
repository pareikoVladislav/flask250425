from flask import Flask, request


app = Flask(__name__)
# http://127.0.0.1:5000
# @app.route('/')  # http://127.0.0.1:5000/home
# def home_page() -> str:
#     return "HELLO FROM OUR FIRST FLASK APP!!!"
#
#
# @app.route('/products')
# def get_list_of_products() -> str:
#     # ...
#     return "LIST OF PRODUCTS"
#
#
# @app.route('/user/<string:username>')
# def get_user_info(username: str) -> str:
#     return f"'{username}' USER INFO"
#
#
# @app.route('/<int:user_id>')
# def get_user_by_id(user_id: int) -> str:
#     return f"User with ID {user_id}"
#
#
# @app.route('/files/<path:file_path>')
# def get_file_by_path(file_path: str) -> str:
#     return f"File with path {file_path}"

users = {1: "Alice", 2: "Bob", 3: "Charlie"}



# HTTP METHODS:
#   GET -- посмотреть
#   POST -- создать
#   PUT \ PATCH -- обновить
#   DELETE -- удалить


# http://127.0.0.1:5000/1  PUT
@app.route('/<int:user_id>', methods=['PUT'])
def update_user_profile_by_id(user_id) -> str:
    name = users.get(user_id)
    if user_id not in users:
        return f"User with ID {user_id} not found"
    data = request.get_json()
    new_name = data.get("name")
    users[user_id] = new_name
    return f"Updated name {new_name}, old name was {name}"


if __name__ == "__main__":
    app.run(debug=True)
