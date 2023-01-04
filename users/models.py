from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.db import models

class UserManager(BaseUserManager):
    """
    Clase encargada de gestionar la creación de usuarios y superusuarios
    """
    def create_user(self, email, password=None, **extra_fields):
        """
        Crea y guarda un usuario con el email y la contraseña especificados.
        """
        if not email:
            raise ValueError('El email es obligatorio')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Crea y guarda un superusuario con el email y la contraseña especificados.
        """
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    """
    Clase que representa al modelo de usuario en la base de datos.
    """
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()
    
    USERNAME_FIELD = 'email'

