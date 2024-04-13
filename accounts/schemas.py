from ninja import ModelSchema
from .models import Profile, CustomUser


class UserIn(ModelSchema):
    class Meta:
        model = CustomUser
        fields = ("username", "password", "email")


class UserOut(ModelSchema):
    class Meta:
        model = CustomUser
        fields = ("username", "email")


class ProfileDetailOut(ModelSchema):
    user: UserOut
    skin_concerns: list[str]
    ing_prefer: list[str] | None = None
    ing_sensitive: list[str] | None = None

    class Meta:
        model = Profile
        fields = (
            "id",
            "user",
            "skin_type",
            "skin_concerns",
            "ing_prefer",
            "ing_sensitive",
        )

    @staticmethod
    def resolve_skin_concerns(obj):
        return [skin_concern.name for skin_concern in obj.skin_concerns.all()]

    @staticmethod
    def resolve_ing_prefer(obj):
        return [ingredient.name for ingredient in obj.ing_prefer.all()]

    @staticmethod
    def resolve_ing_sensitive(obj):
        return [ingredient.name for ingredient in obj.ing_sensitive.all()]



class ProfileIn(ModelSchema):
    user: UserIn | None = None
    skin_concerns: list[int] | None = None
    ing_prefer: list[int] | None = None
    ing_sensitive: list[int] | None = None

    class Meta:
        model = Profile
        fields = ("user", "skin_type", "skin_concerns", "ing_prefer", "ing_sensitive")
