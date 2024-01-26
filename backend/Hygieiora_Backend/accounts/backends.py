from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model


class RoleBasedBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        user_model = get_user_model()
        try:
            user = user_model.objects.get(email=email)
        except user_model.DoesNotExist:
            return None

        # Check user's role and validate accordingly
        if user.role == "patient" and user.email.endswith("st.knust.edu.gh"):
            if user.check_password(password):
                return user
        elif user.role == "doctor":
            if user.check_password(password):
                return user

        return None

    def get_user(self, user_id):
        user_model = get_user_model()
        try:
            return user_model.objects.get(pk=user_id)
        except user_model.DoesNotExist:
            return None
