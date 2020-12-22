from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render, redirect
from .models import Board
from .forms import BoardForm
from myuser.models import Myuser
from tag.models import Tag


def board_detail(request, pk):
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404('게시글을 찾을 수 없습니다.')

    return render(request, 'board_detail.html', {'board': board})

def board_wirte(request):

    # login 하지 않은 채 접속을 시도하면 로그인 창으로 이동 시킴.
    if not request.session.get('user'):
        return redirect('/myuser/login')

    if request.method == 'GET':
        form = BoardForm()

    elif request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            # username 을 session 에서 가져옴
            user_id = request.session.get('user')
            user = Myuser.objects.get(pk=user_id)

            board = Board()
            board.title = form.cleaned_data['title']
            board.contents = form.cleaned_data['contents']
            # writer 부분에 user 를 통채로 넘겨줌.
            board.writer = user
            # DB 에 저장
            board.save()

            tags = form.cleaned_data['tags'].split(',')

            if len(tags) > 0:
                for tag in tags:
                    # get_or_create : tag 가 이미 존재하면 가져오고 없으면 생성을 함
                    # created 는 새로 생성 한 것인지를 알려줌.
                    # 우리는 사용 하지 않을 것임으로 _ 하나 작성해줌.
                    # _tag, created = Tag.objects.get_or_create(name=tag)
                    _tag, _ = Tag.objects.get_or_create(name=tag)
                    # 태그를 board 에 추가해줌
                    board.tags.add(_tag)

            return redirect('/board/list')

    return render(request, 'board_write.html', {'form': form})

def board_list(request):

    # order_by : 정렬
    # -id : id 를 내림 차순으로 가져오겠다. :: 최신순으로 보겠다.
    all_boards = Board.objects.all().order_by('-id')
    page = int(request.GET.get('p', 1))

    # Paginator(전체 게시글, 몇 개씩 보여줄 것인지)
    paginator = Paginator(all_boards, 1)

    boards = paginator.get_page(page)

    return render(request, 'board_list.html', {'boards': boards})
