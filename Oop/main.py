class Error:

    @staticmethod
    def error_500() -> None:
        print("Internal server error")

    @staticmethod
    def error_404() -> None:
        print("Not found")

if __name__ == '__main__':
    Error.error_500()