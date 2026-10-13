from django import forms
from .models import Post


class PostForm(forms.ModelForm):

    def clean_cover_image(self):
        image = self.cleaned_data.get("cover_image")

        if image:
            if image.size > 5 * 1024 * 1024:
                raise forms.ValidationError(
                    "Image file too large (max 5MB)."
                )

            valid_extensions = [".jpg", ".jpeg", ".png", ".webp"]

            if not any(
                image.name.lower().endswith(ext)
                for ext in valid_extensions
            ):
                raise forms.ValidationError(
                    "Unsupported file type. Use JPG, PNG, or WEBP."
                )

        return image

    class Meta:
        model = Post
        fields = "__all__"