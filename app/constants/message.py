class UserMessages:
    CREATED = "User created successfully."
    EXISTS = "A user with this email already exists."
    INVALID_CREDENTIALS = "Invalid email or password."

class AuthMessages:
    UNAUTHORIZED = "You are not authorized to perform this action."
    PASSWORD_RESET = "Password has been reset successfully."
    LOGGED_IN = "Logged in successfully."


class DBMessages:
    ERROR = "Database error occurred. Please try again later."
    NOT_FOUND = "Requested resource not found."

class JWTMessages:
    INVALID_TOKEN = "Invalid token. Please log in again."
    TOKEN_EXPIRED = "Token has expired. Please log in again."