def login(username, password):
    if username == 'Admin' and password == 'Secret':
        return 'Login succesful'
    return 'Invalid Credetianls'

def test_user_registration():
    # Arrange
    user_data = {"username": "john", "email": "john@example.com"}
    db = InMemoryDatabase()

    # Act
    db.register_user(user_data)

    # Assert
    assert db.get_user("john")["email"] == "john@example.com"

    # Cleanup
    db.delete_user("john")  # optional in real pytest since each test should be isolated
