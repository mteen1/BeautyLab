from django.shortcuts import get_object_or_404
from ninja import Router
from .models import Profile, CustomUser
from .schemas import ProfileDetailOut, ProfileIn, UserIn, UserOut
from .customjwt import JWTAuth


router = Router()


@router.get("users/", response=list[UserOut])
def get_users(request):
    """get the list of users"""
    users = CustomUser.objects.filter(is_staff=False)
    return users


@router.post("users/")
def create_user(request, user_data: UserIn):
    """create user object"""
    # Validate user_data and create a new user
    # Example: Create a CustomUser instance
    user = CustomUser(username=user_data.username, email=user_data.email)
    user.set_password(user_data.password)
    user.save()
    return {"message": "User created successfully"}


@router.get("profiles/{id}/", response=ProfileDetailOut)
def get_profile(request, id: int):
    """get profile based on the id"""
    return get_object_or_404(Profile, id=id)


@router.post("profiles/", auth=JWTAuth())
def create_profile(request, profile_data: ProfileIn):
    """creates a profile, the user should be present"""
    user = request.auth.user
    profile = Profile(user=user)
    profile.save()
    return {"message": "Profile created successfully"}
