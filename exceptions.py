class LibraryError(Exception):
    pass


class InvalidTittleError(LibraryError):
    pass

class LimitExceededError(LibraryError):
    """Se excedio el límite de prestamos permitidos"""
    pass

class BookNotAvailableError(LibraryError):
    """El libro no se encuentra disponible"""
    pass

class UserNotFoundError(LibraryError):
    """El usuario no se encuentra registrado"""
    pass