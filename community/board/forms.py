from django import forms


class BoardForm(forms.Form):
    title = forms.CharField(
        error_messages={
            'require': '제목을 입력해주세요.'
        },
        max_length=128,
        label='제목'
    )
    contents = forms.CharField(
        error_messages={
            'require': '내용을 입력해주세요.'
        },
        widget=forms.Textarea,
        label='내용'
    )
    tags = forms.CharField(
        # Tag 가 필수는 아니기 때문에 False 로 설
        required=False,
        widget=forms.Textarea,
        label='태그'
    )