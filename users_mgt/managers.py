from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("請填入信箱")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        # check_initial_club()
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('user_type', "CENTERMEMBER")

        # if extra_fields.get('user_type') is not "CenterMember":
        #     raise ValueError("Superuser 中的 user_type 不是 社團中心成員")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser 中的 is_superuser 欄位必須是 True")
        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser 中的 is_staff 欄位必須是 True")
        return self._create_user(email, password, **extra_fields)
