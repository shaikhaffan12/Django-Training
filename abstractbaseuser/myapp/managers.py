from django.contrib.auth.models import BaseUserManager

class UserAccountManager(BaseUserManager):
    use_in_migrations = True

    def create_user_here(self,email,name,phone,password,**extra_fields):
        values = [email,name,phone]
        field_value_map = dict(zip(self.model.REQUIRED_FIELDS,values))
        for field_name, value in field_value_map.items():
            if not value:
                raise ValueError(f'The {field_name} value must be set')
        email = self.normalize_email(email)
        user = self.model(
            email = email,
            name = name,
            phone = phone,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user
        
    def create_user(self, email, name, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self.create_user_here(email, name, phone, password, **extra_fields)
    
    def create_superuser(self, email, name, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Super user needs to be is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Super user needs to be is_superuser=true')

        return self.create_user_here(email, name, phone, password, **extra_fields)