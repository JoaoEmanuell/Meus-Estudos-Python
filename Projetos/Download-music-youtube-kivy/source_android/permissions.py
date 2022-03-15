class Android:
    def __init__(self) -> None:
        try:
            from android.storage import app_storage_path, primary_external_storage_path, secondary_external_storage_path
            from android.permissions import request_permissions, Permission
            request_permissions([Permission.WRITE_EXTERNAL_STORAGE])
        except:
            print('Plataforma invalida, permissões do android invalidas!')